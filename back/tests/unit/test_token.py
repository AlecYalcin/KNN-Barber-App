import pytest
from src.domain import Usuario, JWTToken, TokenInvalido
from tests.mock import mock_usuario_teste

def test_criacao_de_token(
    mock_usuario_teste
):
    # Criando usuário qualquer
    usuario = mock_usuario_teste

    # Codando informações de usuário
    jwt_token = JWTToken(usuario.to_dict())

    # Verificando validade
    assert jwt_token.token is not None
    assert jwt_token.token_extraido == usuario.to_dict()

def test_identidade_de_tokens(
    mock_usuario_teste
):
    # Criand usuários quaisquer
    usuario_1 = mock_usuario_teste
    usuario_2 = mock_usuario_teste

    # Codando informações de ambos
    jwt_usuario_1 = JWTToken(usuario_1.to_dict())
    jwt_usuario_2 = JWTToken(usuario_2.to_dict())

    assert jwt_usuario_1.token == jwt_usuario_2.token
    assert jwt_usuario_1.token_extraido == jwt_usuario_2.token_extraido

def test_validade_de_token():
    # Criando Token
    jwt_token = JWTToken({})

    # Assimilando um valor qualquer para ele
    jwt_token.token = "qualquer_coisa"

    with pytest.raises(TokenInvalido):
        assert isinstance(jwt_token.token_extraido, str) 