import pytest
from datetime import date, timedelta
from unittest.mock import Mock, create_autospec
from back.domain.models import Barbeiro, HorarioDeAtendimento, StatusPagamento, MetodoPagamento
from back.repositories.relatorio_financeiro_repository import RelatorioFinanceiroRepository

# Fixtures usando create_autospec para mocks mais precisos
@pytest.fixture
def repository():
    return RelatorioFinanceiroRepository()

@pytest.fixture
def barbeiro():
    # Cria um mock que respeita a assinatura da classe Barbeiro
    barb = create_autospec(Barbeiro, instance=True)
    barb.nome = "João"
    barb.cpf = "123.456.789-00"
    barb.email = "joao@barbearia.com"
    barb.telefone = "(11) 99999-9999"
    barb.senha = "senha123"
    barb.tel_trabalho = "(11) 98888-8888"
    return barb

@pytest.fixture
def outro_barbeiro():
    barb = create_autospec(Barbeiro, instance=True)
    barb.nome = "Carlos"
    barb.cpf = "987.654.321-00"
    barb.email = "carlos@barbearia.com"
    barb.telefone = "(11) 97777-7777"
    barb.senha = "senha456"
    barb.tel_trabalho = "(11) 96666-6666"
    return barb

@pytest.fixture
def agendamentos(barbeiro, outro_barbeiro):
    hoje = date.today()
    ontem = hoje - timedelta(days=1)
    semana_passada = hoje - timedelta(days=7)
    
    def criar_agendamento(barb, dia, valor, status, metodo):
        ag = create_autospec(HorarioDeAtendimento, instance=True)
        ag.barbeiro = barb
        ag.jornada = Mock(dia=dia)
        ag.pagamento = Mock(
            valor=valor,
            status=status,
            metodo=metodo,
            confirmar=Mock()
        )
        return ag
    
    return [
        criar_agendamento(barbeiro, hoje, 50.0, StatusPagamento.CONCLUIDO, MetodoPagamento.CARTAO),
        criar_agendamento(barbeiro, ontem, 30.0, StatusPagamento.CONCLUIDO, MetodoPagamento.DINHEIRO),
        criar_agendamento(barbeiro, semana_passada, 40.0, StatusPagamento.PENDENTE, MetodoPagamento.CARTAO),
        criar_agendamento(outro_barbeiro, hoje, 60.0, StatusPagamento.CONCLUIDO, MetodoPagamento.PIX)
    ]

# Testes
def test_listar_pagamentos_realizados_filtra_por_barbeiro(repository, agendamentos, barbeiro):
    resultados = repository.listar_pagamentos_realizados(agendamentos, barbeiro)
    assert len(resultados) == 2
    assert all(ag.barbeiro == barbeiro for ag in resultados)
    assert all(ag.pagamento.status == StatusPagamento.CONCLUIDO for ag in resultados)

def test_confirmar_pagamento(repository, agendamentos):
    ag_pendente = next(ag for ag in agendamentos if ag.pagamento.status == StatusPagamento.PENDENTE)
    resultado = repository.confirmar_pagamento(ag_pendente)
    ag_pendente.pagamento.confirmar.assert_called_once()
    assert resultado == ag_pendente

def test_calcular_metricas(repository, agendamentos, barbeiro):
    metricas = repository.calcular_metricas(agendamentos, barbeiro)
    assert metricas["total_recebido"] == 80.0
    assert metricas["media_por_pagamento"] == 40.0
    assert metricas["quantidade_pagamentos"] == 2
    
def test_listar_pagamentos_vazia(repository, barbeiro):
    resultados = repository.listar_pagamentos_realizados([], barbeiro)
    assert len(resultados) == 0

def test_listar_pagamentos_apenas_pendentes(repository, barbeiro):
    # Criar agendamentos apenas com status PENDENTE
    ag_pendente = create_autospec(HorarioDeAtendimento, instance=True)
    ag_pendente.barbeiro = barbeiro
    ag_pendente.jornada = Mock(dia=date.today())
    ag_pendente.pagamento = Mock(status=StatusPagamento.PENDENTE)
    
    resultados = repository.listar_pagamentos_realizados([ag_pendente], barbeiro)
    assert len(resultados) == 0

def test_listar_pagamentos_filtro_composto(repository, agendamentos, barbeiro):
    hoje = date.today()
    resultados = repository.listar_pagamentos_realizados(
        agendamentos,
        barbeiro,
        data_inicio=hoje - timedelta(days=2),
        data_fim=hoje,
        metodo=MetodoPagamento.CARTAO
    )
    assert len(resultados) == 1
    assert resultados[0].jornada.dia == hoje
    assert resultados[0].pagamento.metodo == MetodoPagamento.CARTAO

def test_confirmar_pagamento_ja_concluido(repository, agendamentos):
    ag_concluido = next(ag for ag in agendamentos if ag.pagamento.status == StatusPagamento.CONCLUIDO)
    resultado = repository.confirmar_pagamento(ag_concluido)
    
    # Verifica que confirmar() foi chamado (comportamento atual)
    ag_concluido.pagamento.confirmar.assert_called_once()
    # Mas o status permanece CONCLUIDO
    assert ag_concluido.pagamento.status == StatusPagamento.CONCLUIDO
    assert resultado == ag_concluido

def test_confirmar_pagamento_invalido(repository):
    with pytest.raises(Exception):
        repository.confirmar_pagamento(None)

# Testes adicionais para calcular_metricas
def test_calcular_metricas_apenas_um_pagamento(repository, barbeiro):
    hoje = date.today()
    ag = create_autospec(HorarioDeAtendimento, instance=True)
    ag.barbeiro = barbeiro
    ag.pagamento = Mock(valor=75.0, status=StatusPagamento.CONCLUIDO)
    
    metricas = repository.calcular_metricas([ag], barbeiro)
    assert metricas["total_recebido"] == 75.0
    assert metricas["media_por_pagamento"] == 75.0
    assert metricas["quantidade_pagamentos"] == 1

def test_calcular_metricas_valores_altos(repository, barbeiro):
    ag1 = create_autospec(HorarioDeAtendimento, instance=True)
    ag1.barbeiro = barbeiro
    ag1.pagamento = Mock(valor=1000.0, status=StatusPagamento.CONCLUIDO)
    
    ag2 = create_autospec(HorarioDeAtendimento, instance=True)
    ag2.barbeiro = barbeiro
    ag2.pagamento = Mock(valor=2000.0, status=StatusPagamento.CONCLUIDO)
    
    metricas = repository.calcular_metricas([ag1, ag2], barbeiro)
    assert metricas["total_recebido"] == 3000.0
    assert metricas["media_por_pagamento"] == 1500.0

def test_calcular_metricas_com_agendamentos_misto(repository, barbeiro, outro_barbeiro):
    # 2 concluídos do barbeiro, 1 pendente do barbeiro, 1 concluído de outro
    ag1 = create_autospec(HorarioDeAtendimento, instance=True)
    ag1.barbeiro = barbeiro
    ag1.pagamento = Mock(valor=50.0, status=StatusPagamento.CONCLUIDO)
    
    ag2 = create_autospec(HorarioDeAtendimento, instance=True)
    ag2.barbeiro = barbeiro
    ag2.pagamento = Mock(valor=30.0, status=StatusPagamento.CONCLUIDO)
    
    ag3 = create_autospec(HorarioDeAtendimento, instance=True)
    ag3.barbeiro = barbeiro
    ag3.pagamento = Mock(valor=40.0, status=StatusPagamento.PENDENTE)
    
    ag4 = create_autospec(HorarioDeAtendimento, instance=True)
    ag4.barbeiro = outro_barbeiro
    ag4.pagamento = Mock(valor=60.0, status=StatusPagamento.CONCLUIDO)
    
    metricas = repository.calcular_metricas([ag1, ag2, ag3, ag4], barbeiro)
    assert metricas["quantidade_pagamentos"] == 2  # Deve ignorar ag3 e ag4
    assert metricas["total_recebido"] == 80.0
