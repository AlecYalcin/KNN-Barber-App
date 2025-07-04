import pytest
from datetime import datetime, timedelta
from src.service.unit_of_work import UnidadeDeTrabalho
from src.service.services.agendamento import (
    criar_agendamento as criar_agendamento_service,
    consultar_agendamento,
    listar_agendamentos,
    remover_agendamento,
    consultar_agendamentos_por_barbeiro,
    consultar_agendamentos_por_horario,
)
from src.domain.exceptions import *
from tests.mock import *



def test_criar_agendamento_raises(
    session_maker,
    mock_criar_usuario,
    mock_criar_jornada_de_trabalho,
    mock_criar_servicos,
):
    base_time = datetime.now() + timedelta(days=1)
    h_inicio = base_time.replace(hour=10, minute=0, second=0, microsecond=0)
    h_fim = base_time.replace(hour=11, minute=30, second=0, microsecond=0)
    mock_criar_servicos({"id0": "servico-001", "id1": "servico-002", "id2": "servico-003"})

    # ServicoNaoEncontrado
    with pytest.raises(ServicoNaoEncontrado):
        criar_agendamento_service(
            uow=UnidadeDeTrabalho(session_maker),
            horario_inicio=h_inicio,
            horario_fim=h_fim,
            barbeiro_cpf="25811756054",
            cliente_cpf="05705608020",
            servicos_id=["invalido"],
        )

    # UsuarioNaoEncontrado
    with pytest.raises(UsuarioNaoEncontrado):
        criar_agendamento_service(
            uow=UnidadeDeTrabalho(session_maker),
            horario_inicio=h_inicio,
            horario_fim=h_fim,
            barbeiro_cpf="25811756054",
            cliente_cpf="99999999999",
            servicos_id=["servico-001", "servico-002", "servico-003"],
        )

    # BarbeiroNaoEncontrado
    with pytest.raises(BarbeiroNaoEncontrado):
        criar_agendamento_service(
            uow=UnidadeDeTrabalho(session_maker),
            horario_inicio=h_inicio,
            horario_fim=h_fim,
            barbeiro_cpf="99999999999",
            cliente_cpf="05705608020",
            servicos_id=["servico-001", "servico-002", "servico-003"],
        )


def test_criar_agendamento_e_conflito(
    session_maker,
    mock_criar_usuario,
    mock_criar_jornada_de_trabalho,
    mock_criar_servicos,
):
    base_time = datetime.now() + timedelta(days=1)
    hora_inicio = base_time.replace(hour=10, minute=0, second=0, microsecond=0)
    hora_fim = base_time.replace(hour=11, minute=30, second=0, microsecond=0)
    mock_criar_servicos({"id0": "servico-001", "id1": "servico-002", "id2": "servico-003"})

    # Criação bem-sucedida
    criar_agendamento_service(
        uow=UnidadeDeTrabalho(session_maker),
        horario_inicio=hora_inicio,
        horario_fim=hora_fim,
        barbeiro_cpf="25811756054",
        cliente_cpf="05705608020",
        servicos_id=["servico-001", "servico-002", "servico-003"],
    )

    # Tentativa de conflito no mesmo horário
    with pytest.raises(HorarioIndisponivelParaBarbeiro):
        criar_agendamento_service(
            uow=UnidadeDeTrabalho(session_maker),
            horario_inicio=hora_inicio,
            horario_fim=hora_fim,
            barbeiro_cpf="25811756054",
            cliente_cpf="05705608020",
            servicos_id=["servico-001", "servico-002", "servico-003"],
        )


def test_consultar_agendamento(
    session_maker,
    mock_criar_usuario,
    mock_criar_jornada_de_trabalho,
    mock_criar_servicos,
):
    base_time = datetime.now() + timedelta(days=1)
    h_inicio = base_time.replace(hour=10, minute=0, second=0, microsecond=0)
    h_fim = base_time.replace(hour=11, minute=30, second=0, microsecond=0)
    mock_criar_servicos({"id0": "servico-001", "id1": "servico-002", "id2": "servico-003"})


    criar_agendamento_service(
        uow=UnidadeDeTrabalho(session_maker),
        horario_inicio=h_inicio,
        horario_fim=h_fim,
        barbeiro_cpf="25811756054",
        cliente_cpf="05705608020",
        servicos_id=["servico-001", "servico-002", "servico-003"],
    )

    with UnidadeDeTrabalho(session_maker) as uow2:
        agendamentos = uow2.agendamentos.listar()
        agendamento = agendamentos[0]
        agendamento_dict = consultar_agendamento(uow2, agendamento.id)

        assert isinstance(agendamento_dict, dict)
        assert agendamento_dict["barbeiro"]["cpf"] == "25811756054"

    agendamento_vazio = consultar_agendamento(UnidadeDeTrabalho(session_maker), "agendamento-naoexiste")
    assert agendamento_vazio == {}


def test_listar_agendamentos(
    session_maker,
    mock_criar_usuario,
    mock_criar_jornada_de_trabalho,
    mock_criar_servicos,
):
    base_time = datetime.now() + timedelta(days=2)
    h_inicio = base_time.replace(hour=10, minute=0, second=0, microsecond=0)
    h_fim = base_time.replace(hour=11, minute=30, second=0, microsecond=0)
    mock_criar_servicos({"id0": "servico-001", "id1": "servico-002", "id2": "servico-003"})


    criar_agendamento_service(
        uow=UnidadeDeTrabalho(session_maker),
        horario_inicio=h_inicio,
        horario_fim=h_fim,
        barbeiro_cpf="25811756054",
        cliente_cpf="05705608020",
        servicos_id=["servico-001", "servico-002", "servico-003"],
    )

    agendamentos = listar_agendamentos(UnidadeDeTrabalho(session_maker))
    assert len(agendamentos) >= 1
    assert agendamentos[0]["cliente"]["cpf"] == "05705608020"


def test_remover_agendamento(
    session_maker,
    mock_criar_usuario,
    mock_criar_jornada_de_trabalho,
    mock_criar_servicos,
):
    base_time = datetime.now() + timedelta(days=3)
    h_inicio = base_time.replace(hour=10, minute=0, second=0, microsecond=0)
    h_fim = base_time.replace(hour=11, minute=30, second=0, microsecond=0)
    mock_criar_servicos({"id0": "servico-001", "id1": "servico-002", "id2": "servico-003"})


    criar_agendamento_service(
        uow=UnidadeDeTrabalho(session_maker),
        horario_inicio=h_inicio,
        horario_fim=h_fim,
        barbeiro_cpf="25811756054",
        cliente_cpf="05705608020",
        servicos_id=["servico-001", "servico-002", "servico-003"],
    )

    with UnidadeDeTrabalho(session_maker) as uow2:
        agendamento = uow2.agendamentos.listar()[0]
        remover_agendamento(uow2, agendamento.id)

    with pytest.raises(AgendamentoNaoEncontrado):
        remover_agendamento(UnidadeDeTrabalho(session_maker), agendamento.id)


def test_consultar_agendamentos_por_barbeiro_e_horario(
    session_maker,
    mock_criar_usuario,
    mock_criar_jornada_de_trabalho,
    mock_criar_servicos,
):
    base_time = datetime.now() + timedelta(days=4)
    h_inicio = base_time.replace(hour=10, minute=0, second=0, microsecond=0)
    h_fim = base_time.replace(hour=11, minute=30, second=0, microsecond=0)
    mock_criar_servicos({"id0": "servico-001", "id1": "servico-002", "id2": "servico-003"})


    criar_agendamento_service(
        uow=UnidadeDeTrabalho(session_maker),
        horario_inicio=h_inicio,
        horario_fim=h_fim,
        barbeiro_cpf="25811756054",
        cliente_cpf="05705608020",
        servicos_id=["servico-001", "servico-002", "servico-003"],
    )

    ags_barbeiro = consultar_agendamentos_por_barbeiro(UnidadeDeTrabalho(session_maker), "25811756054")
    assert len(ags_barbeiro) >= 1
    assert ags_barbeiro[0]["barbeiro"]["cpf"] == "25811756054"

    ags_horario = consultar_agendamentos_por_horario(
        UnidadeDeTrabalho(session_maker),
        (h_inicio, h_fim),
    )
    assert len(ags_horario) >= 1
    assert ags_horario[0]["cliente"]["cpf"] == "05705608020"
