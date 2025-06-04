import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.service.unit_of_work import UnidadeDeTrabalho

# Configuração do banco de dados
LOCAL_URL = "postgresql://admin:admin@localhost:5432/knn_barber_app_db"
DATABASE_URL = os.getenv("DATABASE_URL") or LOCAL_URL

# Criar engine
engine = create_engine(DATABASE_URL)

# Criar fábrica de sessões
session_maker = sessionmaker(bind=engine, expire_on_commit=False)

def get_uow():
    return UnidadeDeTrabalho(session_maker)