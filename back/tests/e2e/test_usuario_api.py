from tests.mock import mock_usuario_teste, mock_criar_usuario

def test_usuario_api(client):
    # Criar Usuário
    response = client.post("usuario/criar",json={
        "cpf":"70056454481",
        "nome":"Alec Yalçin",
        "email":"alecyalcin@teste.com",
        "senha":"senhaForte123",
        "telefone":"84987626875",
    })

    assert response.status_code == 201
    assert response.json() == {"mensagem":"Sucesso ao criar usuário!"}

    # Consultar Usuário
    response = client.get("usuario/70056454481")

    assert response.status_code == 200
    assert response.json() == {
        "cpf":"70056454481",
        "nome":"Alec Yalçin",
        "email":"alecyalcin@teste.com",
        "senha":"senhaForte123",
        "telefone":"84987626875",
        "eh_barbeiro":False,
    }

    usuario_atual = response.json()
    usuario_atual['email'] = "alecyalcin15@teste.com"
    usuario_atual['nome'] = "Alec Can Yalçin"
    usuario_atual['telefone'] = "84911112222"

    # Alterar Usuário
    response = client.patch("usuario/70056454481",json=usuario_atual)

    assert response.status_code == 200
    assert response.json() == {"mensagem":"Usuário atualizado com sucesso!"}

    # Remover Usuário
    response = client.delete("usuario/70056454481")

    assert response.status_code == 200
    assert response.json() == {"mensagem":"O usuário foi excluído do sistema!"}

    response = client.get("usuario/70056454481")
    assert response.json() == {}

def test_usuario_api_criar_exceptions(
    client, 
    mock_usuario_teste,
    mock_criar_usuario,
):
    usuario = mock_usuario_teste
    usuario.cpf = "12345678900"
    usuario.email = "email_invalido"

    # CPFInvalido: O CPF informado não é válido.
    response = client.post("usuario/criar", json=usuario.to_dict())
    assert response.status_code == 400
    assert response.json() == {"error": "CPFInvalido", "mensagem": "O CPF informado não é válido."}

    # EmailInvalido: O Email informado não é válido.
    usuario.cpf = "70056454481"

    response = client.post("usuario/criar", json=usuario.to_dict())
    assert response.status_code == 400
    assert response.json() == {"error": "EmailInvalido", "mensagem": "O Email informado não é válido."}
    
    # CPFEmUso: O CPF já está cadastrado.
    usuario.email = "usuario_teste@email.com"
    usuario.cpf = "80990188000"

    response = client.post("usuario/criar", json=usuario.to_dict())
    assert response.status_code == 400
    assert response.json() == {"error": "CPFEmUso", "mensagem": "O CPF já está cadastrado."}

    # EmailEmUso: O Email já está cadastrado.
    usuario.cpf = "70056454481"
    usuario.email = "usuario1@teste.com"

    response = client.post("usuario/criar", json=usuario.to_dict())
    assert response.status_code == 400
    assert response.json() == {"error": "EmailEmUso", "mensagem": "O Email já está cadastrado."}

    # Exceções de Alterar usuário
    usuario.email = "email_original@gmail.com"


def test_usuario_api_alterar_exceptions(
    client,
    mock_usuario_teste,
    mock_criar_usuario,
):
    usuario = mock_usuario_teste

    response = client.post("usuario/criar", json=usuario.to_dict())
    assert response.status_code == 201

    # EmailInvalido: O Email informado não é válido.
    usuario.email = "email_invalido"

    response = client.patch(f"usuario/{usuario.cpf}", json=usuario.to_dict())
    assert response.status_code == 400
    assert response.json() == {"error": "EmailInvalido", "mensagem": "O Email informado não é válido."}

    # EmailEmUso: O Email escolhido já está cadastrado em outro usuário.
    usuario.email = "usuario1@teste.com"

    response = client.patch(f"usuario/{usuario.cpf}", json=usuario.to_dict())
    assert response.status_code == 400
    assert response.json() == {"error": "EmailEmUso", "mensagem": "O Email escolhido já está cadastrado em outro usuário."}

    # UsuarioNaoEncontrado: Usuário não foi encontrado para a alteração.
    usuario.email = "usuario@teste.com"

    response = client.patch("usuario/12345678900", json=usuario.to_dict())
    assert response.status_code == 404
    assert response.json() == {"error": "UsuarioNaoEncontrado", "mensagem": "Usuário não foi encontrado para a alteração."}

def test_usuario_api_remover_exceptions(
    client
):
    # UsuarioNaoEncontrado: Usuário não foi encontrado para a remoção.
    response = client.delete("usuario/12345678900")
    assert response.status_code == 404
    assert response.json() == {"error": "UsuarioNaoEncontrado", "mensagem": "O cpf informado não foi encontrado na base de dados."}
