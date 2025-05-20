import pytest
import uuid
from back.repositories.servico_repository import ServicoRepository

# Mock da classe Servico
class Servico:
    def __init__(self, nome, descricao, valor_base, duracao):
        self.id = str(uuid.uuid4())
        self.nome = nome
        self.descricao = descricao
        self.valor_base = valor_base
        self.duracao = duracao

@pytest.fixture
def repo():
    return ServicoRepository()

@pytest.fixture
def servico_exemplo():
    return Servico("Corte de Cabelo", "Corte simples", 30.0, 30)

def test_cadastrar_servico(repo, servico_exemplo):
    repo.cadastrar_servico(servico_exemplo)
    assert servico_exemplo in repo.listar_servicos()

def test_listar_servicos(repo, servico_exemplo):
    repo.cadastrar_servico(servico_exemplo)
    lista = repo.listar_servicos()
    assert len(lista) == 1
    assert lista[0].nome == "Corte de Cabelo"

def test_editar_servico(repo, servico_exemplo):
    repo.cadastrar_servico(servico_exemplo)
    repo.editar_servico(servico_exemplo, nome="Corte Especial", valor_base=45.0)

    assert servico_exemplo.nome == "Corte Especial"
    assert servico_exemplo.valor_base == 45.0
    assert servico_exemplo.descricao == "Corte simples"  # Não foi alterado

def test_excluir_servico(repo, servico_exemplo):
    repo.cadastrar_servico(servico_exemplo)
    repo.excluir_servico(servico_exemplo)
    assert servico_exemplo not in repo.listar_servicos()

def test_buscar_servico_por_id(repo, servico_exemplo):
    repo.cadastrar_servico(servico_exemplo)
    encontrado = repo.buscar_servico_por_id(servico_exemplo.id)
    assert encontrado is servico_exemplo

def test_buscar_servico_por_id_inexistente(repo):
    resultado = repo.buscar_servico_por_id("id-invalido")
    assert resultado is None
