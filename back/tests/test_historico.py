import pytest
from datetime import date, time
from back.repositories.historico_repository import HistoricoRepository

# Mocks simples para as dependências
class Cliente:
    def __init__(self, cpf):
        self.cpf = cpf

class Servico:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

class Pagamento:
    def __init__(self, valor, status, metodo):
        self.valor = valor
        self.status = status
        self.metodo = metodo

class StatusPagamento:
    value = "Pago"

class MetodoPagamento:
    value = "Crédito"

class Jornada:
    def __init__(self, dia):
        self.dia = dia

class Horario:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim

class HorarioDeAtendimento:
    def __init__(self, cliente, servico, pagamento, jornada, horario):
        self.cliente = cliente
        self.servico = servico
        self.pagamento = pagamento
        self.jornada = jornada
        self.horario = horario

@pytest.fixture
def repo():
    return HistoricoRepository()

@pytest.fixture
def cliente():
    return Cliente("12345678900")

@pytest.fixture
def agendamento(cliente):
    servico = Servico("1", "Corte")
    pagamento = Pagamento(50.0, StatusPagamento(), MetodoPagamento())
    jornada = Jornada(date(2024, 5, 1))
    horario = Horario(time(10, 0), time(10, 30))
    return HorarioDeAtendimento(cliente, servico, pagamento, jornada, horario)

def test_listar_historico_sem_filtro(repo, cliente, agendamento):
    agendamentos = [agendamento]
    resultado = repo.listar_historico(agendamentos, cliente)
    assert len(resultado) == 1
    assert resultado[0] == agendamento

def test_listar_historico_com_data(repo, cliente, agendamento):
    agendamentos = [agendamento]
    data_inicio = date(2024, 4, 30)
    data_fim = date(2024, 5, 2)
    resultado = repo.listar_historico(agendamentos, cliente, data_inicio, data_fim)
    assert agendamento in resultado

def test_filtrar_por_servico(repo, cliente, agendamento):
    agendamentos = [agendamento]
    resultado = repo.filtrar_por_servico(agendamentos, "1")
    assert len(resultado) == 1
    assert resultado[0].servico.id == "1"

def test_visualizar_detalhes(repo, agendamento):
    detalhes = repo.visualizar_detalhes(agendamento)
    assert detalhes["servico"] == "Corte"
    assert detalhes["valor"] == 50.0
    assert detalhes["status_pagamento"] == "Pago"
    assert detalhes["forma_pagamento"] == "Crédito"
    assert detalhes["data"] == date(2024, 5, 1)
    assert detalhes["horario"] == (time(10, 0), time(10, 30))

def test_exportar_historico(repo, agendamento):
    agendamentos = [agendamento]
    historico = repo.exportar_historico(agendamentos)
    assert isinstance(historico, list)
    assert historico[0]["servico"] == "Corte"
    assert historico[0]["valor"] == 50.0
