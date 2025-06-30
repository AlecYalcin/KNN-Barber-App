from tests.mock import mock_usuario_teste, mock_criar_usuario, criar_usuario, usuario_base

def test_usuario_criar_api(    
    client,
    usuario_base,
    criar_usuario,
):
    # Usuário já existente
    usuario_existente = criar_usuario()

    # CPFInvalido: O CPF informado não é válido.
    response = client.post("usuario/criar", json={
        "cpf":"1234567890",
        "nome":"_",
        "email":"_",
        "senha":"_",
        "telefone":"_",
    })

    assert response.status_code == 400
    assert response.json() == {"error": "CPFInvalido", "mensagem": "O CPF informado não é válido."}

    # EmailInvalido: O Email informado não é válido.
    response = client.post("usuario/criar", json={
        "cpf":"70056454481",
        "nome":"_",
        "email":"email-invalido",
        "senha":"_",
        "telefone":"_",
    })

    assert response.status_code == 400
    assert response.json() == {"error": "EmailInvalido", "mensagem": "O Email informado não é válido."}
    
    # CPFEmUso: O CPF já está cadastrado.
    response = client.post("usuario/criar", json={
        "cpf":usuario_existente.cpf,
        "nome":"_",
        "email":"usuario@teste.com.br",
        "senha":"_",
        "telefone":"_",
    })

    assert response.status_code == 400
    assert response.json() == {"error": "CPFEmUso", "mensagem": "O CPF já está cadastrado."}

    # EmailEmUso: O Email já está cadastrado.
    response = client.post("usuario/criar", json={
        "cpf":"70056454481",
        "nome":"_",
        "email":usuario_existente.email,
        "senha":"_",
        "telefone":"_",
    })

    assert response.status_code == 400
    assert response.json() == {"error": "EmailEmUso", "mensagem": "O Email já está cadastrado."}
    
    # Criar Usuário com Sucesso!
    response = client.post("usuario/criar",json={
        "cpf":"70056454481",
        "nome":"Alec Yalçin",
        "email":"alecyalcin@teste.com",
        "senha":"senhaForte123",
        "telefone":"84987626875",
    })

    assert response.status_code == 201
    assert response.json() == {"mensagem":"Sucesso ao criar usuário!"}

def test_usuario_recuperar_api(
    client,
    mock_criar_usuario,
):
    # Consultar Usuário Inexistente
    response = client.get("usuario/70056454481")

    assert response.status_code == 200
    assert response.json() == {}

    # Consultar Usuário Existente
    response = client.get("usuario/05705608020")

    assert response.status_code == 200
    assert response.json() == {
        "cpf":"05705608020",
        "nome":"Usuário 01",
        "email":"usuario1@teste.com",
        "senha":"123",
        "telefone":None,
        "eh_barbeiro":False,
    }

def test_usuario_alterar_api(
    client,
    criar_usuario,
):
    usuario = criar_usuario()
    
    # EmailInvalido: O Email informado não é válido.

    usuario.email = "email_invalido"

    response = client.patch(f"usuario/{usuario.cpf}", json=usuario.to_dict())
    assert response.status_code == 400
    assert response.json() == {"error": "EmailInvalido", "mensagem": "O Email informado não é válido."}

    # EmailEmUso: O Email escolhido já está cadastrado em outro usuário.

    usuario_2 = criar_usuario(cpf="70056454481",email="usuario1@teste.com")
    usuario.email = "usuario1@teste.com"

    response = client.patch(f"usuario/{usuario.cpf}", json=usuario.to_dict())
    assert response.status_code == 400
    assert response.json() == {"error": "EmailEmUso", "mensagem": "O Email escolhido já está cadastrado em outro usuário."}

    # UsuarioNaoEncontrado: Usuário não foi encontrado para a alteração.

    usuario.email = "usuario@teste.com"

    response = client.patch("usuario/12345678900", json=usuario.to_dict())
    assert response.status_code == 404
    assert response.json() == {"error": "UsuarioNaoEncontrado", "mensagem": "Usuário não foi encontrado para a alteração."}

    # Alterar Usuário com sucesso!
    response = client.patch(f"usuario/{usuario.cpf}", json={
        "nome":"Alec Yalçin",
        "email":"alecyalcin@teste.com",
        "senha":"senhaForte123",
        "telefone":"84987626875",
        "eh_barbeiro":False,
    })

    assert response.status_code == 200
    assert response.json() == {"mensagem":"Usuário atualizado com sucesso!"}

    response = client.get("usuario/92470179041")
    assert response.json() == {
        "cpf":"92470179041",
        "nome":"Alec Yalçin",
        "email":"alecyalcin@teste.com",
        "senha":"senhaForte123",
        "telefone":"84987626875",
        "eh_barbeiro":False,
    }


def test_usuario_deletar_api(
    client,
    mock_criar_usuario,
):
    # UsuarioNaoEncontrado: Usuário não foi encontrado para a remoção.
    response = client.delete("usuario/12345678900")
    assert response.status_code == 404
    assert response.json() == {"error": "UsuarioNaoEncontrado", "mensagem": "O cpf informado não foi encontrado na base de dados."}

    # Remover Usuário com Sucesso
    response = client.delete("usuario/05705608020")

    assert response.status_code == 200
    assert response.json() == {"mensagem":"O usuário foi excluído do sistema!"}

    response = client.get("usuario/05705608020")
    assert response.json() == {}