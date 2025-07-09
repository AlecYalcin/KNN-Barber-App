from tests.mock import mock_criar_usuario, mock_usuario_teste
from src.domain import JWTToken

def test_login_api(
    client,
    mock_criar_usuario,
):
    # Login com usuário não existente
    response = client.post("auth/login",json={
        "email":"email-inexistente",
        "senha":"senha-inexistente",
    })

    assert response.status_code == 404
    assert response.json() == {"error":"UsuarioNaoEncontrado","mensagem":"Não foi encontrado um usuário com esse email e senha."}

    # Login com um usuário existente mas senha errada
    response = client.post("auth/login",json={
        "email":"usuario1@teste.com",
        "senha":"senha-inexistente",
    })

    assert response.status_code == 404
    assert response.json() == {"error":"UsuarioNaoEncontrado","mensagem":"Não foi encontrado um usuário com esse email e senha."}

    # Login com usuário existente
    response = client.post("auth/login",json={
        "email":"usuario1@teste.com",
        "senha":"123",
    })

    # Verificando resposta
    assert response.status_code == 200
    assert response.json() is not None

    # Verificando se o token está realmente pegando os valores certos
    token_info = JWTToken.extrair_token(response.json()['token'])
    assert token_info['cpf'] == "05705608020"
    assert token_info['eh_barbeiro'] == False

def test_register_api(
    client,
    mock_usuario_teste,
):
    usuario = mock_usuario_teste

    # Registrar usuário com sucesso
    response = client.post("auth/register", json={
        **usuario.to_dict(),
    })

    # Verificando resposta
    assert response.status_code == 200
    assert response.json() is not None

    # Verificando se o token está realmente pegando os valores certos
    token_info = JWTToken.extrair_token(response.json()['token'])
    assert token_info['cpf'] == usuario.cpf
    assert token_info['eh_barbeiro'] == usuario.eh_barbeiro

    # =================
    # ATENÇÃO!
    # O teste de EXCEÇÕES de registro NÃO precisa ser implementado.
    # O test_usuario_api presente no arquivo 
    # test_usuario_api.py já realiza esse trabalho. 
    # ==================