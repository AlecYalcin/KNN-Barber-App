from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from back.infrastructure.database.mappings import configure_mappers, metadata

# Configuração do banco de dados
DATABASE_URL = "postgresql://postgres:mysecretpassword@localhost:5432/knn_barber"

# Criar engine
engine = create_engine(DATABASE_URL)

# Criar fábrica de sessões
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Session:
    """
    Dependency para injetar a sessão do banco nas rotas.
    Garante que a sessão é fechada após o uso.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 