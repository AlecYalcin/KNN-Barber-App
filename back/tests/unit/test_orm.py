import pytest
from src.domain.models import *
from sqlalchemy import text
from uuid import uuid4

@pytest.fixture
def create_users(session):
    session.execute(
        text(
            "INSERT INTO usuario (cpf, nome, senha, email) VALUES"
            '("123.456.789-00","Usuário 01","123","usuario1@teste.com"),'
            '("987.654.321-00","Usuário 02","123","usuario2@teste.com"),'
            '("111.222.333-00","Usuário 03","123","usuario3@teste.com")'
        )
    )

@pytest.fixture
def create_services(session):
    def create_services_with_ids(ids: dict):
        session.execute(
            text(
                """
                INSERT INTO servico (id, nome, descricao, preco, duracao) VALUES
                (:id0,"Serviço 01","Serviço de Cavanhaque",20.00,15),
                (:id1,"Serviço 02","Serviço de Cabelo",10.00,30),
                (:id2,"Serviço 03","Serviço de Barba",15.00,45)
                """
            ),
            params=ids
        )    
    yield create_services_with_ids

def test_adicionando_usuario(create_users, session):
    esperado = [
        Usuario(cpf="123.456.789-00",nome="Usuário 01",senha="123",email="usuario1@teste.com",eh_barbeiro=False),
        Usuario(cpf="987.654.321-00",nome="Usuário 02",senha="123",email="usuario2@teste.com",eh_barbeiro=False),
        Usuario(cpf="111.222.333-00",nome="Usuário 03",senha="123",email="usuario3@teste.com",eh_barbeiro=False),
    ]

    assert session.query(Usuario).all() == esperado

def test_adicionando_servico(create_services, session):
    ids = {
        "id0": str(uuid4()),
        "id1": str(uuid4()),
        "id2": str(uuid4()),
    }

    create_services(ids)

    esperado = [
        Servico(id=f"{ids['id0']}",nome="Serviço 01",descricao="Serviço de Cavanhaque",preco=20,duracao=15),
        Servico(id=f"{ids['id1']}",nome="Serviço 02",descricao="Serviço de Cabelo",preco=10,duracao=30),
        Servico(id=f"{ids['id2']}",nome="Serviço 03",descricao="Serviço de Barba",preco=15,duracao=45),
    ]

    assert session.query(Servico).all() == esperado

def test_removendo_usuario(create_users, session):
    session.execute(
        text(
            """
            DELETE FROM usuario
            """
        ),
    )

    assert session.query(Servico).all() == []

def test_removendo_servicos(create_services, session):
    session.execute(
        text(
            """
            DELETE FROM servico
            """
        )
    )

    assert session.query(Servico).all() == []
