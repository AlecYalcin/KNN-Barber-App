import pytest
from src.service.unit_of_work import UnidadeDeTrabalho
from src.service.services.autorizacao import *
from src.domain.exceptions import *
from src.domain.models import JWTToken
from tests.mock import *

def test_autenticar_service(
    session_maker,
    mock_criar_usuario,
):
    # Autenticação com usuário não existente
    with pytest.raises(UsuarioNaoEncontrado):
        with UnidadeDeTrabalho(session_maker) as uow:
            token = autenticar(
                uow=uow,
                email="email-inexistente",
                senha="senha-inexistente",
            )   

    # Autenticação com senha errada
    with pytest.raises(UsuarioNaoEncontrado):
        with UnidadeDeTrabalho(session_maker) as uow:
            token = autenticar(
                uow=uow,
                email="usuario1@teste.com",
                senha="senha-errada"
            )

    # Autenticação com sucesso
    with UnidadeDeTrabalho(session_maker) as uow:
        token = autenticar(
            uow=uow,
            email="usuario1@teste.com",
            senha="123"
        )

    # Verificando se token bate com o usuário
    usuario_extraido = JWTToken.extrair_token(token)
    with UnidadeDeTrabalho(session_maker) as uow:
        usuario_encontrado = uow.usuarios.consultar_por_email("usuario1@teste.com")
        assert usuario_extraido == usuario_encontrado.to_token()

def test_registrar_service(session_maker):
    # Criando usuário
    with UnidadeDeTrabalho(session_maker) as uow:
        token = registrar(
            uow=uow,
            cpf="88764164047",
            nome="Fulano",
            email="fulano@gmail.com",
            senha="12345",
            telefone="4421084326",
        )

    # Verificando se foi criado
    with UnidadeDeTrabalho(session_maker) as uow:
        usuario = uow.usuarios.consultar(cpf="88764164047")
        assert usuario is not None

        # Verificando se token bate com informações
        usuario_extraido = JWTToken.extrair_token(token)
        assert usuario_extraido == usuario.to_token()

    # =================
    # ATENÇÃO!
    # O teste de EXCEÇÕES de registro NÃO precisa ser implementado.
    # O test_criar_usuario_service presente no arquivo 
    # test_autorizacao_services.py já realiza esse trabalho. 
    # ==================

def test_retornar_usuario_service(
    session_maker,
    mock_criar_usuario,                                 
):
    # Autenticação com sucesso
    with UnidadeDeTrabalho(session_maker) as uow:
        token = autenticar(
            uow=uow,
            email="usuario1@teste.com",
            senha="123"
        )
    
    # Retornando usuário a partir de token
    usuario_do_token = retornar_usuario(
        uow=UnidadeDeTrabalho(session_maker),
        token=token,
    )

    # Verificando se é um usuário válido
    assert usuario_do_token.get('cpf') is not None
    assert usuario_do_token.get('nome') is not None
    assert usuario_do_token.get('email') is not None
    assert usuario_do_token.get('senha') is not None

    # Verificando se é um usuário existente
    with UnidadeDeTrabalho(session_maker) as uow:
        usuario_encontrado = uow.usuarios.consultar_por_email(email="usuario1@teste.com")
        assert usuario_do_token == usuario_encontrado.to_dict()