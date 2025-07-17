import pytest
from datetime import datetime
from src.domain.models import *
from tests.mock import *

def test_normalizador_de_horarios():
    horario = {
        "inicio":datetime(2025, 5, 27, 10, 0), 
        "fim":datetime(2025, 5, 27, 11, 40)
    }

    novo_horario = normalizar_horarios(horario=tuple(horario.values()))
    assert novo_horario[0] == datetime(2025, 5, 27, 10, 0)
    assert novo_horario[1] == datetime(2025, 5, 27, 12, 0)

def test_criar_agendamento_completo(
    mock_usuario_teste,
    mock_barbeiro_teste,
    mock_servicos_teste,
):
    usuario = mock_usuario_teste
    barbeiro = mock_barbeiro_teste
    servicos = mock_servicos_teste

    horario = {
        "inicio":datetime(2025, 5, 27, 8, 0), 
        "fim":datetime(2025, 5, 27, 10, 30)
    }

    agendamento = criar_agendamento(usuario, barbeiro, servicos, tuple(horario.values()))

    assert agendamento is not None
    assert agendamento.cliente == usuario
    assert agendamento.barbeiro == barbeiro.usuario
    assert agendamento.servicos == servicos
    assert agendamento.horario_inicio == datetime(2025, 5, 27, 8, 0)
    assert agendamento.horario_fim == datetime(2025, 5,27, 10, 30)

def test_agendamento_com_horario_invalido(
    mock_usuario_teste,
    mock_barbeiro_teste,
    mock_servicos_teste,
):
    usuario = mock_usuario_teste
    barbeiro = mock_barbeiro_teste
    servicos = mock_servicos_teste

    horario = {
        "inicio":datetime(2025, 5, 28, 10, 0), 
        "fim":datetime(2025, 5, 27, 11, 40)
    }

    with pytest.raises(HorarioInvalido):
        criar_agendamento(usuario, barbeiro, servicos, tuple(horario.values()))

def test_agendamento_com_horario_fora_da_jornada(
    mock_usuario_teste,
    mock_barbeiro_teste,
    mock_servicos_teste,
):
    usuario = mock_usuario_teste
    barbeiro = mock_barbeiro_teste
    servicos = mock_servicos_teste

    horario = {
        "inicio":datetime(2025, 5, 25, 10, 0), 
        "fim":datetime(2025, 5, 25, 11, 40)
    }

    with pytest.raises(HorarioForaDaJornada):
        criar_agendamento(usuario, barbeiro, servicos, tuple(horario.values()))

def test_agendamento_com_horario_indisponivel(
    mock_usuario_teste,
    mock_barbeiro_teste,
    mock_servicos_teste,
):
    usuario = mock_usuario_teste
    barbeiro = mock_barbeiro_teste
    servicos = mock_servicos_teste

    horario = {
        "inicio":datetime(2025, 5, 29, 9, 0), 
        "fim":datetime(2025, 5, 29, 10, 45)
    }

    with pytest.raises(HorarioIndisponivelException):
        criar_agendamento(usuario, barbeiro, servicos, tuple(horario.values()))

def test_agendamento_com_horario_insuficiente(
    mock_usuario_teste,
    mock_barbeiro_teste,
    mock_servicos_teste,
):
    usuario = mock_usuario_teste
    barbeiro = mock_barbeiro_teste
    servicos = mock_servicos_teste

    horario = {
        "inicio":datetime(2025, 5, 29, 9, 0), 
        "fim":datetime(2025, 5, 29, 10, 0)
    }

    with pytest.raises(HorarioInsuficiente):
        criar_agendamento(usuario, barbeiro, servicos, tuple(horario.values()))
