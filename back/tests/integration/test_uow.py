from tests.mock import *
from src.service.unit_of_work import UnidadeDeTrabalho
import pytest

def test_uow_usuario(session_maker):
    usuario = Usuario(
        cpf="123.456.789-00",
        nome="Usuário 01",
        senha="123",
        email="usuario1@teste.com",
        eh_barbeiro=False
    )
    
    # Teste de adição
    with UnidadeDeTrabalho(session_maker) as uow:
        uow.usuarios.adicionar(usuario)
        uow.commit()
    
    # Teste de consulta
    with UnidadeDeTrabalho(session_maker) as uow:
        usuario_encontrado = uow.usuarios.consultar("123.456.789-00")
        assert usuario_encontrado.cpf == usuario.cpf
        assert usuario_encontrado.nome == usuario.nome
    
    # Teste de remoção
    with UnidadeDeTrabalho(session_maker) as uow:
        uow.usuarios.remover("123.456.789-00")
        uow.commit()
        
        usuario_encontrado = uow.usuarios.consultar("123.456.789-00")
        assert usuario_encontrado is None

def test_uow_servico(session_maker):
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

    servicos = [servico_barba, servico_cabelo, servico_sobrancelha]
    
    # Teste de adição
    with UnidadeDeTrabalho(session_maker) as uow:
        uow.servicos.adicionar(servico_barba)
        uow.servicos.adicionar(servico_cabelo)
        uow.servicos.adicionar(servico_sobrancelha)
        uow.commit()
    
    # Teste de consulta
    with UnidadeDeTrabalho(session_maker) as uow:
        servicos_encontrados = uow.servicos.listar()
        assert len(servicos_encontrados) > 0
        assert servicos_encontrados == servicos

        servico_barba_encontrado = uow.servicos.consultar_por_nome("Cortar Barba")[0]
        assert servico_barba_encontrado == servicos[0]
    
    # Teste de remoção
    with UnidadeDeTrabalho(session_maker) as uow:
        servico_barba_encontrado = uow.servicos.consultar_por_nome("Cortar Barba")[0]
        uow.servicos.remover(servico_barba_encontrado.id)
        uow.commit()
        
        servico_barba_encontrado = uow.servicos.consultar_por_nome("Cortar Barba")
        assert servico_barba_encontrado == []

def test_uow_jornada(
    session_maker,
    mock_jornada_teste,
):
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

    # Teste de adição
    with UnidadeDeTrabalho(session_maker) as uow:
        for jornada in jornadas:
            uow.jornadas.adicionar(jornada)
        uow.commit()

    # Teste de consulta
    with UnidadeDeTrabalho(session_maker) as uow:
        jornadas_do_barbeiro = uow.jornadas.listar_jornada_de_barbeiro(barbeiro.cpf)
        assert len(jornadas_do_barbeiro) == len(jornadas)
        assert jornadas_do_barbeiro == jornadas

    # Teste de remoção
    with UnidadeDeTrabalho(session_maker) as uow:
        uow.jornadas.remover(jornadas[0].id)
        uow.commit()

        jornada_segunda = uow.jornadas.consultar(jornadas[0].id)
        assert jornada_segunda is None

        jornadas_do_barbeiro = uow.jornadas.listar_jornada_de_barbeiro(barbeiro.cpf)
        assert len(jornadas_do_barbeiro) == len(jornadas)-1
        assert jornadas_do_barbeiro != jornadas

def test_uow_horario_indisponivel(
    session_maker, 
    mock_dia_indisponivel_teste
):
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

    # Teste de adição
    with UnidadeDeTrabalho(session_maker) as uow:
        uow.horarios_indisponiveis.adicionar(dia_indisponivel)
        uow.commit()

    # Teste de consulta
    with UnidadeDeTrabalho(session_maker) as uow:
        horario_indisponivel = uow.horarios_indisponiveis.consultar(dia_indisponivel.id)
        assert horario_indisponivel == dia_indisponivel

    # Teste de remoção
    with UnidadeDeTrabalho(session_maker) as uow:
        uow.horarios_indisponiveis.remover(dia_indisponivel.id)
        uow.commit()

        horario_indisponivel = uow.horarios_indisponiveis.consultar(dia_indisponivel.id)
        assert horario_indisponivel is None

def test_uow_barbeiro(
    session_maker,
    mock_barbeiro_teste,
):
    barbeiro = mock_barbeiro_teste

    # Teste de adição
    with UnidadeDeTrabalho(session_maker) as uow:
        # Criando usuário do barbeiro
        uow.usuarios.adicionar(barbeiro.usuario)

        # Criando jornada do barbeiro
        for jornada in barbeiro.jornada_de_trabalho:
            uow.jornadas.adicionar(jornada)

        # Criando horários indisponíveis do barbeiro
        for horario_indisponivel in barbeiro.horarios_indisponiveis:
            uow.horarios_indisponiveis.adicionar(horario_indisponivel)

        uow.commit()

    # Teste de consulta
    with UnidadeDeTrabalho(session_maker) as uow:
        barbeiro_encontrado = uow.barbeiros.consultar(barbeiro.usuario.cpf)
        assert barbeiro_encontrado == barbeiro

    # Teste de remoção
    with UnidadeDeTrabalho(session_maker) as uow:
        uow.barbeiros.usuario_repo.remover(barbeiro.usuario.cpf)
        uow.commit()

        barbeiro_encontrado = uow.barbeiros.consultar(barbeiro.usuario.cpf)
        assert barbeiro_encontrado.usuario is None
        assert barbeiro_encontrado.jornada_de_trabalho == []
        assert barbeiro_encontrado.horarios_indisponiveis == []

def test_uow_agendamento(
    session_maker,
    mock_usuario_teste,
    mock_barbeiro_teste,
    mock_servicos_teste,
):
    # Criando cliente, barbeiro e serviços 
    usuario = mock_usuario_teste
    barbeiro = mock_barbeiro_teste
    servicos = mock_servicos_teste
   
    # Criando horários
    horario = {
        "inicio":datetime(2025, 5, 27, 8, 0), 
        "fim":datetime(2025, 5, 27, 10, 40)
    }

    # Criando agendamento
    agendamento = criar_agendamento(usuario, barbeiro, servicos, tuple(horario.values()))

    # Teste de adição
    with UnidadeDeTrabalho(session_maker) as uow:
        # Criando usuários
        uow.usuarios.adicionar(barbeiro.usuario)
        uow.usuarios.adicionar(usuario)

        # Criando serviços
        for servico in servicos:
            uow.servicos.adicionar(servico)

        # Criando jornada do barbeiro
        for jornada in barbeiro.jornada_de_trabalho:
            uow.jornadas.adicionar(jornada)

        # Criando horários indisponíveis do barbeiro
        for horario_indisponivel in barbeiro.horarios_indisponiveis:
            uow.horarios_indisponiveis.adicionar(horario_indisponivel)

        # Criando o agendamento
        uow.agendamentos.adicionar(agendamento)

        uow.commit()

    # Teste de consulta
    with UnidadeDeTrabalho(session_maker) as uow:
        agendamento_encontrado = uow.agendamentos.consultar(agendamento.id)

        assert agendamento_encontrado.barbeiro == agendamento.barbeiro
        assert agendamento_encontrado.cliente == agendamento.cliente
        assert agendamento_encontrado.horario_inicio == agendamento.horario_inicio
        assert agendamento_encontrado.horario_fim == agendamento.horario_fim
        assert set(agendamento_encontrado.servicos) == set(agendamento.servicos)

    # Teste de remoção
    with UnidadeDeTrabalho(session_maker) as uow:
        uow.agendamentos.remover(agendamento.id)
        uow.commit()

        agendamento_encontrado = uow.agendamentos.consultar(agendamento.id)
        assert agendamento_encontrado is None

def test_uow_pagamento(
    session_maker,
    mock_usuario_teste,
    mock_barbeiro_teste,
    mock_servicos_teste,
):
    # Criando cliente, barbeiro e serviços 
    usuario = mock_usuario_teste
    barbeiro = mock_barbeiro_teste
    servicos = mock_servicos_teste
   
    # Criando horários
    horario = {
        "inicio":datetime(2025, 5, 27, 8, 0), 
        "fim":datetime(2025, 5, 27, 10, 40)
    }

    # Criando agendamento
    agendamento = criar_agendamento(usuario, barbeiro, servicos, tuple(horario.values()))

    # Criando pagamento
    pagamento = Pagamento(
        valor=sum([servico.preco for servico in agendamento.servicos]),
        data=datetime.now(),
        metodo=MetodoPagamento.PIX,
        agendamento=agendamento
    )

    # Teste de adição
    with UnidadeDeTrabalho(session_maker) as uow:
        # Criando usuários
        uow.usuarios.adicionar(barbeiro.usuario)
        uow.usuarios.adicionar(usuario)

        # Criando serviços
        for servico in servicos:
            uow.servicos.adicionar(servico)

        # Criando jornada do barbeiro
        for jornada in barbeiro.jornada_de_trabalho:
            uow.jornadas.adicionar(jornada)

        # Criando horários indisponíveis do barbeiro
        for horario_indisponivel in barbeiro.horarios_indisponiveis:
            uow.horarios_indisponiveis.adicionar(horario_indisponivel)

        # Criando o agendamento
        uow.agendamentos.adicionar(agendamento)

        # Criando pagamento
        uow.pagamentos.adicionar(pagamento)

        uow.commit()

    # Teste de consulta
    with UnidadeDeTrabalho(session_maker) as uow:
        pagamento_encontrado = uow.pagamentos.consultar(pagamento.id)
        assert pagamento_encontrado == pagamento

    # Teste de remoção
    with UnidadeDeTrabalho(session_maker) as uow:
        uow.pagamentos.remover(pagamento.id)
        uow.commit()

        pagamento_encontrado = uow.pagamentos.consultar(pagamento.id)
        assert pagamento_encontrado is None

def test_uow_faz_rollback_se_nao_comitar(session_maker):
    usuario = Usuario(
        cpf="123.456.789-00",
        nome="Usuário 01",
        senha="123",
        email="usuario1@teste.com",
        eh_barbeiro=False
    )
    
    # Teste de adição sem commit
    with UnidadeDeTrabalho(session_maker) as uow:
        uow.usuarios.adicionar(usuario)
        
    with UnidadeDeTrabalho(session_maker) as uow:
        usuario_encontrado = uow.usuarios.consultar("123.456.789-00")
        assert usuario_encontrado == None

def test_uow_faz_rollback_em_erro(session_maker):
    class ExcecaoTeste(Exception):
        pass

    usuario = Usuario(
        cpf="123.456.789-00",
        nome="Usuário 01",
        senha="123",
        email="usuario1@teste.com",
        eh_barbeiro=False
    )

    with pytest.raises(ExcecaoTeste):
        with UnidadeDeTrabalho(session_maker) as uow:
            uow.usuarios.adicionar(usuario)
            raise ExcecaoTeste()
        
    with UnidadeDeTrabalho(session_maker) as uow:
        usuario_encontrado = uow.usuarios.consultar("123.456.789-00")
        assert usuario_encontrado == None
