import pytest
from back.repositories.cliente_repository import ClienteRepository
from back.domain.models import Cliente

@pytest.fixture
def repo():
    return ClienteRepository()

def test_criar_cliente(repo):
    cliente = repo.criar_cliente("123", "João", "joao@email.com", "99999-9999", "senha123")
    assert isinstance(cliente, Cliente)
    assert cliente.nome == "João"
    assert len(repo.clientes) == 1

def test_buscar_cliente_por_cpf(repo):
    repo.criar_cliente("123", "Maria", "maria@email.com", "88888-8888", "senha123")
    cliente = repo.buscar_cliente_por_cpf("123")
    assert cliente is not None
    assert cliente.nome == "Maria"

def test_buscar_cliente_por_email(repo):
    repo.criar_cliente("456", "Carlos", "carlos@email.com", "77777-7777", "senha456")
    cliente = repo.buscar_cliente_por_email("carlos@email.com")
    assert cliente is not None
    assert cliente.cpf == "456"

def test_listar_clientes(repo):
    repo.criar_cliente("1", "A", "a@email.com", "1111", "s1")
    repo.criar_cliente("2", "B", "b@email.com", "2222", "s2")
    clientes = repo.listar_clientes()
    assert len(clientes) == 2

def test_atualizar_dados(repo):
    repo.criar_cliente("789", "Ana", "ana@email.com", "12345", "senha")
    atualizado = repo.atualizar_dados("789", nome="Ana Paula", email="ana.paula@email.com")
    assert atualizado.nome == "Ana Paula"
    assert atualizado.email == "ana.paula@email.com"

def test_remover_cliente(repo):
    repo.criar_cliente("321", "Pedro", "pedro@email.com", "3333", "senha")
    sucesso = repo.remover_cliente("321")
    assert sucesso is True
    assert repo.buscar_cliente_por_cpf("321") is None
