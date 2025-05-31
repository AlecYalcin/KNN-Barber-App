import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers
from src.adapters.orm import start_mappers, metadata
from sqlalchemy import text

@pytest.fixture
def in_memory_db():
    # Engine criada
    engine = create_engine("sqlite:///:memory:")
    
    # Iniciando mapeamento e depois criando tabelas
    start_mappers()
    metadata.create_all(engine)
    
    # Generator a engine para ficar em lazy memory
    yield engine
    
    # Limpar após uso
    clear_mappers()

@pytest.fixture
def session(in_memory_db):
    # Criador de sessão
    session_maker = sessionmaker(bind=in_memory_db)
    
    # Criando sessão
    session = session_maker()

    # Disponibilizando sessão
    yield session

    # Fechando sessão
    session.close()