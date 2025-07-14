from src.domain.value_objects import JWTToken
from src.service.unit_of_work import AbstractUnidadeDeTrabalho
from src.domain.models import Usuario
from src.domain.exceptions import (
    CPFInvalido, 
    CPFEmUso, 
    EmailInvalido, 
    EmailEmUso,
    UsuarioNaoEncontrado,
    PermissaoNegada,
)
from sqlalchemy.orm.exc import UnmappedInstanceError
from sqlalchemy.exc import IntegrityError

def criar_usuario(
    uow: AbstractUnidadeDeTrabalho,
    cpf: str,
    nome: str, 
    email: str,
    senha: str,
    telefone: str | None = None,
    eh_barbeiro: bool = False,
) -> dict:
    """
    Serviço de criação de novos usuários no sistema.

    Args:
        uow(AbstractUnidadeDeTrabalho): Unidade de trabalho abstrata
        cpf(str): CPF do cliente novo
        nome(str): Nome do cliente novo
        email(str): Email do cliente novo
        senha(str): Senha do cliente novo 
        telefone(str|None): Telefone do cliente novo
        eh_barbeiro(bool): Designação de barbeiro ou cliente
    Raises:
        CPFInvalido: O CPF informado não é válido.
        EmailInvalido: O Email informado não é válido.
        CPFEmUso: O CPF já está cadastrado.
        EmailEmUso: O Email já está cadastrado.
    """

    # Verificar se CPF é válido
    if not Usuario.validar_cpf(cpf):
        raise CPFInvalido("O CPF informado não é válido.")

    # Verificar se Email é válido
    if not Usuario.validar_email(email):
        raise EmailInvalido("O Email informado não é válido.")

    with uow:
        # Verificar se já existe usuário com mesmo cpf
        usuario_com_mesmo_cpf = uow.usuarios.consultar(cpf=cpf)
        if usuario_com_mesmo_cpf:
            raise CPFEmUso("O CPF já está cadastrado.")
        # Verificar se já existe usuário com mesmo email
        usuario_com_mesmo_email = uow.usuarios.consultar_por_email(email=email)
        if usuario_com_mesmo_email:
            raise EmailEmUso("O Email já está cadastrado.")
        # Criando usuário
        usuario = Usuario(cpf, nome, email, senha, telefone, eh_barbeiro)
        uow.usuarios.adicionar(usuario)
        uow.commit()
    return usuario.to_dict()

def consultar_usuario(
    uow: AbstractUnidadeDeTrabalho,
    cpf: str | None = None,
    email: str | None = None,
    solicitante: dict | None = None,
) -> dict:
    """
    Serviço de consulta de usuários existentes no sistema.

    Args:
        uow(AbstractUnidadeDeTrabalho): Unidade de trabalho abstrata
        cpf(str): CPF para consulta, priorizado
        email(str): Email para consulta, caso não haja CPF
        solicitante(dict): Usuário que está solicitando a operação
    Returns:
        dict: dicionário de dados com as informações do usuário para o endpoint.
        Caso não exista usuário, será enviado um dicionário vazio.
    Raises:
        PermissaoNegada: O usuário não possui permissões para realizar essa operação.
    """
    
    # Verificando permissão de usuário
    if ( 
        solicitante 
        and solicitante['cpf'] != cpf 
        and solicitante['eh_barbeiro'] == False
    ):
        raise PermissaoNegada()

    usuario = None
    with uow:
        if cpf:
            usuario = uow.usuarios.consultar(cpf=cpf)
        elif email:
            usuario = uow.usuarios.consultar_por_email(email=email)
        if not usuario:
            return {}
        return usuario.to_dict()

def remover_usuario(
    uow: AbstractUnidadeDeTrabalho,
    cpf: str,
    solicitante: dict | None = None,
) -> None:
    """
    Serviço de deletar usuários existentes no sistema.
    
    Args:
        uow(AbstractUnidadeDeTrabalho): Unidade de trabalho abstrata
        cpf(str): CPF do cliente a ser removio
        solicitante(dict): Usuário que está solicitando a operação
    Raises:
        UsuarioNaoEncontrado: O cpf informado não foi encontrado na base de dados.
    Raises:
        PermissaoNegada: O usuário não possui permissões para realizar essa operação.
    """
    
    # Verificando permissão de usuário
    if ( 
        solicitante 
        and solicitante['cpf'] != cpf 
        and solicitante['eh_barbeiro'] == False
    ):
        raise PermissaoNegada()

    with uow:
        try:
            uow.usuarios.remover(cpf=cpf)
            uow.commit()
        except UnmappedInstanceError:
            raise UsuarioNaoEncontrado("O cpf informado não foi encontrado na base de dados.")

def atualizar_usuario(
    uow: AbstractUnidadeDeTrabalho,
    cpf: str,
    novo_nome: str | None = None,
    novo_email: str | None = None,
    novo_telefone: str | None = None,
    nova_senha: str | None = None,
    solicitante: dict | None = None,
) -> str:
    """
    Serviço para alterar usuários existentes no sistema.

    Args:
        cpf(str): CPF do usuário a ser alterado
        novo_nome(str): Novo nome para o usuário
        novo_email(str): Novo email para o usuário
        novo_telefone(str): Novo telefone para o usuário
        nova_senha(str): Nova senha para o usuário
        solicitante(dict): Usuário que está solicitando a operação
    Raises:
        EmailInvalido: O Email informado não é válido.
        UsuarioNaoEncontrado: Usuário não foi encontrado para a alteração.
        EmailEmUso: O Email escolhido já está cadastrado em outro usuário.
        PermissaoNegada: O usuário não possui permissões para realizar essa operação.
    """
    
    # Verificando permissão de usuário
    if ( 
        solicitante 
        and solicitante['cpf'] != cpf 
        and solicitante['eh_barbeiro'] == False
    ):
        raise PermissaoNegada()

    # Verificar se Email é válido
    if not Usuario.validar_email(novo_email):
        raise EmailInvalido("O Email informado não é válido.")

    # Criando usuário novo base
    novo_usuario = Usuario(
        cpf=cpf, 
        nome=novo_nome, 
        email=novo_email, 
        senha=nova_senha, 
        telefone=novo_telefone
    )

    # Realizando alteração
    with uow:
        try:
            uow.usuarios.alterar(cpf=cpf, novo_usuario=novo_usuario)
            uow.commit()
        except AttributeError:
            raise UsuarioNaoEncontrado("Usuário não foi encontrado para a alteração.")
        except IntegrityError:
            raise EmailEmUso("O Email escolhido já está cadastrado em outro usuário.")

    # Devolvendo token com valores atualizados
    with uow:
        usuario = uow.usuarios.consultar(cpf)
        jwt_token = JWTToken({            
            "cpf": usuario.cpf,
            "nome": usuario.nome,
            "email": usuario.email,
            "telefone": usuario.telefone,
            "eh_barbeiro": usuario.eh_barbeiro,
        })
        return jwt_token.token