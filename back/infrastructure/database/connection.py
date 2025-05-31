from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Configuração do banco de dados
DATABASE_URL = "postgresql://admin:admin@localhost:5432/knn_barber_app_db"

# Criar engine
engine = create_engine(DATABASE_URL)

# Criar fábrica de sessões
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)