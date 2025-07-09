import pytest
from src.entrypoints.routes.autenticacao_router import obter_usuario_atual
from src.service.unit_of_work import UnidadeDeTrabalho
from src.domain import JWTToken
from tests.mock import mock_criar_usuario, mock_usuario_teste
from fastapi import HTTPException

def test_obter_usuario_api(
    client,
    session_maker,
    mock_criar_usuario,
):
    # Recuperando um usuário existente
    response = client.post("auth/login",json={
        "email":"usuario1@teste.com",
        "senha":"123",
    })

    token = response.json()['token']
    usuario = obter_usuario_atual(
        uow=UnidadeDeTrabalho(session_maker),
        token=f"Bearer {token}"
    )

    assert usuario['email'] == "usuario1@teste.com"
    assert usuario['nome'] == "Usuário 01"

    # Recuperando um usuário não existente
    with pytest.raises(HTTPException):
        usuario = obter_usuario_atual(token=None)
