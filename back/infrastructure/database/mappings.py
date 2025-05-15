from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PessoaModel(Base):
    __tablename__ = 'pessoas'

    cpf = Column(String(11), primary_key=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    telefone = Column(String(20), nullable=False)
    senha = Column(String(100), nullable=False)  # In production, this should be hashed 