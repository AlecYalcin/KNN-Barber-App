import pytest
from enum import Enum
from back.repositories.pagamento_repository import PagamentoRepository

# Mocks para os testes
class MetodoPagamento(Enum):
    DINHEIRO = "Dinheiro"
    CARTAO = "Cartão"
    PIX = "Pix"

class Pagamento:
    def __init__(self, valor, metodo):
        self.valor = valor
        self.metodo = metodo

class HorarioDeAtendimento:
    def __init__(self, pagamento):
        self.pagamento = pagamento

@pytest.fixture
def repo():
    return PagamentoRepository()

@pytest.fixture
def pagamento():
    return Pagamento(valor=50.0, metodo=MetodoPagamento.CARTAO)

@pytest.fixture
def agendamento(pagamento):
    return HorarioDeAtendimento(pagamento)

def test_exibir_valor_total(repo, agendamento):
    assert repo.exibir_valor_total(agendamento) == 50.0

def test_listar_formas_pagamento(repo):
    formas = repo.listar_formas_pagamento()
    assert "Dinheiro" in formas
    assert "Cartão" in formas
    assert "PIX" in formas

def test_selecionar_forma_pagamento(repo, agendamento):
    novo_metodo = MetodoPagamento.PIX
    repo.selecionar_forma_pagamento(agendamento, novo_metodo)
    assert agendamento.pagamento.metodo == MetodoPagamento.PIX

def test_alterar_forma_pagamento(repo, agendamento):
    novo_metodo = MetodoPagamento.DINHEIRO
    repo.alterar_forma_pagamento(agendamento, novo_metodo)
    assert agendamento.pagamento.metodo == MetodoPagamento.DINHEIRO

def test_confirmar_detalhes_pagamento(repo, agendamento):
    detalhes = repo.confirmar_detalhes_pagamento(agendamento)
    assert detalhes == {
        "valor_total": 50.0,
        "forma_pagamento": "Cartão"
    }
