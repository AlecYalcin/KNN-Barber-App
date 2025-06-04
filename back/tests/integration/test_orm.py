from src.domain.models import *
from sqlalchemy import text
from uuid import uuid4
from tests.mock import *

def test_adicionando_usuario(mock_criar_usuario, session):
    esperado = [
        Usuario(cpf="05705608020",nome="Usuário 01",senha="123",email="usuario1@teste.com",eh_barbeiro=False),
        Usuario(cpf="56198304035",nome="Usuário 02",senha="123",email="usuario2@teste.com",eh_barbeiro=False),
        Usuario(cpf="80990188000",nome="Usuário 03",senha="123",email="usuario3@teste.com",eh_barbeiro=False),
    ]

    assert session.query(Usuario).all() == esperado

def test_adicionando_servico(mock_criar_servico, session):
    ids = {
        "id0": str(uuid4()),
        "id1": str(uuid4()),
        "id2": str(uuid4()),
    }

    mock_criar_servico(ids)

    esperado = [
        Servico(id=f"{ids['id0']}",nome="Serviço 01",descricao="Serviço de Cavanhaque",preco=20,duracao=15),
        Servico(id=f"{ids['id1']}",nome="Serviço 02",descricao="Serviço de Cabelo",preco=10,duracao=30),
        Servico(id=f"{ids['id2']}",nome="Serviço 03",descricao="Serviço de Barba",preco=15,duracao=45),
    ]

    assert session.query(Servico).all() == esperado

def test_removendo_usuario(mock_criar_usuario, session):
    session.execute(
        text(
            """
            DELETE FROM usuario
            """
        ),
    )

    assert session.query(Servico).all() == []

def test_removendo_servicos(mock_criar_usuario, session):
    session.execute(
        text(
            """
            DELETE FROM servico
            """
        )
    )

    assert session.query(Servico).all() == []
