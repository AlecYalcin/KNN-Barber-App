import pytest
from sqlalchemy import StaticPool, create_engine, event
from sqlalchemy.orm import sessionmaker, clear_mappers
from src.service.unit_of_work import UnidadeDeTrabalho
from src.adapters.orm import start_mappers, metadata
from infrastructure.database.connection import engine as postgres_engine, get_uow, session_maker as postgres_maker

# ==================
# FIXTURES DE SQLITE
# ==================

@pytest.fixture
def in_memory_db():
    # Engine criada
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False}, 
        poolclass=StaticPool,
    )

    # Habilita foreign keys para SQLite
    def enable_foreign_keys(dbapi_connection, connection_record):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()
    
    event.listen(engine, "connect", enable_foreign_keys)

    # Criando tabelas do banco de dados
    metadata.create_all(engine)
    
    # Generator a engine para ficar em lazy memory
    yield engine

    # Encerrando engine
    engine.dispose()

@pytest.fixture
def session_maker(in_memory_db):
    # Iniciando o mapemaento de ORM 
    start_mappers()

    # Introduzindo a sessionmaker
    yield sessionmaker(bind=in_memory_db, expire_on_commit=False)
    
    # Limpando mapeamento de ORM
    clear_mappers()

@pytest.fixture
def session(session_maker):
    # Criando sessão
    session = session_maker()

    # Disponibilizando sessão
    yield session

    # Fechando sessão
    session.close()

# ====================
# FIXTURES DE POSTGRES
# ====================

@pytest.fixture
def postgres_db():
    # Criando tabelas do banco de dados
    metadata.create_all(postgres_engine)

@pytest.fixture
def postgres_session_maker(postgres_db):
    # Iniciando o mapemaento de ORM 
    start_mappers()

    # Introduzindo a sessionmaker
    yield postgres_maker
    
    # Limpando mapeamento de ORM
    clear_mappers()

@pytest.fixture
def postgres_session(postgres_session_maker):
    # Criando sessão
    session = postgres_session_maker()

    # Disponibilizando sessão
    yield session

    # Fechando sessão
    session.close()

# =============
# FIXURE DE API
# =============

from src.entrypoints.fastapi import app
from fastapi.testclient import TestClient

@pytest.fixture
def client(session_maker):
    app.dependency_overrides[get_uow] = lambda: UnidadeDeTrabalho(session_maker)
    yield TestClient(app)
