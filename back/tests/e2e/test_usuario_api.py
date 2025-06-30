from tests.mock import criador_de_usuario, usuario_base
from .mock_api import retrieve_token

def test_usuario_criar_api(    
    client,
    criador_de_usuario,
):
    # Usuário já existente
    usuario_existente = criador_de_usuario()

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
    criador_de_usuario,
    retrieve_token,
):
    # Criando usuário e token
    usuario = criador_de_usuario(cpf="qualquer-cpf", email="qualquer-email")
    token = retrieve_token(usuario.email, usuario.senha)

    # PermissaoNegada: O usuário não possui permissões para realizar essa operação.
    response = client.get(f"usuario/70056454481", headers={
        'Authorization': f'Bearer {token}',
    })

    assert response.status_code == 401
    assert response.json() == {"error":"PermissaoNegada","mensagem":"O usuário não possui permissões para realizar essa operação."}

    # Criando usuário e token de barbeiros
    usuario = criador_de_usuario(eh_barbeiro=True)
    token = retrieve_token(usuario.email, usuario.senha)

    # Consultar Usuário Inexistente
    response = client.get(f"usuario/70056454481", headers={
        'Authorization': f'Bearer {token}',
    })

    assert response.status_code == 200
    assert response.json() == {}

    # Consultar Usuário Existente
    response = client.get(f"usuario/{usuario.cpf}", headers={
        'Authorization': f'Bearer {token}',
    })

    assert response.status_code == 200
    assert response.json() == usuario.to_dict()

def test_usuario_alterar_api(
    client,
    criador_de_usuario,
    retrieve_token,
):
    usuario = criador_de_usuario(cpf="cpf-qualquer", email="email-qualquer")
    token = retrieve_token(usuario.email, usuario.senha)

    # PermissaoNegada: O usuário não possui permissões para realizar essa operação.

    response = client.patch(f"usuario/70056454481", json=usuario.to_dict(), headers={
        'Authorization': f'Bearer {token}',
    })
    assert response.status_code == 401
    assert response.json() == {"error":"PermissaoNegada","mensagem":"O usuário não possui permissões para realizar essa operação."}

    # Criando usuário e token de barbeiros
    usuario = criador_de_usuario(eh_barbeiro=True)
    token = retrieve_token(usuario.email, usuario.senha)

    # EmailInvalido: O Email informado não é válido.
    usuario.email = "email_invalido"

    response = client.patch(f"usuario/{usuario.cpf}", json=usuario.to_dict(), headers={
        'Authorization': f'Bearer {token}',
    })
    assert response.status_code == 400
    assert response.json() == {"error": "EmailInvalido", "mensagem": "O Email informado não é válido."}

    # EmailEmUso: O Email escolhido já está cadastrado em outro usuário.

    criador_de_usuario(cpf="70056454481",email="usuario1@teste.com")
    usuario.email = "usuario1@teste.com"

    response = client.patch(f"usuario/{usuario.cpf}", json=usuario.to_dict(), headers={
        'Authorization': f'Bearer {token}',
    })
    assert response.status_code == 400
    assert response.json() == {"error": "EmailEmUso", "mensagem": "O Email escolhido já está cadastrado em outro usuário."}

    # UsuarioNaoEncontrado: Usuário não foi encontrado para a alteração.

    usuario.email = "usuario@teste.com"

    response = client.patch("usuario/12345678900", json=usuario.to_dict(), headers={
        'Authorization': f'Bearer {token}',
    })
    assert response.status_code == 404
    assert response.json() == {"error": "UsuarioNaoEncontrado", "mensagem": "Usuário não foi encontrado para a alteração."}

    # Alterar Usuário com sucesso!
    response = client.patch(f"usuario/{usuario.cpf}", json={
        "nome":"Alec Yalçin",
        "email":"alecyalcin@teste.com",
        "senha":"senhaForte123",
        "telefone":"84987626875",
        "eh_barbeiro":False,
    }, headers={
        'Authorization': f'Bearer {token}',
    })

    assert response.status_code == 200
    assert response.json() == {"mensagem":"Usuário atualizado com sucesso!"}

    response = client.get("usuario/92470179041", headers={
        'Authorization': f'Bearer {token}',
    })
    assert response.json() == {
        "cpf":"92470179041",
        "nome":"Alec Yalçin",
        "email":"alecyalcin@teste.com",
        "senha":"senhaForte123",
        "telefone":"84987626875",
        "eh_barbeiro":True,
    }


def test_usuario_deletar_api(
    client,
    criador_de_usuario,
    retrieve_token,
):    
    usuario = criador_de_usuario(cpf="cpf-qualquer", email="email-qualquer")
    token = retrieve_token(usuario.email, usuario.senha)

    # PermissaoNegada: O usuário não possui permissões para realizar essa operação.

    response = client.delete(f"usuario/70056454481", headers={
        'Authorization': f'Bearer {token}',
    })

    assert response.status_code == 401
    assert response.json() == {"error":"PermissaoNegada","mensagem":"O usuário não possui permissões para realizar essa operação."}

    # Criando usuário e token de barbeiros
    usuario = criador_de_usuario(eh_barbeiro=True)
    token = retrieve_token(usuario.email, usuario.senha)

    # UsuarioNaoEncontrado: Usuário não foi encontrado para a remoção.
    response = client.delete("usuario/12345678900", headers={
        'Authorization': f'Bearer {token}',
    })

    assert response.status_code == 404
    assert response.json() == {"error": "UsuarioNaoEncontrado", "mensagem": "O cpf informado não foi encontrado na base de dados."}

    # Remover Usuário com Sucesso
    usuario_2 = criador_de_usuario(cpf="70056454481", email="alec@email.com")

    response = client.delete(f"usuario/{usuario_2.cpf}", headers={
        'Authorization': f'Bearer {token}',
    })

    assert response.status_code == 200
    assert response.json() == {"mensagem":"O usuário foi excluído do sistema!"}

    response = client.get(f"usuario/{usuario_2.cpf}", headers={
        'Authorization': f'Bearer {token}',
    })

    assert response.json() == {}