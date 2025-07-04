import pytest
from datetime import datetime, timedelta
from tests.mock import *

def test_criar_agendamento_api(
    client,
    mock_criar_usuario,
    mock_criar_servicos,
    mock_criar_jornada_de_trabalho
):
    base_time = datetime.now() + timedelta(days=1)
    h_inicio = base_time.replace(hour=10, minute=0, second=0, microsecond=0)
    h_fim = base_time.replace(hour=11, minute=30, second=0, microsecond=0)
    mock_criar_servicos({"id0": "servico-001", "id1": "servico-002", "id2": "servico-003"})

    payload = {
        "horario_inicio": h_inicio.strftime("%Y-%m-%dT%H:%M:%S"),
        "horario_fim": h_fim.strftime("%Y-%m-%dT%H:%M:%S"),
        "barbeiro_cpf": "25811756054",
        "cliente_cpf": "05705608020",
        "servicos_id": ["servico-001"]
    }

    # Criação bem-sucedida
    response = client.post("/agendamento/criar", json=payload)
    print("Erro:", response.json())
    assert response.status_code == 201
    assert response.json() == {"mensagem": "Agendamento criado com sucesso!"}

    # Tentativa de conflito no mesmo horário
    response = client.post("/agendamento/criar", json=payload)
    assert response.status_code == 400
    assert "erro" in response.json()
