import pytest
from src.domain.models import Usuario, Servico
from src.adapters.repositories import *
from tests.mock import *

def test_usuario_repository(session):
    # Criando modelo de usuário
    usuario1 = Usuario(
        cpf="123.456.789-00",
        nome="Usuário 01",
        senha="123",
        email="usuario1@teste.com"
    )

    usuario2 = Usuario(
        cpf="987.654.321-00",
        nome="Usuário 02",
        senha="321",
        email="usuario2@teste.com"
    )

    # Criando usuário no banco de dados
    usuario_repo = UsuarioRepository(session=session)
    usuario_repo.adicionar(usuario1)
    usuario_repo.adicionar(usuario2)

    # Procurando e assegurando que são iguais
    usuario_deletado = usuario_repo.consultar_por_cpf(cpf=usuario1.cpf)
    assert usuario1 == usuario_deletado

    # Procurando todos os clientes
    usuarios_encontrados = usuario_repo.retornar_clientes()
    assert usuarios_encontrados == [usuario1, usuario2]

    # Removendo usuário no banco de dados
    usuario_repo.remover(usuario1.cpf)
    usuario_deletado = usuario_repo.consultar_por_cpf(cpf=usuario1.cpf)
    assert usuario_deletado == None

def test_servico_repository(session):
    # Criando serviços
    servico_barba = Servico(
        nome="Cortar Barba",
        descricao="Corte de Barba Simples",
        preco=15,
        duracao=30,
    )

    servico_cabelo = Servico(
        nome="Cortar Cabelo",
        descricao="Corte curto simples",
        preco=20,
        duracao=30,
    )

    servico_sobrancelha = Servico(
        nome="Fazer sobrancelhas",
        descricao="Tirar excesso de sobrancelhas",
        preco=40,
        duracao=15,
    )

    print(servico_barba.id, servico_cabelo.id, servico_sobrancelha.id)

    # Criando serviços no banco de dados
    servico_repo = ServicoRepository(session=session)
    servico_repo.adicionar(servico_barba)
    servico_repo.adicionar(servico_cabelo)
    servico_repo.adicionar(servico_sobrancelha)

    # Procurando pelos serviços adicionados
    servicos_encontrados = servico_repo.retornar_servicos()
    assert servicos_encontrados == [servico_barba, servico_cabelo, servico_sobrancelha]

    # Pesquisando por um serviço específico
    servico_encontrado = servico_repo.consultar_por_id(id=servico_barba.id)
    assert servico_encontrado == servico_barba

    # Pesquisnado por serviços parecidos
    servicos_parecidos = servico_repo.consultar_por_nome(nome="Cortar")
    assert servicos_parecidos == [servico_barba, servico_cabelo]

def test_jornada_repository(session, mock_jornada_teste):
    # Criando Barbeiro
    barbeiro = Usuario(
        cpf="987.654.321-00",
        nome="Barbeiro Teste",
        email="barbeiro@teste.com",
        senha="senha_barbeiro123",
        telefone="(84) 98765-4321",
        eh_barbeiro=True,
    )

    # Criando Jornada de Segunda a Sexta
    jornadas = mock_jornada_teste(barbeiro)

    # Adicionando jornada
    jornada_repo = JornadaRepository(session=session)
    for jornada in jornadas:
        jornada_repo.adicionar(jornada=jornada)

    # Procurar jornada por ID
    for jornada in jornadas:
        jornada_encontrada = jornada_repo.consultar_por_id(id=jornada.id)
        assert jornada_encontrada == jornada

    # Comparar todas as jornadas
    jornadas_encontradas = jornada_repo.consultar_por_barbeiro_e_vigente(cpf=barbeiro.cpf)
    assert jornadas_encontradas == jornadas

def test_horario_indisponivel_repostiroy(session, mock_dia_indisponivel_teste):
    # Criando Barbeiro
    barbeiro = Usuario(
        cpf="987.654.321-00",
        nome="Barbeiro Teste",
        email="barbeiro@teste.com",
        senha="senha_barbeiro123",
        telefone="(84) 98765-4321",
        eh_barbeiro=True,
    )

    # Dia indisponível
    dia_indisponivel = mock_dia_indisponivel_teste(
        barbeiro=barbeiro,
        horario_inicio=datetime(2025, 5, 29, 10, 0),
        horario_fim=datetime(2025, 5, 29, 10, 30),    
    )

    # Adicionando dias indisponíveis
    horario_indisponivel_repo = HorarioIndisponivelRepository(session=session)

    # Adicionando horário indisponível
    horario_indisponivel_repo.adicionar(dia_indisponivel)

    # Procurando dia por id
    horario_indisponivel_encontrado = horario_indisponivel_repo.consultar_por_id(dia_indisponivel.id)
    assert horario_indisponivel_encontrado == dia_indisponivel

    # Procurando por barbeiro
    horarios_indisponiveis_barbeiro = horario_indisponivel_repo.consultar_por_barbeiro(barbeiro.cpf)
    assert horarios_indisponiveis_barbeiro == [dia_indisponivel]

    # Procurando por horario
    horarios_indisponiveis_no_dia = horario_indisponivel_repo.consultar_por_horario(
        horarios=(
            datetime(2025, 5, 29, 10, 15),
            datetime(2025, 5, 29, 10, 30),
        )
    )
    assert horarios_indisponiveis_no_dia == [dia_indisponivel]

def test_barbeiro_repository(session, mock_barbeiro_teste):
    # Criando barbeiro
    barbeiro = mock_barbeiro_teste

    # Criando repositório
    barbeiro_repo = BarbeiroRepository(session=session)

    # Adicionando barbeiro
    barbeiro_repo.usuario_repo.adicionar(barbeiro.usuario)
    for jornada in barbeiro.jornada_de_trabalho:
        barbeiro_repo.jornada_repo.adicionar(jornada)
    for horario in barbeiro.horarios_indisponiveis:
        barbeiro_repo.horario_indisponivel_repo.adicionar(horario)

    # Procurando por barbeiro
    barbeiro_encontrado = barbeiro_repo.consultar_por_cpf(barbeiro.usuario.cpf)
    assert barbeiro_encontrado == barbeiro

    # Procurando por barbeiros
    barbeiros_encontrados = barbeiro_repo.lista_de_barbeiros()
    assert barbeiros_encontrados == [barbeiro]

def test_agendamento_repository(
    session,
    mock_usuario_teste,
    mock_barbeiro_teste,
    mock_servicos_teste,
):
    # Criando cliente, barbeiro e serviços 
    usuario = mock_usuario_teste
    barbeiro = mock_barbeiro_teste
    servicos = mock_servicos_teste

    # Repositórios
    usuario_repo = UsuarioRepository(session=session)
    servico_repo = ServicoRepository(session=session)
    barbeiro_repo = BarbeiroRepository(session=session)

    # Adicionando cliente
    usuario_repo.adicionar(usuario)

    # Adicionando babeiros, jornadas e horários
    barbeiro_repo.usuario_repo.adicionar(barbeiro.usuario)
    for jornada in barbeiro.jornada_de_trabalho:
        barbeiro_repo.jornada_repo.adicionar(jornada)
    for horario in barbeiro.horarios_indisponiveis:
        barbeiro_repo.horario_indisponivel_repo.adicionar(horario)

    # Adicionando serviços
    for servico in servicos:
        servico_repo.adicionar(servico=servico)
        
    # Criando horários
    horario = {
        "inicio":datetime(2025, 5, 27, 10, 0), 
        "fim":datetime(2025, 5, 27, 11, 40)
    }

    # Criando agendamento
    agendamento = criar_agendamento(usuario, barbeiro, servicos, tuple(horario.values()))

    # Criando repositório de agendamento
    agendamento_repo = AgendamentoRepository(session=session)
    agendamento_repo.adicionar(agendamento)

    # Procurando agendamento
    agendamento_encontrado = agendamento_repo.consultar_por_id(id=agendamento.id)
    assert agendamento_encontrado == agendamento

    # Procurando agendamentos
    agendamentos_encontrados = agendamento_repo.retornar_agendamentos()
    assert agendamentos_encontrados == [agendamento]

    # Procurando agendamento por horário
    agendamento_horario = agendamento_repo.consultar_por_horario(horarios=(
        datetime(2025, 5, 27, 7),
        datetime(2025, 5, 27, 17),
    ))
    assert agendamento_horario == [agendamento]

def test_pagamento_repository(
    session,
    mock_usuario_teste,
    mock_barbeiro_teste,
    mock_servicos_teste,
):
    # Criando cliente, barbeiro e serviços 
    usuario = mock_usuario_teste
    barbeiro = mock_barbeiro_teste
    servicos = mock_servicos_teste

    # Repositórios
    usuario_repo = UsuarioRepository(session=session)
    servico_repo = ServicoRepository(session=session)
    barbeiro_repo = BarbeiroRepository(session=session)

    # Adicionando cliente
    usuario_repo.adicionar(usuario)

    # Adicionando babeiros, jornadas e horários
    barbeiro_repo.usuario_repo.adicionar(barbeiro.usuario)
    for jornada in barbeiro.jornada_de_trabalho:
        barbeiro_repo.jornada_repo.adicionar(jornada)
    for horario in barbeiro.horarios_indisponiveis:
        barbeiro_repo.horario_indisponivel_repo.adicionar(horario)

    # Adicionando serviços
    for servico in servicos:
        servico_repo.adicionar(servico=servico)
        
    # Criando horários
    horario = {
        "inicio":datetime(2025, 5, 27, 10, 0), 
        "fim":datetime(2025, 5, 27, 11, 40)
    }

    # Criando agendamento
    agendamento = criar_agendamento(usuario, barbeiro, servicos, tuple(horario.values()))

    # Criando repositório de agendamento
    agendamento_repo = AgendamentoRepository(session=session)
    agendamento_repo.adicionar(agendamento)

    # Criando pagamento
    pagamento = Pagamento(
        valor=sum([servico.preco for servico in agendamento.servicos]),
        data=datetime.now(),
        metodo=MetodoPagamento.PIX,
        agendamento=agendamento
    )

    # Criando repositório de pagamento
    pagamento_repo = PagamentoRepository(session=session)
    pagamento_repo.adicionar(pagamento)

    # Procurando pagamento
    pagamento_encontrado = pagamento_repo.consultar_por_id(pagamento.id)
    assert pagamento_encontrado == pagamento

    # Procurando pagamento de agendamento 
    pagamento_de_agendamento = pagamento_repo.consultar_por_agendamento(agendamento.id)
    assert pagamento_de_agendamento == pagamento

    # Procurando pagamentos do cliente
    pagamentos_do_cliente = pagamento_repo.retornar_pagamentos_de_cliente(usuario.cpf)
    assert pagamentos_do_cliente == [pagamento]