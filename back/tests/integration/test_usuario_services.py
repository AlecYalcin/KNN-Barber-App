import pytest
from src.domain.models import Usuario
from src.domain.exceptions import *
from src.service import *
from src.adapters.repositories import UsuarioRepository
from tests.mock import *

def test_criar_usuario_service(session_maker):
    usuario = Usuario(
        cpf="12345678900",
        nome="Usuário Teste",
        email="email_invalido",
        senha="senhateste",
    )

    # Criação de usuário com CPF inválido
    with pytest.raises(CPFInvalido):
        criar_usuario(
            uow=UnidadeDeTrabalho(session_maker),
            cpf=usuario.cpf,
            nome=usuario.nome,
            email=usuario.email,
            senha=usuario.senha,
        )

    # Criação de usuário com Email inválido
    usuario.cpf = "54304796089"
    with pytest.raises(EmailInvalido):
        criar_usuario(
            uow=UnidadeDeTrabalho(session_maker),
            cpf=usuario.cpf,
            nome=usuario.nome,
            email=usuario.email,
            senha=usuario.senha,
        )

    # Criação de usuário com sucesso
    usuario.email = "email@teste.com.br"
    criar_usuario(
        uow=UnidadeDeTrabalho(session_maker),
        cpf=usuario.cpf,
        nome=usuario.nome,
        email=usuario.email,
        senha=usuario.senha,
    )

    with UnidadeDeTrabalho(session_maker) as uow:
        usuario_encontrado = uow.usuarios.consultar(usuario.cpf)
        assert usuario_encontrado == usuario

    # Criação de usuário com CPF já existente
    with pytest.raises(CPFEmUso):
        criar_usuario(
            uow=UnidadeDeTrabalho(session_maker),
            cpf=usuario.cpf,
            nome=usuario.nome,
            email=usuario.email,
            senha=usuario.senha,
        )

    # Criação de usuário com Email já existente
    usuario.cpf = "69980389095"
    with pytest.raises(EmailEmUso):
        criar_usuario(
            uow=UnidadeDeTrabalho(session_maker),
            cpf=usuario.cpf,
            nome=usuario.nome,
            email=usuario.email,
            senha=usuario.senha,
        )

def test_consultar_usuario_service(session_maker, mock_usuario_teste):
    usuario = mock_usuario_teste

    # Criando usuário através do repositório
    with UnidadeDeTrabalho(session_maker) as uow:
        uow.usuarios.adicionar(usuario)
        uow.commit()

    # Pesquisando por CPF
    usuario_encontrado = consultar_usuario(uow=UnidadeDeTrabalho(session_maker), cpf=usuario.cpf)
    assert usuario_encontrado == usuario.to_dict()
    
    # Pesquisando por Nome
    usuario_encontrado = consultar_usuario(uow=UnidadeDeTrabalho(session_maker), email=usuario.email)
    assert usuario_encontrado == usuario.to_dict()

    # Pesquisando por um CPF inexistente
    usuario_inexistente = consultar_usuario(uow=UnidadeDeTrabalho(session_maker), cpf="111.222.333.444-55")
    assert usuario_inexistente == {}

    # Pesquisando por um Email inexistente
    usuario_inexistente = consultar_usuario(uow=UnidadeDeTrabalho(session_maker), email="email@inexistente.com")
    assert usuario_inexistente == {}
