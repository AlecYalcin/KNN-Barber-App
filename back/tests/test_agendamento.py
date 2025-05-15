import pytest
from datetime import date, time
from back.domain.models import (
    Cliente, Barbeiro, Servico, Jornada, Horario,
    MetodoPagamento, StatusServico
)
from back.repositories.agendamento_repository import AgendamentoRepository

@pytest.fixture
def cliente():
    return Cliente("1", "João", "joao@email.com", "9999-9999", "senha123")

@pytest.fixture
def barbeiro():
    return Barbeiro("2", "Carlos", "carlos@email.com", "8888-8888", "senha456", "3333-3333")

@pytest.fixture
def servico():
    return Servico("3", "Barba", "Barba completa", 30, duracao=30)

@pytest.fixture
def jornada_com_horario_disponivel():
    jornada = Jornada(date(2025, 5, 13), "tarde")
    horario = Horario(time(14, 0), time(14, 30))
    jornada.adicionar_horario(horario)
    return jornada

def test_listar_servicos(servico):
    lista = AgendamentoRepository.listar_servicos([servico])
    assert len(lista) == 1
    assert lista[0].nome == "Barba"

def test_listar_horarios_disponiveis(jornada_com_horario_disponivel):
    horarios = AgendamentoRepository.listar_horarios_disponiveis(jornada_com_horario_disponivel)
    assert len(horarios) == 1
    assert horarios[0].disponivel is True

def test_calcular_duracao_total(servico):
    duracao = AgendamentoRepository.calcular_duracao_total([servico])
    assert duracao == 30

def test_calcular_valor_total(servico):
    valor = AgendamentoRepository.calcular_valor_total([servico])
    assert valor == 30

def test_agendar_sucesso(cliente, barbeiro, jornada_com_horario_disponivel, servico):
    horario = jornada_com_horario_disponivel.horarios[0]
    agendamento = AgendamentoRepository.agendar(
        cliente, barbeiro, jornada_com_horario_disponivel, horario, servico, MetodoPagamento.PIX
    )
    assert agendamento.status_servico == StatusServico.AGENDADO
    assert agendamento.pagamento.valor == servico.valor_base
    assert not agendamento.horario.disponivel


def test_agendar_falha_horario_indisponivel(cliente, barbeiro, jornada_com_horario_disponivel, servico):
    horario = jornada_com_horario_disponivel.horarios[0]
    horario.disponivel = False  # simula indisponibilidade

    with pytest.raises(Exception, match="Horário não está mais disponível"):
        AgendamentoRepository.agendar(
            cliente, barbeiro, jornada_com_horario_disponivel, horario, servico, MetodoPagamento.PIX
        )
