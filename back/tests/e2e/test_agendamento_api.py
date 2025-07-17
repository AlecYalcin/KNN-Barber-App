from datetime import datetime, timedelta

import pytest
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
    assert response.status_code == 201
    assert response.json() == {"mensagem": "Agendamento criado com sucesso!"}

    # Tentativa de conflito no mesmo horário
    response = client.post("/agendamento/criar", json=payload)
    assert response.status_code == 400
    assert response.json() == {'error': 'HorarioIndisponivelParaBarbeiro', 'mensagem': 'O horário selecionado encontra-se indisponível para o barbeiro.'}


def test_listar_e_consultar_agendamento_api(
    client,
    mock_criar_agendamento
):
    # Arrange
    ids = mock_criar_agendamento
    agendamento_id = ids["id_agendamento"]
    servicos_ids = ids["servicos"]
    # Certifique-se de que o mock está criando o agendamento com o cliente_cpf correto
    # Se necessário, ajuste o mock_criar_agendamento para definir cliente_cpf="05705608020"

    # Act - Listar todos os agendamentos
    response_listar = client.get("/agendamento/listar")
    assert response_listar.status_code == 200
    agendamentos = response_listar.json()

    # Verifica se o agendamento recém-criado está na lista
    agendamento = next((a for a in agendamentos if a.get("id") == agendamento_id), None)
    assert agendamento is not None, f"Agendamento com id {agendamento_id} não encontrado. Lista: {agendamentos}"
    assert agendamento['cliente'].get("cpf") == "05705608020", f"Esperado cliente_cpf '05705608020', mas veio: {agendamento['cliente'].get('cpf')}"
    assert agendamento['barbeiro'].get("cpf") == "25811756054", f"Esperado barbeiro_cpf '25811756054', mas veio: {agendamento['barbeiro'].get('cpf')}"
    
    assert isinstance(agendamento.get('servicos'), list) and len(agendamento.get('servicos', [])) > 0, "Serviços não encontrados no agendamento"

    servico = next((s for s in agendamento.get("servicos", []) if s.get("id") in servicos_ids), None)
    assert servico is not None, f"Serviço com id {servicos_ids} não encontrado no agendamento. Serviços: {agendamento.get('servicos', [])}"

    # Act - Consultar agendamento específico por ID
    response_consultar = client.get(f"/agendamento/{agendamento_id}")
    assert response_consultar.status_code == 200
    agendamento = response_consultar.json()

    # Assert - Verificar os campos esperados
    assert agendamento["id"] == agendamento_id
    assert agendamento["cliente"].get("cpf") == "05705608020"
    assert agendamento["barbeiro"].get("cpf") == "25811756054"
    

def test_remover_agendamento_api(
    client,
    mock_criar_agendamento
):
    # Arrange: cria agendamento mockado
    ids = mock_criar_agendamento
    agendamento_id = ids["id_agendamento"]

    # Verifica que o agendamento existe antes da exclusão
    response_get = client.get(f"/agendamento/{agendamento_id}")
    assert response_get.status_code == 200
    assert response_get.json().get("id") == agendamento_id

    # Act: remove o agendamento
    response_delete = client.delete(f"/agendamento/{agendamento_id}")
    assert response_delete.status_code == 200
    assert response_delete.json() == {"mensagem": "Agendamento removido com sucesso!"}
