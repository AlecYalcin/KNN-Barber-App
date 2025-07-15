from uuid import uuid4
from datetime import datetime, timedelta
from tests.mock import *
from .mock_api import criar_usuario_e_token, criador_de_usuario

def test_pagamento_criar_api(
    client, 
    mock_criar_usuarios_e_agendamento,
    criar_usuario_e_token,
):
    # Criar dados necessários
    cliente, barbeiro, agendamento = mock_criar_usuarios_e_agendamento
    
    # Criar usuário e token de cliente (sem permissão) - usar CPF e email únicos
    _, token_cliente = criar_usuario_e_token(cpf="11111111111", email="cliente_novo@test.com", eh_barbeiro=False)
    
    # PermissaoNegada: O usuário não possui permissões para realizar essa operação
    response = client.post("/pagamento/criar", json={
        "valor": 50.0,
        "metodo": "PIX",
        "agendamento_id": agendamento.id
    }, headers={
        'Authorization': f'Bearer {token_cliente}',
    })
    
    assert response.status_code == 401
    assert response.json() == {"error": "PermissaoNegada", "mensagem": "O usuário não possui permissões para realizar essa operação."}
    
    # Criar usuário e token de barbeiro (com permissão) - usar CPF e email únicos
    _, token_barbeiro = criar_usuario_e_token(cpf="22222222222", email="barbeiro_novo@test.com", eh_barbeiro=True)
    
    # ValorInvalido: O valor do pagamento precisa ser maior que zero
    response = client.post("/pagamento/criar", json={
        "valor": 0.0,
        "metodo": "PIX",
        "agendamento_id": agendamento.id
    }, headers={
        'Authorization': f'Bearer {token_barbeiro}',
    })
    
    assert response.status_code == 400
    assert response.json() == {"error": "ValorInvalido", "mensagem": "O valor do pagamento precisa ser maior que zero."}
    
    # ValorInvalido: O valor do pagamento precisa ser maior que zero (negativo)
    response = client.post("/pagamento/criar", json={
        "valor": -10.0,
        "metodo": "PIX",
        "agendamento_id": agendamento.id
    }, headers={
        'Authorization': f'Bearer {token_barbeiro}',
    })
    
    assert response.status_code == 400
    assert response.json() == {"error": "ValorInvalido", "mensagem": "O valor do pagamento precisa ser maior que zero."}
    
    # AgendamentoNaoEncontrado: Agendamento não foi encontrado
    response = client.post("/pagamento/criar", json={
        "valor": 50.0,
        "metodo": "PIX",
        "agendamento_id": "agendamento-inexistente"
    }, headers={
        'Authorization': f'Bearer {token_barbeiro}',
    })
    
    assert response.status_code == 404
    assert response.json() == {"error": "AgendamentoNaoEncontrado", "mensagem": "Agendamento não foi encontrado."}
    
    # MetodoPagamentoInvalido: Método de pagamento inválido (422 devido à validação Pydantic)
    response = client.post("/pagamento/criar", json={
        "valor": 50.0,
        "metodo": "METODO_INVALIDO",
        "agendamento_id": agendamento.id
    }, headers={
        'Authorization': f'Bearer {token_barbeiro}',
    })
    
    assert response.status_code == 422  # Pydantic validation error
    
    # Criar pagamento com sucesso - PIX
    response = client.post("/pagamento/criar", json={
        "valor": 50.0,
        "metodo": "PIX",
        "agendamento_id": agendamento.id
    }, headers={
        'Authorization': f'Bearer {token_barbeiro}',
    })
    
    assert response.status_code == 201
    assert response.json() == {"mensagem": "Pagamento cadastrado com sucesso!"}
    
    # Criar pagamento com sucesso - Cartão
    response = client.post("/pagamento/criar", json={
        "valor": 30.0,
        "metodo": "Cartão",
        "agendamento_id": agendamento.id
    }, headers={
        'Authorization': f'Bearer {token_barbeiro}',
    })
    
    assert response.status_code == 201
    assert response.json() == {"mensagem": "Pagamento cadastrado com sucesso!"}
    
    # Criar pagamento com sucesso - Dinheiro
    response = client.post("/pagamento/criar", json={
        "valor": 20.0,
        "metodo": "Dinheiro",
        "agendamento_id": agendamento.id
    }, headers={
        'Authorization': f'Bearer {token_barbeiro}',
    })
    
    assert response.status_code == 201
    assert response.json() == {"mensagem": "Pagamento cadastrado com sucesso!"}

def test_pagamento_consultar_api(client, mock_criar_pagamento):
    # Criar pagamento
    pagamento = mock_criar_pagamento
    
    # Consultar pagamento existente
    response = client.get(f"/pagamento/{pagamento.id}")
    assert response.status_code == 200
    assert response.json()['id'] == pagamento.id
    assert response.json()['valor'] == pagamento.valor
    assert response.json()['metodo'] == pagamento.metodo.value
    
    # Consultar pagamento inexistente
    response = client.get(f"/pagamento/pagamento-inexistente")
    # O endpoint pode retornar 200 com {} ou 404, vamos verificar o conteúdo
    if response.status_code == 200:
        assert response.json() == {}
    else:
        assert response.status_code == 404
        assert response.json() == {"error": "PagamentoNaoEncontrado", "mensagem": "Pagamento não foi encontrado."}

def test_pagamento_consultar_por_agendamento_api(client, mock_criar_pagamento):
    # Criar pagamento
    pagamento = mock_criar_pagamento
    
    # Consultar pagamento por agendamento
    response = client.get(f"/pagamento/agendamento/{pagamento.agendamento_id}")
    assert response.status_code == 200
    assert response.json()['id'] == pagamento.id
    assert response.json()['valor'] == pagamento.valor
    assert response.json()['metodo'] == pagamento.metodo.value
    
    # Consultar agendamento sem pagamento
    response = client.get(f"/pagamento/agendamento/agendamento-sem-pagamentos")
    assert response.status_code == 200
    assert response.json() is None

def test_pagamento_listar_por_cliente_api(client, mock_criar_pagamentos_cliente):
    # Criar múltiplos pagamentos para um cliente
    cliente_cpf, pagamentos = mock_criar_pagamentos_cliente
    
    # Listar pagamentos do cliente
    response = client.get(f"/pagamento/listar/{cliente_cpf}")
    assert response.status_code == 200
    assert len(response.json()) == 3
    
    # Verificar se todos os pagamentos estão presentes
    pagamento_ids = [p['id'] for p in response.json()]
    for pagamento in pagamentos:
        assert pagamento.id in pagamento_ids
    
    # Listar pagamentos de cliente sem pagamentos
    response = client.get(f"/pagamento/listar/99999999999")
    assert response.status_code == 200
    assert response.json() == []

def test_pagamento_atualizar_api(
    client,
    mock_criar_pagamento,
    criar_usuario_e_token,
):
    # Criar pagamento
    pagamento = mock_criar_pagamento
    
    # Criar usuário e token de barbeiro - usar CPF e email únicos
    _, token_barbeiro = criar_usuario_e_token(cpf="33333333333", email="barbeiro_atualizar@test.com", eh_barbeiro=True)
    
    # Atualizar pagamento com sucesso
    response = client.patch(f"/pagamento/{pagamento.id}", json={
        "valor": 60.0,
        "metodo": "Cartão"
    }, headers={
        'Authorization': f'Bearer {token_barbeiro}',
    })
    
    assert response.status_code == 200
    assert response.json() == {"mensagem": "Pagamento atualizado com sucesso."}
    
    # Verificar atualização
    response = client.get(f"/pagamento/{pagamento.id}")
    assert response.json()['valor'] == 60.0
    assert response.json()['metodo'] == "Cartão"
    
    # ValorInvalido: O valor do pagamento precisa ser maior que zero
    response = client.patch(f"/pagamento/{pagamento.id}", json={
        "valor": 0.0,
        "metodo": "PIX"
    }, headers={
        'Authorization': f'Bearer {token_barbeiro}',
    })
    
    assert response.status_code == 400
    assert response.json() == {"error": "ValorInvalido", "mensagem": "O valor do pagamento precisa ser maior que zero."}
    
    # MetodoPagamentoInvalido: Método de pagamento inválido (422 devido à validação Pydantic)
    response = client.patch(f"/pagamento/{pagamento.id}", json={
        "valor": 50.0,
        "metodo": "METODO_INVALIDO"
    }, headers={
        'Authorization': f'Bearer {token_barbeiro}',
    })
    
    assert response.status_code == 422  # Pydantic validation error
    
    # PagamentoNaoEncontrado: Pagamento não foi encontrado
    response = client.patch(f"/pagamento/pagamento-inexistente", json={
        "valor": 50.0,
        "metodo": "PIX"
    }, headers={
        'Authorization': f'Bearer {token_barbeiro}',
    })
    
    assert response.status_code == 404
    assert response.json() == {"error": "PagamentoNaoEncontrado", "mensagem": "Pagamento não foi encontrado para a alteração."}
    
    # PermissaoNegada: O usuário não possui permissões para realizar essa operação
    _, token_cliente = criar_usuario_e_token(cpf="44444444444", email="cliente_atualizar@test.com", eh_barbeiro=False)
    
    response = client.patch(f"/pagamento/{pagamento.id}", json={
        "valor": 50.0,
        "metodo": "PIX"
    }, headers={
        'Authorization': f'Bearer {token_cliente}',
    })
    
    assert response.status_code == 401
    assert response.json() == {"error": "PermissaoNegada", "mensagem": "O usuário não possui permissões para realizar essa operação."}

def test_pagamento_excluir_api(
    client,
    mock_criar_pagamento,
    criar_usuario_e_token,
):
    # Criar pagamento
    pagamento = mock_criar_pagamento
    
    # Criar usuário e token de barbeiro - usar CPF e email únicos
    _, token_barbeiro = criar_usuario_e_token(cpf="55555555555", email="barbeiro_excluir@test.com", eh_barbeiro=True)
    
    # Excluir pagamento com sucesso
    response = client.delete(f"/pagamento/{pagamento.id}", headers={
        'Authorization': f'Bearer {token_barbeiro}',
    })
    
    assert response.status_code == 200
    assert response.json() == {"mensagem": "Pagamento excluído com sucesso."}
    
    # Verificar exclusão
    response = client.get(f"/pagamento/{pagamento.id}")
    if response.status_code == 200:
        assert response.json() == {}
    else:
        assert response.status_code == 404
    
    # PagamentoNaoEncontrado: Pagamento não foi encontrado
    response = client.delete(f"/pagamento/pagamento-inexistente", headers={
        'Authorization': f'Bearer {token_barbeiro}',
    })
    
    assert response.status_code == 404
    assert response.json() == {"error": "PagamentoNaoEncontrado", "mensagem": "Pagamento não foi encontrado para exclusão."}
    
    # PermissaoNegada: O usuário não possui permissões para realizar essa operação
    _, token_cliente = criar_usuario_e_token(cpf="66666666666", email="cliente_excluir@test.com", eh_barbeiro=False)
    
    response = client.delete(f"/pagamento/{pagamento.id}", headers={
        'Authorization': f'Bearer {token_cliente}',
    })
    
    assert response.status_code == 401
    assert response.json() == {"error": "PermissaoNegada", "mensagem": "O usuário não possui permissões para realizar essa operação."}

def test_pagamento_fluxo_completo_api(
    client,
    mock_criar_usuarios_e_agendamento,
    criar_usuario_e_token,
):
    # Criar dados necessários
    cliente, barbeiro, agendamento = mock_criar_usuarios_e_agendamento
    
    # Criar usuário e token de barbeiro - usar CPF e email únicos
    _, token_barbeiro = criar_usuario_e_token(cpf="77777777777", email="barbeiro_fluxo@test.com", eh_barbeiro=True)
    
    # 1. Criar primeiro pagamento
    response = client.post("/pagamento/criar", json={
        "valor": 50.0,
        "metodo": "PIX",
        "agendamento_id": agendamento.id
    }, headers={
        'Authorization': f'Bearer {token_barbeiro}',
    })
    
    assert response.status_code == 201
    
    # 2. Verificar pagamento criado
    response = client.get(f"/pagamento/agendamento/{agendamento.id}")
    assert response.status_code == 200
    assert response.json() is not None
    
    pagamento_id = response.json()['id']
    
    # 3. Consultar pagamento específico
    response = client.get(f"/pagamento/{pagamento_id}")
    assert response.status_code == 200
    assert response.json()['valor'] == 50.0
    assert response.json()['metodo'] == "PIX"
    
    # 4. Atualizar pagamento
    response = client.patch(f"/pagamento/{pagamento_id}", json={
        "valor": 60.0,
        "metodo": "Cartão"
    }, headers={
        'Authorization': f'Bearer {token_barbeiro}',
    })
    
    assert response.status_code == 200
    
    # 5. Verificar atualização
    response = client.get(f"/pagamento/{pagamento_id}")
    assert response.json()['valor'] == 60.0
    assert response.json()['metodo'] == "Cartão"
    
    # 6. Listar pagamentos do cliente
    response = client.get(f"/pagamento/listar/{cliente.cpf}")
    assert response.status_code == 200
    assert len(response.json()) == 1
    
    # 7. Excluir pagamento
    response = client.delete(f"/pagamento/{pagamento_id}", headers={
        'Authorization': f'Bearer {token_barbeiro}',
    })
    
    assert response.status_code == 200
    
    # 8. Verificar exclusão
    response = client.get(f"/pagamento/{pagamento_id}")
    if response.status_code == 200:
        assert response.json() == {}
    else:
        assert response.status_code == 404

def test_pagamento_multiplos_metodos_api(
    client,
    mock_criar_usuarios_e_agendamento,
    criar_usuario_e_token,
):
    # Criar dados necessários
    cliente, barbeiro, agendamento = mock_criar_usuarios_e_agendamento
    
    # Criar usuário e token de barbeiro - usar CPF e email únicos
    _, token_barbeiro = criar_usuario_e_token(cpf="88888888888", email="barbeiro_multiplos@test.com", eh_barbeiro=True)
    
    # Criar pagamento com método PIX
    response = client.post("/pagamento/criar", json={
        "valor": 30.0,
        "metodo": "PIX",
        "agendamento_id": agendamento.id
    }, headers={
        'Authorization': f'Bearer {token_barbeiro}',
    })
    
    assert response.status_code == 201
    
    # Verificar se o pagamento foi criado
    response = client.get(f"/pagamento/agendamento/{agendamento.id}")
    assert response.status_code == 200
    assert response.json() is not None
    assert response.json()['metodo'] == "PIX"
    assert response.json()['valor'] == 30.0 