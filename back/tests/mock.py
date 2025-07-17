import pytest
from datetime import datetime, date, time, timedelta
from src.domain.models import *
from sqlalchemy import text
from uuid import uuid4
import json


@pytest.fixture
def usuario_base():
    def _usuario_base(
        cpf="92470179041",
        nome="Usuário Teste",
        email="usuario@teste.com",
        senha="senha_segura123",
        telefone="84912345678",
        eh_barbeiro=False,
    ) -> Usuario:
        return Usuario(
            cpf=cpf,
            nome=nome,
            email=email,
            senha=senha,
            telefone=telefone,
            eh_barbeiro=eh_barbeiro,
        )
    yield _usuario_base

@pytest.fixture
def criador_de_usuario(
    session, 
):
    def _criar_usuario(
        cpf="92470179041",
        nome="Usuário Teste",
        email="usuario@teste.com",
        senha="senha_segura123",
        telefone="84912345678",
        eh_barbeiro=False,  
    ) -> Usuario:
        session.execute(
            text(
                """
                INSERT INTO usuario
                (cpf, nome, email, senha, telefone, eh_barbeiro)
                VALUES
                (:cpf, :nome, :email, :senha, :telefone, :eh_barbeiro)
                """
            ),
            params={
                "cpf": cpf,
                "nome": nome,
                "email": email,
                "senha": senha,
                "telefone": telefone,
                "eh_barbeiro": eh_barbeiro,
            }
        )
        session.commit()

        usuario = Usuario(cpf, nome, email, senha, telefone, eh_barbeiro)
        return session.merge(usuario)
    yield _criar_usuario

@pytest.fixture
def mock_usuario_teste():
    usuario = Usuario(
        cpf="92470179041",
        nome="Usuário Teste",
        email="usuario@teste.com",
        senha="senha_segura123",
        telefone="84912345678",
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

@pytest.fixture
def mock_criar_usuario(session):
    session.execute(
        text(
            """
            INSERT INTO usuario (cpf, nome, senha, email) VALUES
            ('05705608020','Usuário 01','123','usuario1@teste.com'),
            ('56198304035','Usuário 02','123','usuario2@teste.com'),
            ('80990188000','Usuário 03','123','usuario3@teste.com')
            """
        )
    )
    session.commit()

@pytest.fixture
def mock_criar_barbeiro(session):
    session.execute(
        text(
            """
            INSERT INTO usuario (cpf, nome, senha, email, eh_barbeiro) VALUES
            ('25811756054','Barbeiro 01','123','barbeiro1@teste.com', TRUE),
            ('36311464004','Barbeiro 02','123','barbeiro2@teste.com', TRUE),
            ('09357654097','Barbeiro 03','123','barbeiro3@teste.com', TRUE)
            """
        )
    )
    session.commit()

@pytest.fixture
def mock_criar_servicos(session):
    def create_services_with_ids(ids: dict | None = None):
        if not ids:
            ids = {
                "id0": str(uuid4()),
                "id1": str(uuid4()),
                "id2": str(uuid4()),
            }

        session.execute(
            text(
                """
                INSERT INTO servico (id, nome, descricao, preco, duracao) VALUES
                (:id0,'Serviço 01','Serviço de Cavanhaque',20.00,15),
                (:id1,'Serviço 02','Serviço de Cabelo',10.00,30),
                (:id2,'Serviço 03','Serviço de Barba',15.00,45)
                """
            ),
            params=ids
        )    
        session.commit()
    yield create_services_with_ids

@pytest.fixture
def mock_criar_jornada_de_trabalho(session, mock_criar_barbeiro):
    session.execute(
        text(
            """
            INSERT into jornada (id, ativa, horario_inicio, horario_fim, horario_pausa, horario_retorno, dia_da_semana, barbeiro_cpf) VALUES
            ('jornada-001', TRUE, '08:00', '12:00', NULL    , NULL      , 'SEGUNDA' , '25811756054'),
            ('jornada-004', TRUE, '08:00', '12:00', NULL    , NULL      , 'TERCA'   , '25811756054'),
            ('jornada-007', TRUE, '08:00', '12:00', NULL    , NULL      , 'QUARTA'  , '25811756054'),
            ('jornada-010', TRUE, '08:00', '12:00', NULL    , NULL      , 'QUINTA'  , '25811756054'),
            ('jornada-013', TRUE, '08:00', '12:00', NULL    , NULL      , 'SEXTA'   , '25811756054'),
            ('jornada-016', TRUE, '09:00', '14:00', NULL    , NULL      , 'SABADO'  , '25811756054'),
            ('jornada-021', TRUE, '09:00', '13:00', NULL    , NULL      , 'DOMINGO' , '25811756054'),
            ('jornada-002', TRUE, '13:00', '17:00', NULL    , NULL      , 'SEGUNDA' , '36311464004'),
            ('jornada-005', TRUE, '13:00', '17:00', NULL    , NULL      , 'TERCA'   , '36311464004'),
            ('jornada-008', TRUE, '13:00', '17:00', NULL    , NULL      , 'QUARTA'  , '36311464004'),
            ('jornada-011', TRUE, '13:00', '17:00', NULL    , NULL      , 'QUINTA'  , '36311464004'),
            ('jornada-014', TRUE, '13:00', '17:00', NULL    , NULL      , 'SEXTA'   , '36311464004'),
            ('jornada-017', TRUE, '14:00', '19:00', NULL    , NULL      , 'SABADO'  , '36311464004'),
            ('jornada-020', TRUE, '11:00', '15:00', NULL    , NULL      , 'DOMINGO' , '36311464004'),
            ('jornada-003', TRUE, '09:00', '18:00', '12:00' , '13:00'   , 'SEGUNDA' , '09357654097'),
            ('jornada-006', TRUE, '09:00', '18:00', '12:00' , '13:00'   , 'TERCA'   , '09357654097'),
            ('jornada-009', TRUE, '09:00', '18:00', '12:00' , '13:00'   , 'QUARTA'  , '09357654097'),
            ('jornada-012', TRUE, '09:00', '18:00', '12:00' , '13:00'   , 'QUINTA'  , '09357654097'),
            ('jornada-015', TRUE, '09:00', '18:00', '12:00' , '13:00'   , 'SEXTA'   , '09357654097'),
            ('jornada-018', TRUE, '10:00', '16:00', '12:30' , '13:00'   , 'SABADO'  , '09357654097'),
            ('jornada-019', TRUE, '10:00', '14:00', NULL    , NULL      , 'DOMINGO' , '09357654097');
            """
        )
    )
    session.commit()


@pytest.fixture
def mock_criar_horarios_indisponiveis(session, mock_criar_barbeiro):
    cpf = '25811756054'
    horario_1 = (datetime(2025, 6, 10), datetime(2025, 6, 11))
    horario_2 = (datetime(2025, 7, 10), datetime(2025, 7, 15))
    horario_3 = (datetime(2025, 8, 1), datetime(2025, 8, 30))

    session.execute(
        text(
            """
            INSERT INTO horario_indisponivel(id, horario_inicio, horario_fim, justificativa, barbeiro_cpf) VALUES
            ('horario-001', :inicio1, :fim1, :just1, :cpf),
            ('horario-002', :inicio2, :fim2, :just2, :cpf),
            ('horario-003', :inicio3, :fim3, :just3, :cpf)
            """
        ),
        {
            "inicio1": horario_1[0].isoformat(sep=' '),
            "fim1": horario_1[1].isoformat(sep=' '),
            "just1": "Indisponível hoje",
            "inicio2": horario_2[0].isoformat(sep=' '),
            "fim2": horario_2[1].isoformat(sep=' '),
            "just2": "Indisponível amanhã",
            "inicio3": horario_3[0].isoformat(sep=' '),
            "fim3": horario_3[1].isoformat(sep=' '),
            "just3": "Férias",
            "cpf": cpf,
        }
    )
    session.commit()

@pytest.fixture
def mock_criar_agendamento(
    session,
    mock_criar_servicos,
    mock_criar_barbeiro,
    mock_criar_usuario,
    mock_criar_jornada_de_trabalho,
):
    # Cria serviços e obtém os IDs
    ids_servicos = {
        "id0": "servico-001",
        "id1": "servico-002",
        "id2": "servico-003",
    }
    mock_criar_servicos(ids=ids_servicos)

    # Cria agendamentos
    session.execute(
        text(
            """
            INSERT INTO agendamento (id, horario_inicio, horario_fim, cliente_cpf, barbeiro_cpf) VALUES
            ('agendamento-001', '2025-06-10 10:00:00', '2025-06-10 11:00:00', '05705608020', '25811756054'),
            ('agendamento-002', '2025-06-11 14:00:00', '2025-06-11 15:00:00', '56198304035', '36311464004'),
            ('agendamento-003', '2025-06-12 09:30:00', '2025-06-12 10:30:00', '80990188000', '09357654097')
            """
        )
    )

    # Relaciona serviços aos agendamentos na tabela intermediária
    session.execute(
        text(
            """
            INSERT INTO servicos_do_agendamento (agendamento, servico) VALUES
            ('agendamento-001', :servico1),
            ('agendamento-001', :servico2),
            ('agendamento-002', :servico3)
            """
        ),
        {
            "servico1": ids_servicos["id0"],
            "servico2": ids_servicos["id1"],
            "servico3": ids_servicos["id2"],
        }
    )

    session.commit()
    return {
        "id_agendamento": "agendamento-001",
        "servicos": [ids_servicos["id0"], ids_servicos["id1"]],
    }


# Mocks para Pagamento
@pytest.fixture
def mock_criar_pagamento(session):
    """Cria um pagamento de teste"""
    from src.domain.models import Pagamento, Agendamento, Usuario, Servico, Barbeiro
    from src.domain.value_objects import MetodoPagamento
    from datetime import datetime, timedelta
    from sqlalchemy import text
    
    # Criar usuários via SQL
    session.execute(
        text("""
            INSERT INTO usuario (cpf, nome, email, senha, telefone, eh_barbeiro) VALUES
            ('12345678901', 'Cliente Teste', 'cliente@test.com', 'senha123', '11999999999', FALSE),
            ('98765432100', 'Barbeiro Teste', 'barbeiro@test.com', 'senha123', '11888888888', TRUE)
        """)
    )
    
    # Criar serviços via SQL
    servico1_id = str(uuid4())
    servico2_id = str(uuid4())
    session.execute(
        text("""
            INSERT INTO servico (id, nome, descricao, preco, duracao) VALUES
            (:id1, 'Corte', 'Corte de cabelo', 30.0, 30),
            (:id2, 'Barba', 'Fazer a barba', 20.0, 20)
        """),
        {"id1": servico1_id, "id2": servico2_id}
    )
    
    # Criar agendamento via SQL
    agendamento_id = str(uuid4())
    horario_inicio = datetime.now() + timedelta(days=1)
    horario_fim = horario_inicio + timedelta(minutes=50)
    
    session.execute(
        text("""
            INSERT INTO agendamento (id, horario_inicio, horario_fim, barbeiro_cpf, cliente_cpf) VALUES
            (:id, :horario_inicio, :horario_fim, '98765432100', '12345678901')
        """),
        {
            "id": agendamento_id,
            "horario_inicio": horario_inicio,
            "horario_fim": horario_fim
        }
    )
    
    # Criar relação agendamento-serviços
    session.execute(
        text("""
            INSERT INTO servicos_do_agendamento (agendamento, servico) VALUES
            (:agendamento, :servico1),
            (:agendamento, :servico2)
        """),
        {
            "agendamento": agendamento_id,
            "servico1": servico1_id,
            "servico2": servico2_id
        }
    )
    
    # Criar pagamento via SQL
    pagamento_id = str(uuid4())
    session.execute(
        text("""
            INSERT INTO pagamento (id, valor, data, metodo, agendamento_id) VALUES
            (:id, :valor, :data, :metodo, :agendamento_id)
        """),
        {
            "id": pagamento_id,
            "valor": 50.0,
            "data": datetime.now(),
            "metodo": "PIX",
            "agendamento_id": agendamento_id
        }
    )
    
    session.commit()
    
    # Retornar objeto Pagamento para os testes
    pagamento = Pagamento(
        valor=50.0,
        data=datetime.now(),
        metodo=MetodoPagamento.PIX,
        agendamento=Agendamento(
            id=agendamento_id,
            horario_inicio=horario_inicio,
            horario_fim=horario_fim,
            barbeiro=Usuario(cpf="98765432100", nome="Barbeiro Teste", email="barbeiro@test.com", senha="senha123", telefone="11888888888", eh_barbeiro=True),
            cliente=Usuario(cpf="12345678901", nome="Cliente Teste", email="cliente@test.com", senha="senha123", telefone="11999999999", eh_barbeiro=False),
            servicos=[]
        )
    )
    pagamento.id = pagamento_id
    pagamento.agendamento_id = agendamento_id
    
    return pagamento

@pytest.fixture
def mock_criar_usuarios_e_agendamento(session):
    """Cria usuários e agendamento para testes de pagamento"""
    from src.domain.models import Agendamento, Usuario, Servico, Barbeiro
    from datetime import datetime, timedelta
    from sqlalchemy import text
    
    # Criar usuários via SQL
    session.execute(
        text("""
            INSERT INTO usuario (cpf, nome, email, senha, telefone, eh_barbeiro) VALUES
            ('12345678901', 'Cliente Teste', 'cliente@test.com', 'senha123', '11999999999', FALSE),
            ('98765432100', 'Barbeiro Teste', 'barbeiro@test.com', 'senha123', '11888888888', TRUE)
        """)
    )
    
    # Criar serviços via SQL
    servico1_id = str(uuid4())
    servico2_id = str(uuid4())
    session.execute(
        text("""
            INSERT INTO servico (id, nome, descricao, preco, duracao) VALUES
            (:id1, 'Corte', 'Corte de cabelo', 30.0, 30),
            (:id2, 'Barba', 'Fazer a barba', 20.0, 20)
        """),
        {"id1": servico1_id, "id2": servico2_id}
    )
    
    # Criar agendamento via SQL
    agendamento_id = str(uuid4())
    horario_inicio = datetime.now() + timedelta(days=1)
    horario_fim = horario_inicio + timedelta(minutes=50)
    
    session.execute(
        text("""
            INSERT INTO agendamento (id, horario_inicio, horario_fim, barbeiro_cpf, cliente_cpf) VALUES
            (:id, :horario_inicio, :horario_fim, '98765432100', '12345678901')
        """),
        {
            "id": agendamento_id,
            "horario_inicio": horario_inicio,
            "horario_fim": horario_fim
        }
    )
    
    # Criar relação agendamento-serviços
    session.execute(
        text("""
            INSERT INTO servicos_do_agendamento (agendamento, servico) VALUES
            (:agendamento, :servico1),
            (:agendamento, :servico2)
        """),
        {
            "agendamento": agendamento_id,
            "servico1": servico1_id,
            "servico2": servico2_id
        }
    )
    
    session.commit()
    
    # Retornar objetos para os testes
    cliente = Usuario(cpf="12345678901", nome="Cliente Teste", email="cliente@test.com", senha="senha123", telefone="11999999999", eh_barbeiro=False)
    barbeiro_usuario = Usuario(cpf="98765432100", nome="Barbeiro Teste", email="barbeiro@test.com", senha="senha123", telefone="11888888888", eh_barbeiro=True)
    barbeiro = Barbeiro(usuario=barbeiro_usuario)
    agendamento = Agendamento(
        id=agendamento_id,
        horario_inicio=horario_inicio,
        horario_fim=horario_fim,
        barbeiro=barbeiro_usuario,
        cliente=cliente,
        servicos=[]
    )
    
    return cliente, barbeiro, agendamento

@pytest.fixture
def mock_criar_pagamentos_cliente(session):
    """Cria múltiplos pagamentos para um cliente"""
    from src.domain.models import Pagamento, Agendamento, Usuario, Servico, Barbeiro
    from src.domain.value_objects import MetodoPagamento
    from datetime import datetime, timedelta
    from sqlalchemy import text
    
    # Criar usuários via SQL
    session.execute(
        text("""
            INSERT INTO usuario (cpf, nome, email, senha, telefone, eh_barbeiro) VALUES
            ('12345678901', 'Cliente Teste', 'cliente@test.com', 'senha123', '11999999999', FALSE),
            ('98765432100', 'Barbeiro Teste', 'barbeiro@test.com', 'senha123', '11888888888', TRUE)
        """)
    )
    
    # Criar serviços via SQL
    servico1_id = str(uuid4())
    servico2_id = str(uuid4())
    session.execute(
        text("""
            INSERT INTO servico (id, nome, descricao, preco, duracao) VALUES
            (:id1, 'Corte', 'Corte de cabelo', 30.0, 30),
            (:id2, 'Barba', 'Fazer a barba', 20.0, 20)
        """),
        {"id1": servico1_id, "id2": servico2_id}
    )
    
    # Criar múltiplos agendamentos e pagamentos
    agendamentos = []
    pagamentos = []
    
    for i in range(3):
        agendamento_id = str(uuid4())
        horario_inicio = datetime.now() + timedelta(days=i+1)
        horario_fim = horario_inicio + timedelta(minutes=50)
        
        # Criar agendamento
        session.execute(
            text("""
                INSERT INTO agendamento (id, horario_inicio, horario_fim, barbeiro_cpf, cliente_cpf) VALUES
                (:id, :horario_inicio, :horario_fim, '98765432100', '12345678901')
            """),
            {
                "id": agendamento_id,
                "horario_inicio": horario_inicio.isoformat(sep=' '),
                "horario_fim": horario_fim.isoformat(sep=' ')
            }
        )
        
        # Criar relação agendamento-serviços
        session.execute(
            text("""
                INSERT INTO servicos_do_agendamento (agendamento, servico) VALUES
                (:agendamento, :servico1),
                (:agendamento, :servico2)
            """),
            {
                "agendamento": agendamento_id,
                "servico1": servico1_id,
                "servico2": servico2_id
            }
        )
        
        # Criar pagamento
        pagamento_id = str(uuid4())
        session.execute(
            text("""
                INSERT INTO pagamento (id, valor, data, metodo, agendamento_id) VALUES
                (:id, :valor, :data, :metodo, :agendamento_id)
            """),
            {
                "id": pagamento_id,
                "valor": 50.0 + (i * 10),
                "data": datetime.now(),
                "metodo": "PIX" if i % 2 == 0 else "CARTAO",
                "agendamento_id": agendamento_id
            }
        )
        
        # Criar objetos para retorno
        agendamento = Agendamento(
            id=agendamento_id,
            horario_inicio=horario_inicio,
            horario_fim=horario_fim,
            barbeiro=Usuario(cpf="98765432100", nome="Barbeiro Teste", email="barbeiro@test.com", senha="senha123", telefone="11888888888", eh_barbeiro=True),
            cliente=Usuario(cpf="12345678901", nome="Cliente Teste", email="cliente@test.com", senha="senha123", telefone="11999999999", eh_barbeiro=False),
            servicos=[]
        )
        agendamentos.append(agendamento)
        
        pagamento = Pagamento(
            valor=50.0 + (i * 10),
            data=datetime.now(),
            metodo=MetodoPagamento.PIX if i % 2 == 0 else MetodoPagamento.CARTAO,
            agendamento=agendamento
        )
        pagamento.id = pagamento_id
        pagamentos.append(pagamento)
    
    session.commit()
    
    return "12345678901", pagamentos

