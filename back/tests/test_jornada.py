import pytest
from datetime import date, time
from back.repositories.jornada_repository import JornadaRepository

# Mocks para as dependências
class Horario:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim
        self.disponivel = True
        self.justificativa = None

class Jornada:
    def __init__(self, dia, turno):
        self.dia = dia
        self.turno = turno
        self.horarios = []

    def adicionar_horario(self, horario):
        self.horarios.append(horario)

class Barbeiro:
    def __init__(self, nome):
        self.nome = nome
        self.jornadas = []

    def definir_jornada(self, jornada):
        self.jornadas.append(jornada)

@pytest.fixture
def repo():
    return JornadaRepository()

@pytest.fixture
def barbeiro():
    return Barbeiro("João")

@pytest.fixture
def jornada():
    return Jornada(date(2024, 5, 15), "Manhã")

def test_definir_jornada(repo, barbeiro):
    dia = date(2024, 5, 15)
    turno = "Tarde"
    jornada = repo.definir_jornada(barbeiro, dia, turno)
    assert jornada in barbeiro.jornadas
    assert jornada.dia == dia
    assert jornada.turno == turno

def test_editar_jornada(repo, jornada):
    novo_dia = date(2024, 5, 20)
    novo_turno = "Noite"
    repo.editar_jornada(jornada, novo_dia, novo_turno)
    assert jornada.dia == novo_dia
    assert jornada.turno == novo_turno

def test_desativar_jornada(repo, jornada):
    horario1 = Horario(time(9, 0), time(10, 0))
    horario2 = Horario(time(10, 0), time(11, 0))
    jornada.horarios = [horario1, horario2]
    repo.desativar_jornada(jornada)
    assert not horario1.disponivel
    assert not horario2.disponivel

def test_registrar_indisponibilidade(repo, jornada):
    inicio = time(14, 0)
    fim = time(15, 0)
    justificativa = "Reunião"
    horario = repo.registrar_indisponibilidade(jornada, inicio, fim, justificativa)
    assert not horario.disponivel
    assert horario in jornada.horarios

def test_editar_horario_indisponivel(repo):
    horario = Horario(time(8, 0), time(9, 0))
    novo_inicio = time(9, 0)
    novo_fim = time(10, 0)
    repo.editar_horario_indisponivel(horario, novo_inicio, novo_fim, disponivel=False)
    assert horario.inicio == novo_inicio
    assert horario.fim == novo_fim
    assert not horario.disponivel

def test_excluir_horario_indisponivel(repo, jornada):
    horario = Horario(time(11, 0), time(12, 0))
    jornada.adicionar_horario(horario)
    result = repo.excluir_horario_indisponivel(jornada, horario)
    assert result is True
    assert horario not in jornada.horarios

def test_excluir_horario_indisponivel_nao_existente(repo, jornada):
    horario = Horario(time(11, 0), time(12, 0))
    result = repo.excluir_horario_indisponivel(jornada, horario)
    assert result is False
