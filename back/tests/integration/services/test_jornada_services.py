import pytest
from src.domain.models import Barbeiro, Jornada
from src.domain.exceptions import *
from src.service.services.barbeiro import (
    criar_jornada,
    consultar_jornada,
    consultar_jornada_de_trabalho,
    alterar_ativacao_de_jornada,
    excluir_jornada,
)
from src.service.unit_of_work import UnidadeDeTrabalho
from tests.mock import *
from datetime import time

def test_criar_jornada_service(
    session_maker, 
    mock_criar_barbeiro,
):
    # HorarioDaJornadaInvalido: "O horário de início é maior que o horário de fim." 
    with pytest.raises(HorarioDaJornadaInvalido):
        criar_jornada(
            uow=UnidadeDeTrabalho(session_maker),
            barbeiro_cpf="25811756054",
            dia_da_semana="Segunda",
            horario_inicio=time(hour=17),
            horario_fim=time(hour=7),
        )

    # HorarioDaJornadaInvalido: "Caso haja uma pausa, é necessário ter um retorno. O inverso também." 
    with pytest.raises(HorarioDaJornadaInvalido):
        criar_jornada(
            uow=UnidadeDeTrabalho(session_maker),
            barbeiro_cpf="25811756054",
            dia_da_semana="Segunda",
            horario_inicio=time(hour=7),
            horario_pausa=time(hour=12),
            horario_fim=time(hour=17),
        )
    with pytest.raises(HorarioDaJornadaInvalido):
        criar_jornada(
            uow=UnidadeDeTrabalho(session_maker),
            barbeiro_cpf="25811756054",
            dia_da_semana="Segunda",
            horario_inicio=time(hour=7),
            horario_retorno=time(hour=14),
            horario_fim=time(hour=17),
        )
  
    # HorarioDaJornadaInvalido: "O horário de pausa não pode ser maior que o horário de retorno." 
    with pytest.raises(HorarioDaJornadaInvalido):
        criar_jornada(
            uow=UnidadeDeTrabalho(session_maker),
            barbeiro_cpf="25811756054",
            dia_da_semana="Segunda",
            horario_inicio=time(hour=7),
            horario_pausa=time(hour=14),
            horario_retorno=time(hour=12),
            horario_fim=time(hour=17),
        )
    
    # HorarioDaJornadaInvalido: "O horário de pausa/retorno não deve estar fora da faixa do horário de início e fim." 
    with pytest.raises(HorarioDaJornadaInvalido):
        criar_jornada(
            uow=UnidadeDeTrabalho(session_maker),
            barbeiro_cpf="25811756054",
            dia_da_semana="Segunda",
            horario_inicio=time(hour=7),
            horario_pausa=time(hour=6),
            horario_retorno=time(hour=18),
            horario_fim=time(hour=17),
        )
    with pytest.raises(HorarioDaJornadaInvalido):
        criar_jornada(
            uow=UnidadeDeTrabalho(session_maker),
            barbeiro_cpf="25811756054",
            dia_da_semana="Segunda",
            horario_inicio=time(hour=7),
            horario_pausa=time(hour=6),
            horario_retorno=time(hour=6,minute=59),
            horario_fim=time(hour=17),
        )

    # DiaDaSemanaInvalido: "O dia da semana fornecido não condiz com nenhum valor salvo. Tente: Segunda, Terça, Quarta, Quinta, Sexta, Sábado ou Domingo."
    with pytest.raises(DiaDaSemanaInvalido):
        criar_jornada(
            uow=UnidadeDeTrabalho(session_maker),
            barbeiro_cpf="25811756054",
            dia_da_semana="segunda-feira",
            horario_inicio=time(hour=7),
            horario_pausa=time(hour=12),
            horario_retorno=time(hour=14),
            horario_fim=time(hour=17),
        )

    # BarbeiroNaoEncontrado: "Não foi encontrado nenhum barbeiro com esse identificador."
    with pytest.raises(BarbeiroNaoEncontrado):
        criar_jornada(
            uow=UnidadeDeTrabalho(session_maker),
            barbeiro_cpf="1234567890",
            dia_da_semana="Segunda",
            horario_inicio=time(hour=7),
            horario_pausa=time(hour=12),
            horario_retorno=time(hour=14),
            horario_fim=time(hour=17),
        )


    # Criar jornada com pausa e retorno
    criar_jornada(
        uow=UnidadeDeTrabalho(session_maker),
        barbeiro_cpf="25811756054",
        dia_da_semana="Segunda",
        horario_inicio=time(hour=7),
        horario_pausa=time(hour=12),
        horario_retorno=time(hour=14),
        horario_fim=time(hour=17),
    )

    # JornadaJaExistenteNoMesmoDia: "Já existe uma jornada para esse barbeiro no mesmo dia."
    with pytest.raises(JornadaJaExistenteNoMesmoDia):
        criar_jornada(
            uow=UnidadeDeTrabalho(session_maker),
            barbeiro_cpf="25811756054",
            dia_da_semana="Segunda",
            horario_inicio=time(hour=7),
            horario_pausa=time(hour=12),
            horario_retorno=time(hour=14),
            horario_fim=time(hour=17),
        )

    # Criar jornada sem pausa e retorno
    criar_jornada(
        uow=UnidadeDeTrabalho(session_maker),
        barbeiro_cpf="25811756054",
        dia_da_semana="Domingo",
        horario_inicio=time(hour=7),
        horario_fim=time(hour=10),
    )

    with UnidadeDeTrabalho(session_maker) as uow:
        jornadas = uow.jornadas.listar_jornada_de_barbeiro(cpf="25811756054")
        assert len(jornadas) == 2
        # Segunda 
        assert jornadas[0].barbeiro.cpf == "25811756054"
        assert jornadas[0].dia_da_semana == DiaDaSemana.SEGUNDA
        assert jornadas[0].horario_inicio == time(hour=7)
        assert jornadas[0].horario_pausa == time(hour=12)
        assert jornadas[0].horario_retorno == time(hour=14)
        assert jornadas[0].horario_fim == time(hour=17)
        # Domingo
        assert jornadas[1].barbeiro.cpf == "25811756054"
        assert jornadas[1].dia_da_semana == DiaDaSemana.DOMINGO
        assert jornadas[1].horario_inicio == time(hour=7)
        assert jornadas[1].horario_fim == time(hour=10)

def test_consultar_jornada_service(
    session_maker,
    mock_criar_jornada_de_trabalho,
):
    # Consultar jornada existente
    jornada = consultar_jornada(
        uow=UnidadeDeTrabalho(session_maker),
        id="jornada-001",
    )
    assert jornada == {
        'id':'jornada-001',
        'ativa': True,
        'barbeiro':{
            'cpf':'25811756054',
            'nome':'Barbeiro 01',
            'senha':'123',
            'email':'barbeiro1@teste.com',
            'telefone':None,
            'eh_barbeiro':True,
        },
        'dia_da_semana':"Segunda",
        'horario_inicio':time(hour=8),
        'horario_fim':time(hour=12),
        'horario_pausa':None,
        'horario_retorno':None,
    }

    # Consultar jornada inexistentes
    jornada = consultar_jornada(
        uow=UnidadeDeTrabalho(session_maker),
        id="saofsafsfsafsf",
    )
    assert jornada == {}

def test_consultar_jornada_de_trabalho_service(
    session_maker,
    mock_criar_jornada_de_trabalho,
):
    # Consultar jornada de barbeiro
    jornada_de_trabalho = consultar_jornada_de_trabalho(
        uow=UnidadeDeTrabalho(session_maker),
        barbeiro_cpf='25811756054'
    )
    assert len(jornada_de_trabalho) == 7
    assert jornada_de_trabalho[0] == {
        'id':'jornada-001',
        'ativa': True,
        'barbeiro':{
            'cpf':'25811756054',
            'nome':'Barbeiro 01',
            'senha':'123',
            'email':'barbeiro1@teste.com',
            'telefone':None,
            'eh_barbeiro':True,
        },
        'dia_da_semana':"Segunda",
        'horario_inicio':time(hour=8),
        'horario_fim':time(hour=12),
        'horario_pausa':None,
        'horario_retorno':None,
    }

    # Consultar jornada de um barbeiro inexistente
    jornada_de_trabalho = consultar_jornada_de_trabalho(
        uow=UnidadeDeTrabalho(session_maker),
        barbeiro_cpf='1234567890'
    )
    assert jornada_de_trabalho == []

def test_alterar_ativacao_de_jornada_service(
    session_maker,
    mock_criar_jornada_de_trabalho,
):
    # Alterando ativação de jornada com sucesso
    alterar_ativacao_de_jornada(
        uow=UnidadeDeTrabalho(session_maker),
        id='jornada-001',
    )

    # Verificando
    with UnidadeDeTrabalho(session_maker) as uow:
        jornada = uow.jornadas.consultar('jornada-001')
        assert jornada.ativa == False
    
        # Adicionando jornada no dia da anterior
        barbeiro = uow.usuarios.consultar(cpf='25811756054')
        uow.jornadas.adicionar(
            Jornada(
                barbeiro=barbeiro,
                dia_da_semana=DiaDaSemana.SEGUNDA,
                horario_inicio=time(hour=7),
                horario_fim=time(hour=11),
            )
        )
        uow.commit()

    # JornadaJaExistenteNoMesmoDia: Se essa jornada for ativada, existirão duas jornadas no mesmo dia. Jornada: {jornada_id}
    with pytest.raises(JornadaJaExistenteNoMesmoDia):
        alterar_ativacao_de_jornada(
            uow=UnidadeDeTrabalho(session_maker),
            id='jornada-001',
        )

    # JornadaNaoEncontrada: A jornada especificada não foi encontrada
    with pytest.raises(JornadaNaoEncontrada):
        alterar_ativacao_de_jornada(
            uow=UnidadeDeTrabalho(session_maker),
            id='jornada-999',
        )

def test_excluir_jornada_service(
    session_maker,
    mock_criar_jornada_de_trabalho,
):
    # Verificando existencia de jornada antes de exclusão
    with UnidadeDeTrabalho(session_maker) as uow:
        jornada_excluida = uow.jornadas.consultar('jornada-001')
        assert jornada_excluida is not None    

    # JornadaNaoEncontrada: A jornada especificada não foi encontrada
    with pytest.raises(JornadaNaoEncontrada):
        excluir_jornada(
            uow=UnidadeDeTrabalho(session_maker),
            id='jornada-999',
        )

    # Excluindo jornada existente
    excluir_jornada(
        uow=UnidadeDeTrabalho(session_maker),
        id='jornada-001',
    )

    # Verificando se exclusão obteve sucesso
    with UnidadeDeTrabalho(session_maker) as uow:
        jornada_excluida = uow.jornadas.consultar('jornada-001')
        assert jornada_excluida is None