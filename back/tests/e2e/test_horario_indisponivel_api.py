from tests.mock import mock_criar_horarios_indisponiveis, mock_criar_barbeiro
from datetime import datetime

def test_criando_horario_indisponivel_api(
    client,
    session_maker,
    mock_criar_barbeiro,
):
    # HorarioIndisponivelInvalido: O horário de inicio tem que ser menor que o horário de fim.
    response = client.post('/horario-indisponivel/criar', json={
        "barbeiro_cpf":"25811756054",
        "horario_inicio":datetime(2025, 7, 10, 6).isoformat(),
        "horario_fim":datetime(2025, 6, 10, 6).isoformat(),
        "justificativa":"Viagem as Bahamas",
    })
    assert response.status_code == 400
    assert response.json() == {"error":"HorarioIndisponivelInvalido","mensagem":"O horário de inicio tem que ser menor que o horário de fim."}

    # BarbeiroNaoEncontrado: O cpf informado não pertencem a um barbeiro do sistema.
    response = client.post('/horario-indisponivel/criar', json={
        "barbeiro_cpf":"1234567890",
        "horario_inicio":datetime(2025, 5, 10, 6).isoformat(),
        "horario_fim":datetime(2025, 7, 10, 6).isoformat(),
        "justificativa":"Viagem as Bahamas",
    })
    assert response.status_code == 404
    assert response.json() == {"error":"BarbeiroNaoEncontrado","mensagem":"O cpf informado não pertencem a um barbeiro do sistema."}

    # Criando horário indisponível com sucess    
    response = client.post('/horario-indisponivel/criar', json={
        "barbeiro_cpf":"25811756054",
        "horario_inicio":datetime(2025, 6, 10, 6).isoformat(),
        "horario_fim":datetime(2025, 7, 10, 6).isoformat(),
        "justificativa":"Viagem as Bahamas",
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
    response = client.get('/horario-indisponivel/pesquisar-horarios')
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
):
    # HorarioIndisponivelInvalido: O horário de inicio tem que ser menor que o horário de fim.
    response = client.patch('/horario-indisponivel/horario-001', json={
        "horario_inicio":datetime(2025, 7, 10, 6).isoformat(),
        "horario_fim":datetime(2025, 6, 10, 6).isoformat(),
        "justificativa":"Horário Inválido",
    })
    assert response.status_code == 400
    assert response.json() == {"error":"HorarioIndisponivelInvalido","mensagem":"O horário de inicio tem que ser menor que o horário de fim."}

    # HorarioIndisponivelNaoEncontrado: O horario indisponivel especificado não foi encontrado.
    response = client.patch('/horario-indisponivel/horario-999', json={
        "horario_inicio":datetime(2025, 6, 10, 6).isoformat(),
        "horario_fim":datetime(2025, 7, 10, 6).isoformat(),
        "justificativa":"Horário não Encontrado",
    })
    assert response.status_code == 404
    assert response.json() == {"error":"HorarioIndisponivelNaoEncontrado","mensagem":"O horario indisponivel especificado não foi encontrado."}

    # Editando horário indisponível com sucesso    
    response = client.patch('/horario-indisponivel/horario-001', json={
        "horario_inicio":datetime(2025, 6, 20, 6).isoformat(),
        "horario_fim":datetime(2025, 7, 21, 6).isoformat(),
        "justificativa":"Viagem ao centro da terra",
    })
    assert response.status_code == 200
    assert response.json() == {"mensagem":"Horário indisponível alterado com sucesso!"}

def test_excluindo_horario_indisponivel_api(
    client,
    mock_criar_horarios_indisponiveis,
):
    # HorarioIndisponivelNaoEncontrado: "O horario indisponivel especificado não foi encontrado."
    response = client.delete('/horario-indisponivel/horario-999')
    assert response.status_code == 404
    assert response.json() == {
        "error":"HorarioIndisponivelNaoEncontrado",
        "mensagem":"O horario indisponivel especificado não foi encontrado."
    }

    # Excluindo horário indisponível com sucesso
    response = client.delete('/horario-indisponivel/horario-001')
    assert response.status_code == 200
    assert response.json() == {"mensagem":"Horário indisponível excluído com sucesso!"}