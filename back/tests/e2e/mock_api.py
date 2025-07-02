import pytest 
from tests.mock import criador_de_usuario
from src.domain.value_objects import JWTToken

@pytest.fixture
def retrieve_token(client):
    def _retrieve_token(email: str, senha: str):
        response = client.post("auth/login",json={
            "email":email,
            "senha":senha,
        })
        return response.json()['token']
    yield _retrieve_token

@pytest.fixture
def criar_usuario_e_token(criador_de_usuario):
    def _criar_usuario_e_token(
        cpf="92470179041",
        nome="Usuário Teste",
        email="usuario@teste.com",
        senha="senha_segura123",
        telefone="84912345678",
        eh_barbeiro=False,  
    ) -> tuple[dict, str]:
        # Criando usuário
        usuario = criador_de_usuario(
            cpf=cpf, 
            nome=nome,
            email=email,
            senha=senha,
            telefone=telefone,
            eh_barbeiro=eh_barbeiro,
        )

        jwt_token = JWTToken(usuario.to_token())

        # Devolvendo usuário e token
        return usuario, jwt_token.token
    yield _criar_usuario_e_token