import pytest
from datetime import date, time

from domain.models import (
    Cliente,
    Barbeiro,
    Servico,
    Jornada,
    Horario,
    MetodoPagamento,
    StatusServico,
    HorarioIndisponivelParaBarbeiro,
    criar_horario_de_atendimento
)


@pytest.mark.parametrize(
    "cliente, barbeiro, servico",
    [
        (
            Cliente("123", "João", "joao@email.com", "9999-9999", "senha123"),
            Barbeiro("456", "Carlos", "carlos@email.com", "8888-8888", "senha456", "3333-3333"),
            Servico("1", "Corte de Cabelo", "Corte simples", 50)
        )
    ]
)
def test_criacao_atendimento_sucesso(cliente, barbeiro, servico):
    jornada = Jornada(date(2025, 4, 10), "tarde")
    horario = Horario(time(14, 0), time(14, 30))
    jornada.adicionar_horario(horario)
    barbeiro.definir_jornada(jornada)

    atendimento = criar_horario_de_atendimento(cliente, barbeiro, jornada, horario, servico, MetodoPagamento.PIX)

    assert atendimento._status_servico == StatusServico.AGENDADO
    assert atendimento._pagamento._valor == 50
    assert atendimento._pagamento._metodo == MetodoPagamento.PIX
    assert atendimento._horario.disponivel is False


@pytest.mark.parametrize(
    "cliente, barbeiro, servico",
    [
        (
            Cliente("123", "João", "joao@email.com", "9999-9999", "senha123"),
            Barbeiro("456", "Carlos", "carlos@email.com", "8888-8888", "senha456", "3333-3333"),
            Servico("1", "Corte de Cabelo", "Corte simples", 50)
        )
    ]
)
def test_criacao_atendimento_horario_indisponivel(cliente, barbeiro, servico):
    jornada = Jornada(date(2025, 4, 10), "tarde")
    horario = Horario(time(15, 0), time(15, 30))
    horario.disponivel = False  # Simula horário já ocupado
    jornada.adicionar_horario(horario)
    barbeiro.definir_jornada(jornada)

    with pytest.raises(HorarioIndisponivelParaBarbeiro):
        criar_horario_de_atendimento(cliente, barbeiro, jornada, horario, servico, MetodoPagamento.CARTAO)
