import pytest
from src.domain.models import HorarioIndisponivel
from src.domain.exceptions import *
from src.service.services.horario_indisponivel import (
    criar_horario_indisponivel,
    consultar_horario_indisponivel,
    consultar_horario_indisponivel_por_horario,
    alterar_horario_indisponivel,
    excluir_horario_indisponivel,
)
from src.service.unit_of_work import UnidadeDeTrabalho
from tests.mock import *
from datetime import datetime

def test_criar_horario_indisponivel_service(
    session_maker,
    mock_criar_barbeiro,
):
    # HorarioIndisponivelInvalido: O horário de inicio tem que ser menor que o horário de fim.
    with pytest.raises(HorarioIndisponivelInvalido):
        criar_horario_indisponivel(
            uow=UnidadeDeTrabalho(session_maker),
            barbeiro_cpf="25811756054",
            horario_inicio=datetime(2025, 6, 10, 10),
            horario_fim=datetime(2025, 6, 10, 9),
            justificativa="Horário Inválido",
        )

    # BarbeiroNaoEncontrado: O cpf informado não pertencem a um barbeiro do sistema.
    with pytest.raises(BarbeiroNaoEncontrado):
        criar_horario_indisponivel(
            uow=UnidadeDeTrabalho(session_maker),
            barbeiro_cpf="12345678900",
            horario_inicio=datetime(2025, 6, 10, 10),
            horario_fim=datetime(2025, 6, 10, 12),
            justificativa="Horário Inválido"
        )

    # Criar Jornada
    criar_horario_indisponivel(
        uow=UnidadeDeTrabalho(session_maker),
        barbeiro_cpf="25811756054",
        horario_inicio=datetime(2025, 6, 10, 12),
        horario_fim=datetime(2025, 6, 10, 17),
        justificativa="Aniversário"
    )

    with UnidadeDeTrabalho(session_maker) as uow:
        horario_indisponivel = uow.horarios_indisponiveis.consultar_por_barbeiro(cpf="25811756054")
        assert len(horario_indisponivel) == 1
        assert horario_indisponivel[0].horario_inicio == datetime(2025, 6, 10, 12)
        assert horario_indisponivel[0].horario_fim == datetime(2025, 6, 10, 17)
        assert horario_indisponivel[0].justificativa == "Aniversário"
        assert horario_indisponivel[0].barbeiro.cpf == "25811756054"

def test_consultar_horario_indisponivel_service(
    session_maker,
    mock_criar_horarios_indisponiveis,
):
    # Consultar horário já existente
    horario_indisponivel = consultar_horario_indisponivel(
        uow=UnidadeDeTrabalho(session_maker),
        id='horario-001',
    )

    # Verificando informação
    horario_1 = (datetime(2025, 6, 10), datetime(2025, 6, 11))
    assert horario_indisponivel == {
        'id':'horario-001',
        'horario_inicio': horario_1[0].isoformat(),
        'horario_fim': horario_1[1].isoformat(),
        'justificativa':'Indisponível hoje',
        'barbeiro':{
            'cpf':'25811756054',
            'nome':'Barbeiro 01',
            'senha':'123',
            'email':'barbeiro1@teste.com',
            'telefone':None,
            'eh_barbeiro':True,
        },
    }

    # Consultar horário inexistente
    horario_inexistente = consultar_horario_indisponivel(
        uow=UnidadeDeTrabalho(session_maker),
        id='horario-999',
    )
    assert horario_inexistente == {}

def test_consultar_horario_indisponivel_por_horario_service(
    session_maker,
    mock_criar_horarios_indisponiveis,
):
    # Consultando horários disponíveis em uma faixa
    horarios_indisponiveis = consultar_horario_indisponivel_por_horario(
        uow=UnidadeDeTrabalho(session_maker),
        horario_inicio=datetime(2025, 1, 1),
        horario_fim=datetime(2025, 12, 31),
    )

    # Verificando informação
    horario_1 = (datetime(2025, 6, 10), datetime(2025, 6, 11))
    assert len(horarios_indisponiveis) == 3
    assert horarios_indisponiveis[0] == {
        'id':'horario-001',
        'horario_inicio': horario_1[0].isoformat(),
        'horario_fim': horario_1[1].isoformat(),
        'justificativa':'Indisponível hoje',
        'barbeiro':{
            'cpf':'25811756054',
            'nome':'Barbeiro 01',
            'senha':'123',
            'email':'barbeiro1@teste.com',
            'telefone':None,
            'eh_barbeiro':True,
        },
    }

    # Consultando horários inexistentes
    horarios_inexistentes = consultar_horario_indisponivel_por_horario(
        uow=UnidadeDeTrabalho(session_maker),
        horario_inicio=datetime(2023, 1, 1),
        horario_fim=datetime(2024, 12, 31),
    )
    assert horarios_inexistentes == []

def test_editar_horario_indisponivel_service(
    session_maker,
    mock_criar_horarios_indisponiveis,
):
    # Alterar horário indisponível com sucesso
    alterar_horario_indisponivel(
        uow=UnidadeDeTrabalho(session_maker),
        id='horario-001',
        horario_inicio=datetime(2025, 6, 9),
        horario_fim=datetime(2025, 6, 10),
        justificativa='Aniversário adiantado',
    )

    # Verificando alteração
    with UnidadeDeTrabalho(session_maker) as uow:
        horario_encontrado = uow.horarios_indisponiveis.consultar(id='horario-001')
        assert horario_encontrado.horario_inicio == datetime(2025, 6, 9)
        assert horario_encontrado.horario_fim == datetime(2025, 6, 10)
        assert horario_encontrado.justificativa == 'Aniversário adiantado'

    # HorarioIndisponivelInvalido: O horário de inicio tem que ser menor que o horário de fim.
    with pytest.raises(HorarioIndisponivelInvalido):
        alterar_horario_indisponivel(
            uow=UnidadeDeTrabalho(session_maker),
            id='horario-001',
            horario_inicio=datetime(2025, 6, 9),
            horario_fim=datetime(2025, 6, 8),
            justificativa='Horário Inválido'
        )

    # HorarioIndisponivelNaoEncontrado: O horario indisponivel especificado não foi encontrado.
    with pytest.raises(HorarioIndisponivelNaoEncontrado):
        alterar_horario_indisponivel(
            uow=UnidadeDeTrabalho(session_maker),
            id='horario-999',
            horario_inicio=datetime(2025, 6, 10),
            horario_fim=datetime(2025, 6, 12),
            justificativa='Horário Não encontrado'
        )

def excluir_horario_indisponivel_service(
    session_maker,
    mock_criar_horarios_indisponiveis,
):
    # Horário excluido com sucesso
    excluir_horario_indisponivel(
        uow=UnidadeDeTrabalho(session_maker),
        id='horario-001',
    )

    # Verificando exclusão
    with UnidadeDeTrabalho(session_maker) as uow:
        horario_encontrado = uow.horarios_indisponiveis.consultar(id='horario-001')
        assert horario_encontrado == None
  
    # HorarioIndisponivelNaoEncontrado: O horario indisponivel especificado não foi encontrado.
    with pytest.raises(HorarioIndisponivelNaoEncontrado):
        excluir_horario_indisponivel(
            uow=UnidadeDeTrabalho(session_maker),
            id='horario-999',
        )