import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from domain.models import (
    Cliente, Barbeiro, Servico, Horario,
    MetodoPagamento, StatusServico, HorarioIndisponivelParaBarbeiro,
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
    horario = Horario("1", "2025-04-10", "14:00", "Disponível")
    atendimento = criar_horario_de_atendimento(cliente, barbeiro, horario, servico, MetodoPagamento.PIX)

    assert atendimento._status_servico == StatusServico.AGENDADO
    assert atendimento._pagamento._valor == 50

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
    horario = Horario("2", "2025-04-10", "15:00", "Indisponível")

    with pytest.raises(HorarioIndisponivelParaBarbeiro):
        criar_horario_de_atendimento(cliente, barbeiro, horario, servico, MetodoPagamento.CARTAO)
