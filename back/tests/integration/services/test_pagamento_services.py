import pytest
from datetime import datetime, timedelta
from src.domain.models import Pagamento, Agendamento, Usuario, Servico, Barbeiro
from src.domain.exceptions import *
from src.service.services.pagamento import *
from src.service.unit_of_work import UnidadeDeTrabalho
from src.domain.value_objects import MetodoPagamento
from tests.mock import *

def test_criar_pagamento_service(session_maker, mock_criar_usuarios_e_agendamento):
    # Criar dados necessários
    cliente, barbeiro, agendamento = mock_criar_usuarios_e_agendamento
    
    # Teste com valor inválido (zero)
    with pytest.raises(ValorInvalido):
        criar_pagamento(
            uow=UnidadeDeTrabalho(session_maker),
            valor=0.0,
            metodo=MetodoPagamento.PIX,
            agendamento_id=agendamento.id,
            solicitante={"cpf": barbeiro.usuario.cpf, "eh_barbeiro": True}
        )
    
    # Teste com valor inválido (negativo)
    with pytest.raises(ValorInvalido):
        criar_pagamento(
            uow=UnidadeDeTrabalho(session_maker),
            valor=-10.0,
            metodo=MetodoPagamento.PIX,
            agendamento_id=agendamento.id,
            solicitante={"cpf": barbeiro.usuario.cpf, "eh_barbeiro": True}
        )
    
    # Teste com agendamento inexistente
    with pytest.raises(AgendamentoNaoEncontrado):
        criar_pagamento(
            uow=UnidadeDeTrabalho(session_maker),
            valor=50.0,
            metodo=MetodoPagamento.PIX,
            agendamento_id="agendamento-inexistente",
            solicitante={"cpf": barbeiro.usuario.cpf, "eh_barbeiro": True}
        )
    
    # Teste com usuário sem permissão (cliente)
    with pytest.raises(PermissaoNegada):
        criar_pagamento(
            uow=UnidadeDeTrabalho(session_maker),
            valor=50.0,
            metodo=MetodoPagamento.PIX,
            agendamento_id=agendamento.id,
            solicitante={"cpf": cliente.cpf, "eh_barbeiro": False}
        )
    
    # Teste de criação bem-sucedida
    criar_pagamento(
        uow=UnidadeDeTrabalho(session_maker),
        valor=50.0,
        metodo=MetodoPagamento.PIX,
        agendamento_id=agendamento.id,
        solicitante={"cpf": barbeiro.usuario.cpf, "eh_barbeiro": True}
    )
    
    # Verificar criação
    with UnidadeDeTrabalho(session_maker) as uow:
        pagamento = uow.pagamentos.consultar_por_agendamento(agendamento.id)
        assert pagamento is not None
        assert pagamento.valor == 50.0
        assert pagamento.metodo == MetodoPagamento.PIX
        assert pagamento.agendamento_id == agendamento.id

def test_consultar_pagamento_service(session_maker, mock_criar_pagamento):
    # Criar pagamento
    pagamento = mock_criar_pagamento
    
    # Consultar pagamento existente
    pagamento_encontrado = consultar_pagamento(
        uow=UnidadeDeTrabalho(session_maker),
        id=pagamento.id
    )
    # Comparar apenas os campos principais, ignorando diferenças de timestamp
    assert pagamento_encontrado['id'] == pagamento.to_dict()['id']
    assert pagamento_encontrado['valor'] == pagamento.to_dict()['valor']
    assert pagamento_encontrado['metodo'] == pagamento.to_dict()['metodo']
    assert pagamento_encontrado['agendamento_id'] == pagamento.to_dict()['agendamento_id']
    
    # Consultar pagamento inexistente
    pagamento_encontrado = consultar_pagamento(
        uow=UnidadeDeTrabalho(session_maker),
        id="pagamento-inexistente"
    )
    assert pagamento_encontrado == {}

def test_consultar_pagamento_por_agendamento_service(session_maker, mock_criar_pagamento):
    # Criar pagamento
    pagamento = mock_criar_pagamento
    
    # Consultar pagamento por agendamento
    pagamento_encontrado = consultar_pagamento_por_agendamento(
        uow=UnidadeDeTrabalho(session_maker),
        agendamento_id=pagamento.agendamento_id
    )
    assert pagamento_encontrado is not None
    # Comparar apenas os campos principais, ignorando diferenças de timestamp
    assert pagamento_encontrado['id'] == pagamento.to_dict()['id']
    assert pagamento_encontrado['valor'] == pagamento.to_dict()['valor']
    assert pagamento_encontrado['metodo'] == pagamento.to_dict()['metodo']
    assert pagamento_encontrado['agendamento_id'] == pagamento.to_dict()['agendamento_id']
    
    # Consultar agendamento sem pagamento
    pagamento_encontrado = consultar_pagamento_por_agendamento(
        uow=UnidadeDeTrabalho(session_maker),
        agendamento_id="agendamento-sem-pagamento"
    )
    assert pagamento_encontrado is None

def test_listar_pagamentos_de_cliente_service(session_maker, mock_criar_pagamentos_cliente):
    # Criar múltiplos pagamentos para um cliente
    cliente_cpf, pagamentos = mock_criar_pagamentos_cliente
    
    # Listar pagamentos do cliente
    pagamentos_encontrados = listar_pagamentos_de_cliente(
        uow=UnidadeDeTrabalho(session_maker),
        cpf=cliente_cpf
    )
    assert len(pagamentos_encontrados) == len(pagamentos)
    
    # Verificar se todos os pagamentos estão na lista
    for pagamento in pagamentos:
        assert any(p['id'] == pagamento.id for p in pagamentos_encontrados)
    
    # Listar pagamentos de cliente sem pagamentos
    pagamentos_encontrados = listar_pagamentos_de_cliente(
        uow=UnidadeDeTrabalho(session_maker),
        cpf="cliente-sem-pagamentos"
    )
    assert pagamentos_encontrados == []

def test_atualizar_pagamento_service(session_maker, mock_criar_pagamento):
    # Criar pagamento
    pagamento = mock_criar_pagamento
    
    # Teste com pagamento inexistente
    with pytest.raises(PagamentoNaoEncontrado):
        atualizar_pagamento(
            uow=UnidadeDeTrabalho(session_maker),
            id="pagamento-inexistente",
            novo_valor=60.0,
            novo_metodo=MetodoPagamento.CARTAO
        )
    
    # Teste com valor inválido
    with pytest.raises(ValorInvalido):
        atualizar_pagamento(
            uow=UnidadeDeTrabalho(session_maker),
            id=pagamento.id,
            novo_valor=-10.0
        )
    
    # Teste com usuário sem permissão
    with pytest.raises(PermissaoNegada):
        atualizar_pagamento(
            uow=UnidadeDeTrabalho(session_maker),
            id=pagamento.id,
            novo_valor=60.0,
            solicitante={"cpf": "cliente-sem-permissao", "eh_barbeiro": False}
        )
    
    # Teste de atualização bem-sucedida
    atualizar_pagamento(
        uow=UnidadeDeTrabalho(session_maker),
        id=pagamento.id,
        novo_valor=60.0,
        novo_metodo=MetodoPagamento.CARTAO,
        solicitante={"cpf": "barbeiro-com-permissao", "eh_barbeiro": True}
    )
    
    # Verificar atualização
    with UnidadeDeTrabalho(session_maker) as uow:
        pagamento_atualizado = uow.pagamentos.consultar(pagamento.id)
        assert pagamento_atualizado.valor == 60.0
        assert pagamento_atualizado.metodo == MetodoPagamento.CARTAO

def test_remover_pagamento_service(session_maker, mock_criar_pagamento):
    # Criar pagamento
    pagamento = mock_criar_pagamento
    
    # Verificar que existe
    with UnidadeDeTrabalho(session_maker) as uow:
        pagamento_encontrado = uow.pagamentos.consultar(pagamento.id)
        assert pagamento_encontrado == pagamento
    
    # Teste com pagamento inexistente
    with pytest.raises(PagamentoNaoEncontrado):
        remover_pagamento(
            uow=UnidadeDeTrabalho(session_maker),
            id="pagamento-inexistente"
        )
    
    # Teste com usuário sem permissão
    with pytest.raises(PermissaoNegada):
        remover_pagamento(
            uow=UnidadeDeTrabalho(session_maker),
            id=pagamento.id,
            solicitante={"cpf": "cliente-sem-permissao", "eh_barbeiro": False}
        )
    
    # Teste de remoção bem-sucedida
    remover_pagamento(
        uow=UnidadeDeTrabalho(session_maker),
        id=pagamento.id,
        solicitante={"cpf": "barbeiro-com-permissao", "eh_barbeiro": True}
    )
    
    # Verificar remoção
    with UnidadeDeTrabalho(session_maker) as uow:
        pagamento_encontrado = uow.pagamentos.consultar(pagamento.id)
        assert pagamento_encontrado is None

def test_validacoes_pagamento_service(session_maker, mock_criar_usuarios_e_agendamento):
    # Criar dados necessários
    cliente, barbeiro, agendamento = mock_criar_usuarios_e_agendamento
    
    # Teste com método de pagamento inválido
    with pytest.raises(ValueError):
        criar_pagamento(
            uow=UnidadeDeTrabalho(session_maker),
            valor=50.0,
            metodo="METODO_INVALIDO",
            agendamento_id=agendamento.id,
            solicitante={"cpf": barbeiro.usuario.cpf, "eh_barbeiro": True}
        )
    
    # Teste com valor muito alto
    with pytest.raises(ValorInvalido):
        criar_pagamento(
            uow=UnidadeDeTrabalho(session_maker),
            valor=1000000.0,  # Valor muito alto
            metodo=MetodoPagamento.PIX,
            agendamento_id=agendamento.id,
            solicitante={"cpf": barbeiro.usuario.cpf, "eh_barbeiro": True}
        )

def test_multiplos_pagamentos_agendamento_service(session_maker, mock_criar_usuarios_e_agendamento):
    # Criar dados necessários
    cliente, barbeiro, agendamento = mock_criar_usuarios_e_agendamento
    
    # Criar primeiro pagamento
    criar_pagamento(
        uow=UnidadeDeTrabalho(session_maker),
        valor=30.0,
        metodo=MetodoPagamento.PIX,
        agendamento_id=agendamento.id,
        solicitante={"cpf": barbeiro.usuario.cpf, "eh_barbeiro": True}
    )
    
    # Criar segundo pagamento para o mesmo agendamento
    criar_pagamento(
        uow=UnidadeDeTrabalho(session_maker),
        valor=20.0,
        metodo=MetodoPagamento.CARTAO,
        agendamento_id=agendamento.id,
        solicitante={"cpf": barbeiro.usuario.cpf, "eh_barbeiro": True}
    )
    
    # Verificar que o método consultar_por_agendamento retorna apenas o primeiro pagamento encontrado
    with UnidadeDeTrabalho(session_maker) as uow:
        pagamento = uow.pagamentos.consultar_por_agendamento(agendamento.id)
        assert pagamento is not None
        # O método retorna o primeiro pagamento encontrado (pode ser qualquer um dos dois)
        assert pagamento.valor in [30.0, 20.0]
        assert pagamento.metodo in [MetodoPagamento.PIX, MetodoPagamento.CARTAO] 