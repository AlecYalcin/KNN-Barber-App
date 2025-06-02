from src.service.unit_of_work import AbstractUnidadeDeTrabalho
from src.domain.models import Usuario
from src.domain.exceptions import (
    CPFInvalido, 
    CPFEmUso, 
    EmailInvalido, 
    EmailEmUso,
)

def criar_usuario(
    uow: AbstractUnidadeDeTrabalho,
    cpf: str,
    nome: str, 
    email: str,
    senha: str,
    telefone: str | None = None,
    eh_barbeiro: bool = False,
) -> None:
    """
    Serviço de criação de novos usuários no sistema.

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

def consultar_usuario(
    uow: AbstractUnidadeDeTrabalho,
    cpf: str | None = None,
    email: str | None = None,
) -> dict:
    
    usuario = None
    with uow:
        if cpf:
            usuario = uow.usuarios.consultar(cpf=cpf)
        elif email:
            usuario = uow.usuarios.consultar_por_email(email=email)
        if not usuario:
            return {}
        return usuario.to_dict()

def atualizar_usuario():
    """"""

def deletar_usuario():
    """"""

