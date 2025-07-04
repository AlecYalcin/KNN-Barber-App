from src.service.unit_of_work import AbstractUnidadeDeTrabalho
from src.domain.value_objects import JWTToken
from src.domain.exceptions import (
    UsuarioNaoEncontrado,
    TokenInvalido,
)
from src.service.services.usuario import criar_usuario

def autenticar(
    uow: AbstractUnidadeDeTrabalho,
    email: str,
    senha: str,
) -> str:
    """
    Função para reconhecer se um email e senha existem no banco de dados e retornar um Token JWT

    Args:
        uow(AbstractUnidadeDeTrabalho): Unidade de trabalho abstrata
        email(str): Email da conta
        senha(str): Senha da conta
    Returns:
        str: token_jwt gerado com as informações do usuário
    Raises:
        UsuarioNaoEncontrado: Não foi encontrado um usuário com esse email e senha.
    """
    
    # Encontrando se o usuário existe
    with uow:
        # Procurnado por usuário existente
        usuario = uow.usuarios.consultar_por_email(email)

        # Verificando existência e campos
        if usuario is None or usuario.senha != senha:
            raise UsuarioNaoEncontrado("Não foi encontrado um usuário com esse email e senha.")
        
        # Gerando token 
        jwt_token = JWTToken(usuario.to_token())
        return jwt_token.token

def registrar(
    uow: AbstractUnidadeDeTrabalho,
    cpf: str,
    nome: str,
    email: str,
    senha: str,
    telefone: str | None = None,
) -> str:
    """
    Função para adicionar um novo usuário com nome, email, senha e telefone no banco de dados e retornar um Token JWT

    Args:
        uow(AbstractUnidadeDeTrabalho): Unidade de trabalho abstrata
        cpf(str): CPF do cliente novo
        nome(str): Nome do cliente novo
        email(str): Email do cliente novo
        senha(str): Senha do cliente novo 
        telefone(str|None): Telefone do cliente novo
    Returns:
        str: token_jwt gerado com as informações de usuário.
    """

    # Criando usuário com serviço já existente
    usuario = criar_usuario(
        uow=uow,
        cpf=cpf,
        nome=nome,
        email=email,
        senha=senha,
        telefone=telefone,
    )

    # Gerando token
    jwt_token = JWTToken({"cpf":usuario['cpf'],"eh_barbeiro":usuario['eh_barbeiro']})
    return jwt_token.token

def retornar_usuario(
    uow: AbstractUnidadeDeTrabalho,
    token: str,
) -> dict:
    """
    Função para reconhecer usuário a partir de um token JWT

    Args:
        uow(AbstractUnidadeDeTrabalho): Unidade de trabalho abstrata
        token(str): Token a ser extraído
    Returns:
        dict: informações do usuário encontrado
    Raises:
        TokenInvalido: o token passado não é válido.
        UsuarioNaoEncontrado: Não foi encontrado um usuário com esse token no sistema
    """

    # Verificando validade do token
    try:
        jwt_token = JWTToken.extrair_token(token)
    except TokenInvalido:
        raise TokenInvalido("o token passado não é válido.")
    
    # Encontrando usuário do token
    with uow:
        usuario = uow.usuarios.consultar(jwt_token['cpf'])

        # Verificando existência de usuário    
        if usuario is None:
            raise UsuarioNaoEncontrado("Não foi encontrado um usuário com esse token no sistema")
        
        return usuario.to_dict()
    