import pytest
from back.repositories.barbeiro_repository import BarbeiroRepository
from back.domain.models import Barbeiro

@pytest.fixture
def repo():
    return BarbeiroRepository()

def test_criar_barbeiro(repo):
    barbeiro = repo.criar_barbeiro("123", "João", "joao@email.com", "99999-9999", "senha123", "88888-8888")
    assert isinstance(barbeiro, Barbeiro)
    assert barbeiro.nome == "João"
    assert len(repo.barbeiros) == 1

def test_buscar_barbeiro_por_cpf(repo):
    repo.criar_barbeiro("123", "Maria", "maria@email.com", "99999-9999", "senha123", "88888-8888")
    resultado = repo.buscar_barbeiro_por_cpf("123")
    assert resultado is not None
    assert resultado.nome == "Maria"

def test_buscar_barbeiro_por_email(repo):
    repo.criar_barbeiro("456", "Carlos", "carlos@email.com", "99999-9999", "senha456", "88888-8888")
    resultado = repo.buscar_barbeiro_por_email("carlos@email.com")
    assert resultado is not None
    assert resultado.cpf == "456"

def test_listar_barbeiros(repo):
    repo.criar_barbeiro("1", "A", "a@email.com", "1", "s1", "2")
    repo.criar_barbeiro("2", "B", "b@email.com", "2", "s2", "3")
    barbeiros = repo.listar_barbeiros()
    assert len(barbeiros) == 2

def test_atualizar_dados(repo):
    repo.criar_barbeiro("789", "Ana", "ana@email.com", "12345", "senha", "54321")
    atualizado = repo.atualizar_dados("789", nome="Ana Paula", email="ana.paula@email.com")
    assert atualizado.nome == "Ana Paula"
    assert atualizado.email == "ana.paula@email.com"

def test_remover_barbeiro(repo):
    repo.criar_barbeiro("321", "Pedro", "pedro@email.com", "7777", "senha", "6666")
    sucesso = repo.remover_barbeiro("321")
    assert sucesso is True
    assert repo.buscar_barbeiro_por_cpf("321") is None
