from tests.mock import mock_criar_horarios_indisponiveis, mock_criar_barbeiro
from .mock_api import criar_usuario_e_token, criador_de_usuario, retrieve_token
from datetime import datetime

def test_criando_horario_indisponivel_api(
    client,
    criador_de_usuario,
    criar_usuario_e_token,
):
    # Criando usuário e token
    _, token = criar_usuario_e_token(cpf="qualquer-cpf", email="qualquer-email")

    # PermissaoNegada: O usuário não possui permissões para realizar essa operação.
    response = client.post('/horario-indisponivel/criar', json={
        "barbeiro_cpf":"25811756054",
        "horario_inicio":datetime(2025, 7, 10, 6).isoformat(),
        "horario_fim":datetime(2025, 6, 10, 6).isoformat(),
        "justificativa":"Viagem as Bahamas",
    }, headers={
        'Authorization': f'Bearer {token}',
    })

    assert response.status_code == 401
    assert response.json() == {"error":"PermissaoNegada","mensagem":"O usuário não possui permissões para realizar essa operação."}

    # Criando usuário e token de barbeiros
    usuario, token = criar_usuario_e_token(eh_barbeiro=True)

    # HorarioIndisponivelInvalido: O horário de inicio tem que ser menor que o horário de fim.
    response = client.post('/horario-indisponivel/criar', json={
        "barbeiro_cpf":usuario.cpf,
        "horario_inicio":datetime(2025, 7, 10, 6).isoformat(),
        "horario_fim":datetime(2025, 6, 10, 6).isoformat(),
        "justificativa":"Viagem as Bahamas",
    }, headers={
        'Authorization': f'Bearer {token}',
    })

    assert response.status_code == 400
    assert response.json() == {"error":"HorarioIndisponivelInvalido","mensagem":"O horário de inicio tem que ser menor que o horário de fim."}

    # BarbeiroNaoEncontrado: O cpf informado não pertencem a um barbeiro do sistema.
    response = client.post('/horario-indisponivel/criar', json={
        "barbeiro_cpf":"1234567890",
        "horario_inicio":datetime(2025, 5, 10, 6).isoformat(),
        "horario_fim":datetime(2025, 7, 10, 6).isoformat(),
        "justificativa":"Viagem as Bahamas",
    }, headers={
        'Authorization': f'Bearer {token}',
    })

    assert response.status_code == 404
    assert response.json() == {"error":"BarbeiroNaoEncontrado","mensagem":"O cpf informado não pertencem a um barbeiro do sistema."}

    # Criando outro barbeiro existente no sistema
    usuario_2 = criador_de_usuario(cpf="55493147033", email="email@diferente.com", eh_barbeiro=True)

    # PermissaoNegada: Não é possível criar a jornada de outro barbeiro.
    response = client.post('/horario-indisponivel/criar', json={
        "barbeiro_cpf":usuario_2.cpf,
        "horario_inicio":datetime(2025, 5, 10, 6).isoformat(),
        "horario_fim":datetime(2025, 7, 10, 6).isoformat(),
        "justificativa":"Viagem as Bahamas",
    }, headers={
        'Authorization': f'Bearer {token}',
    })

    assert response.status_code == 401
    assert response.json() == {"error":"PermissaoNegada","mensagem":"Não é possível criar a jornada de outro barbeiro."}

    # Criando horário indisponível com sucess    
    response = client.post('/horario-indisponivel/criar', json={
        "barbeiro_cpf":usuario.cpf,
        "horario_inicio":datetime(2025, 6, 10, 6).isoformat(),
        "horario_fim":datetime(2025, 7, 10, 6).isoformat(),
        "justificativa":"Viagem as Bahamas",
    }, headers={
        'Authorization': f'Bearer {token}',
    })

    assert response.status_code == 201
    assert response.json() == {"mensagem":"Horário indisponível cadastrado com sucesso!"}

def test_consultando_horario_indisponivel_api(
    client,
    mock_criar_horarios_indisponiveis,
):
    # Consultando horário inexistente
    response = client.get("/horario-indisponivel/horario-999")
    assert response.status_code == 200
    assert response.json() == {}

    # Consultando horário existente
    horario_1 = (datetime(2025, 6, 10), datetime(2025, 6, 11))
    response = client.get("/horario-indisponivel/horario-001")
    assert response.status_code == 200
    assert response.json() == {
        'id':'horario-001',
        'horario_inicio': horario_1[0].isoformat(),
        'horario_fim': horario_1[1].isoformat(),
        'justificativa':'Indisponível hoje',
        'barbeiro':{
            'cpf':'25811756054',
            'nome':'Barbeiro 01',
            'senha':'123',
            'email':'barbeiro1@teste.com',
            'telefone':None,
            'eh_barbeiro':True,
        },
    }

def test_consultando_horario_indisponivel_por_faixa_de_horarios_api(
    client,
    mock_criar_horarios_indisponiveis,
):
    # Consultando horários inexistentes
    response = client.get(
        f'/horario-indisponivel/pesquisar-horarios?horario_inicio={datetime(2024, 1, 1)}&horario_fim={datetime(2023, 1, 1)}')
    assert response.status_code == 200
    assert response.json() == []

    # Consultando horários padrão
    response = client.get(
        f'/horario-indisponivel/pesquisar-horarios?horario_inicio={datetime(2025, 6, 1)}&horario_fim={datetime(2025, 6, 30)}')
    assert response.status_code == 200
    assert len(response.json()) == 1

    # Consultando horários do ano
    response = client.get(
        f'/horario-indisponivel/pesquisar-horarios?horario_inicio={datetime(2025, 1, 1)}&horario_fim={datetime(2025, 12, 31)}'
    )
    assert response.status_code == 200
    assert len(response.json()) == 3

def test_atualizando_horario_indisponivel_api(
    client,
    mock_criar_horarios_indisponiveis,
    criar_usuario_e_token,
    retrieve_token,
):
    # Criando usuário e token
    _, token = criar_usuario_e_token(cpf="qualquer-cpf", email="qualquer-email")

    # PermissaoNegada: O usuário não possui permissões para realizar essa operação.
    response = client.patch('/horario-indisponivel/horario-001', json={
        "horario_inicio":datetime(2025, 7, 10, 6).isoformat(),
        "horario_fim":datetime(2025, 6, 10, 6).isoformat(),
        "justificativa":"Horário Inválido",
    }, headers={
        'Authorization': f'Bearer {token}',
    })

    assert response.status_code == 401
    assert response.json() == {"error":"PermissaoNegada","mensagem":"O usuário não possui permissões para realizar essa operação."}

    # Criando usuário e token de barbeiros
    token = retrieve_token(email="barbeiro1@teste.com", senha="123")

    # HorarioIndisponivelInvalido: O horário de inicio tem que ser menor que o horário de fim.
    response = client.patch('/horario-indisponivel/horario-001', json={
        "horario_inicio":datetime(2025, 7, 10, 6).isoformat(),
        "horario_fim":datetime(2025, 6, 10, 6).isoformat(),
        "justificativa":"Horário Inválido",
    }, headers={
        'Authorization': f'Bearer {token}',
    })

    assert response.status_code == 400
    assert response.json() == {"error":"HorarioIndisponivelInvalido","mensagem":"O horário de inicio tem que ser menor que o horário de fim."}

    # HorarioIndisponivelNaoEncontrado: O horario indisponivel especificado não foi encontrado.
    response = client.patch('/horario-indisponivel/horario-999', json={
        "horario_inicio":datetime(2025, 6, 10, 6).isoformat(),
        "horario_fim":datetime(2025, 7, 10, 6).isoformat(),
        "justificativa":"Horário não Encontrado",
    }, headers={
        'Authorization': f'Bearer {token}',
    })

    assert response.status_code == 404
    assert response.json() == {"error":"HorarioIndisponivelNaoEncontrado","mensagem":"O horario indisponivel especificado não foi encontrado."}

    # Criando outro barbeiro existente no sistema
    _, token2 = criar_usuario_e_token(cpf="55493147033", email="email@diferente.com", eh_barbeiro=True)

    # PermissaoNegada: Não é possível criar a jornada de outro barbeiro.
    response = client.patch('/horario-indisponivel/horario-001', json={
        "horario_inicio":datetime(2025, 6, 20, 6).isoformat(),
        "horario_fim":datetime(2025, 7, 21, 6).isoformat(),
        "justificativa":"Viagem ao centro da terra",
    }, headers={
        'Authorization': f'Bearer {token2}',
    })

    assert response.status_code == 401
    assert response.json() == {"error":"PermissaoNegada","mensagem":"Não é possível alterar a jornada de outro barbeiro."}

    # Editando horário indisponível com sucesso    
    response = client.patch('/horario-indisponivel/horario-001', json={
        "horario_inicio":datetime(2025, 6, 20, 6).isoformat(),
        "horario_fim":datetime(2025, 7, 21, 6).isoformat(),
        "justificativa":"Viagem ao centro da terra",
    }, headers={
        'Authorization': f'Bearer {token}',
    })
    
    assert response.status_code == 200
    assert response.json() == {"mensagem":"Horário indisponível alterado com sucesso!"}

def test_excluindo_horario_indisponivel_api(
    client,
    mock_criar_horarios_indisponiveis,
    criar_usuario_e_token,
    retrieve_token,
):
    # Criando usuário e token
    _, token = criar_usuario_e_token(cpf="qualquer-cpf", email="qualquer-email")

    # PermissaoNegada: O usuário não possui permissões para realizar essa operação.
    response = client.delete('/horario-indisponivel/horario-999', headers={
        'Authorization': f'Bearer {token}',
    })

    assert response.status_code == 401
    assert response.json() == {"error":"PermissaoNegada","mensagem":"O usuário não possui permissões para realizar essa operação."}

    # Criando usuário e token de barbeiros
    token = retrieve_token(email="barbeiro1@teste.com", senha="123")

    # HorarioIndisponivelNaoEncontrado: "O horario indisponivel especificado não foi encontrado."
    response = client.delete('/horario-indisponivel/horario-999', headers={
        'Authorization': f'Bearer {token}',
    })

    assert response.status_code == 404
    assert response.json() == {"error":"HorarioIndisponivelNaoEncontrado","mensagem":"O horario indisponivel especificado não foi encontrado."}

    # Criando outro barbeiro existente no sistema
    _, token2 = criar_usuario_e_token(cpf="55493147033", email="email@diferente.com", eh_barbeiro=True)

    # PermissaoNegada: Não é possível criar a jornada de outro barbeiro.
    response = client.delete('/horario-indisponivel/horario-001', headers={
        'Authorization': f'Bearer {token2}',
    })

    assert response.status_code == 401
    assert response.json() == {"error":"PermissaoNegada","mensagem":"Não é possível excluir a jornada de outro barbeiro."}

    # Excluindo horário indisponível com sucesso
    response = client.delete('/horario-indisponivel/horario-001', headers={
        'Authorization': f'Bearer {token}',
    })

    assert response.status_code == 200
    assert response.json() == {"mensagem":"Horário indisponível excluído com sucesso!"}