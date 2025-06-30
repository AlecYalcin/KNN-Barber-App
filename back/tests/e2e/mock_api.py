import pytest 

@pytest.fixture
def retrieve_token(client):
    def _retrieve_token(email: str, senha: str):
        response = client.post("auth/login",json={
            "email":email,
            "senha":senha,
        })
        return response.json()['token']
    yield _retrieve_token