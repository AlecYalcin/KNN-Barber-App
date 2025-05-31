import pytest
from datetime import datetime, date, time, timedelta
from src.domain.models import *

@pytest.fixture
def mock_usuario_teste():
    usuario = Usuario(
        cpf="123.456.789-00",
        nome="Usuário Teste",
        email="usuario@teste.com",
        senha="senha_segura123",
        telefone="(84) 91234-5678",
        eh_barbeiro=False,
    )
    yield usuario

@pytest.fixture
def mock_jornada_teste():
    def fazer_jornada(barbeiro: Usuario):
        "Segunda a Sexta das 7h00 até 11h00 e 13h00 até 17h00"
        jornadas = []
        for dia in [DiaDaSemana.SEGUNDA, DiaDaSemana.TERCA, DiaDaSemana.QUARTA, DiaDaSemana.QUINTA, DiaDaSemana.SEXTA]:
            jornada = Jornada(
                ativa=True,
                horario_inicio=time(7, 0),
                horario_pausa=time(11, 0),
                horario_retorno=time(13, 0),
                horario_fim=time(17, 0),
                dia_da_semana=dia,
                barbeiro=barbeiro,
            )
            jornadas.append(jornada)
        return jornadas
    yield fazer_jornada

@pytest.fixture
def mock_dia_indisponivel_teste():
    def fazer_dia_indisponivel(barbeiro: Usuario, horario_inicio: datetime, horario_fim: datetime):
        return HorarioIndisponivel(
            horario_inicio=horario_inicio,
            horario_fim=horario_fim,
            justificativa="Justificativa Teste",
            barbeiro=barbeiro
        )
    yield fazer_dia_indisponivel

@pytest.fixture
def mock_barbeiro_teste(
    mock_jornada_teste,
    mock_dia_indisponivel_teste,
):
    # CPF aleatório
    barbeiro = Usuario(
            cpf="987.654.321-00",
            nome="Barbeiro Teste",
            email="barbeiro@teste.com",
            senha="senha_barbeiro123",
            telefone="(84) 98765-4321",
            eh_barbeiro=True,
    )
    
    # Criando Jornada
    jornada = mock_jornada_teste(barbeiro)

    # Data atual (exemplo)
    dia_indisponivel = mock_dia_indisponivel_teste(
        barbeiro=barbeiro,
        horario_inicio=datetime(2025, 5, 29, 10, 0),
        horario_fim=datetime(2025, 5, 29, 10, 30),    
    )

    # Retornando agregado de barbeiro
    return Barbeiro(
        usuario=barbeiro,
        jornada_de_trabalho=jornada,
        horarios_indisponiveis=[dia_indisponivel],
    )

@pytest.fixture
def mock_servicos_teste():
    servico_corte = Servico(
        nome="Corte de Cabelo",
        descricao="Corte de cabelo masculino com finalização.",
        preco=30.0,
        duracao=30
    )

    servico_barba = Servico(
        nome="Barba",
        descricao="Aparar e modelar a barba com toalha quente.",
        preco=20.0,
        duracao=20
    )

    servico_pacote = Servico(
        nome="Corte + Barba",
        descricao="Pacote promocional: corte de cabelo e barba.",
        preco=45.0,
        duracao=50
    )

    return [servico_corte, servico_barba, servico_pacote]
