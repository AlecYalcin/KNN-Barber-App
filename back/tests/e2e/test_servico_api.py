from uuid import uuid4
from tests.mock import mock_servicos_teste, mock_criar_servicos
from .mock_api import criar_usuario_e_token, criador_de_usuario

def test_servico_criar_api(
    client, 
    mock_servicos_teste,
    criar_usuario_e_token,
):
    servicos = mock_servicos_teste

    # Criando usuário e token
    _, token = criar_usuario_e_token(cpf="qualquer-cpf", email="qualquer-email")

    # PermissaoNegada: O usuário não possui permissões para realizar essa operação.
    for servico in servicos:
        response = client.post("/servico/criar", json=servico.to_dict(), headers={
            'Authorization': f'Bearer {token}',
        })

        assert response.status_code == 401
        assert response.json() == {"error":"PermissaoNegada","mensagem":"O usuário não possui permissões para realizar essa operação."}

    # Criando usuário e token de barbeiros
    _, token = criar_usuario_e_token(eh_barbeiro=True)

    # Criar Serviço com Sucesso
    for servico in servicos:
        response = client.post("/servico/criar", json=servico.to_dict(), headers={
            'Authorization': f'Bearer {token}',
        })

        assert response.status_code == 201
        assert response.json() == {"mensagem":"Serviço cadastrado com sucesso!"}

    # DuracaoInvalida: A duração do serviço não está entre 5min ou 120min
    response = client.post("/servico/criar", json={
        "nome":"Serviço Qualquer",
        "descricao":"Serviço Qualquer",
        "preco":16,
        "duracao":-16,
    }, 
    headers={
        'Authorization': f'Bearer {token}',
    })

    assert response.status_code == 400
    assert response.json() == {"error": "DuracaoInvalida", "mensagem": "A duração do serviço não está entre 5min ou 120min"}

    # PrecoInvalido: O preço do serviço precisa ser maior que zero.
    response = client.post("/servico/criar", json={
        "nome":"Serviço Qualquer",
        "descricao":"Serviço Qualquer",
        "preco":-16,
        "duracao":16,
    }, 
    headers={
        'Authorization': f'Bearer {token}',
    })

    assert response.status_code == 400
    assert response.json() == {"error": "PrecoInvalido", "mensagem": "O preço do serviço precisa ser maior que zero."}

def test_servico_consultar_api(client, mock_criar_servicos):
    servicos_id = {
        "id0":str(uuid4()),
        "id1":str(uuid4()),
        "id2":str(uuid4()),
    }

    # Criando serviços com ids específicos
    mock_criar_servicos(servicos_id)

    # Consultando serviço existente
    for id in servicos_id.values():
        response = client.get(f"/servico/{id}")
        assert response.status_code == 200
        assert response.json()['id'] == id

    # Consultando serviço inexistente
    response = client.get(f"/servico/identificador_inexistnete")
    assert response.status_code == 200
    assert response.json() == {}

def test_servico_listar_api(client, mock_criar_servicos):
    servicos_id = {
        "id0":str(uuid4()),
        "id1":str(uuid4()),
        "id2":str(uuid4()),
    }

    # Criando serviços com ids específicos
    mock_criar_servicos(servicos_id)

    # Consultando a lista de serviços existentes
    response = client.get(f"/servico/listar")
    assert response.status_code == 200
    assert len(response.json()) == 3

    rjson = response.json()
    for servico in rjson:
        assert servico['id'] in list(servicos_id.values())

    # Consultando a lista de serviços existentes com query params
    response = client.get(f"servico/listar?nome=Serviço 01")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]['id'] == servicos_id['id0']

    # Consultando lista de serviços inexistentes
    response = client.get(f"servico/listar?nome=nao_existe")
    assert response.status_code == 200
    assert response.json() == []

def test_servico_alterar_api(
    client, 
    mock_criar_servicos,
    criar_usuario_e_token,
):
    servicos_id = {
        "id0":str(uuid4()),
        "id1":str(uuid4()),
        "id2":str(uuid4()),
    }

    # Criando serviços com ids específicos
    mock_criar_servicos(servicos_id)

    # Criando usuário e token
    _, token = criar_usuario_e_token(cpf="qualquer-cpf", email="qualquer-email")

    # PermissaoNegada: O usuário não possui permissões para realizar essa operação.
    response = client.patch(f"servico/{servicos_id['id0']}", json={
        "duracao":-16,
    }, headers={
        'Authorization': f'Bearer {token}',
    })

    assert response.status_code == 401
    assert response.json() == {"error":"PermissaoNegada","mensagem":"O usuário não possui permissões para realizar essa operação."}

    # Criando usuário e token de barbeiros
    _, token = criar_usuario_e_token(eh_barbeiro=True)

    # DuracaoInvalida: A duração do serviço não está entre 5min ou 120min
    response = client.patch(f"servico/{servicos_id['id0']}", json={
        "duracao":-16,
    }, headers={
        'Authorization': f'Bearer {token}',
    })

    assert response.status_code == 400
    assert response.json() == {"error": "DuracaoInvalida", "mensagem": "A duração do serviço não está entre 5min ou 120min"}

    # PrecoInvalido: O preço do serviço precisa ser maior que zero.
    response = client.patch(f"servico/{servicos_id['id0']}", json={
        "preco":-16,
    }, headers={
        'Authorization': f'Bearer {token}',
    })
    
    assert response.status_code == 400
    assert response.json() == {"error": "PrecoInvalido", "mensagem": "O preço do serviço precisa ser maior que zero."}

    # ServicoNaoEncontrado: Serviço não foi encontrado para a alteração
    response = client.patch("servico/1234567890asdfghjkl", json={
        "nome":"Serviço Inválido",
        "descricao":"Serviço Incompleto",
        "preco":30,
        "duracao":15,
    }, headers={
        'Authorization': f'Bearer {token}',
    })
    
    assert response.status_code == 404
    assert response.json() == {"error":"ServicoNaoEncontrado","mensagem":"Serviço não foi encontrado para a alteração."}

    # Alterando serviço com sucesso
    response = client.patch(f"servico/{servicos_id['id0']}", json={
        "nome":"Corte de Cabelo",
        "descricao":"Corte Simples",
        "preco": 15,
        "duracao": 45,        
    }, headers={
        'Authorization': f'Bearer {token}',
    })
    
    assert response.status_code == 200
    assert response.json() == {"mensagem":"Serviço atualizado com sucesso."}

def test_servico_excluir_api(
    client, 
    mock_criar_servicos,
    criar_usuario_e_token,
):
    servicos_id = {
        "id0":str(uuid4()),
        "id1":str(uuid4()),
        "id2":str(uuid4()),
    }

    # Criando serviços com ids específicos
    mock_criar_servicos(servicos_id)

    # Criando usuário e token
    _, token = criar_usuario_e_token(cpf="qualquer-cpf", email="qualquer-email")

    # PermissaoNegada: O usuário não possui permissões para realizar essa operação.
    response = client.delete(f"servico/1234567890asdfghjklç", headers={
        'Authorization': f'Bearer {token}',
    })

    assert response.status_code == 401
    assert response.json() == {"error":"PermissaoNegada","mensagem":"O usuário não possui permissões para realizar essa operação."}

    # Criando usuário e token de barbeiros
    _, token = criar_usuario_e_token(eh_barbeiro=True)

    # ServicoNaoEncontrado: Serviço não foi encontrado para exclusão.
    response = client.delete(f"servico/1234567890asdfghjklç", headers={
        'Authorization': f'Bearer {token}',
    })
    
    assert response.status_code == 404
    assert response.json() == {"error":"ServicoNaoEncontrado","mensagem":"Serviço não foi encontrado para exclusão."}

    # Serviço Excluído com sucesso
    response = client.delete(f"servico/{servicos_id['id0']}", headers={
        'Authorization': f'Bearer {token}',
    })
    
    assert response.status_code == 200
    assert response.json() == {"mensagem":"Serviço excluído com sucesso."}

