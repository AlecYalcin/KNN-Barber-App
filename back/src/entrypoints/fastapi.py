from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from back.infrastructure.database.connection import engine, SessionLocal
from sqlalchemy.orm import sessionmaker, clear_mappers
from back.src.adapters.orm import start_mappers, metadata

app = FastAPI(title="KNN Barber API")

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configurar banco de dados
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Configura o mapeamento do banco de dados
    start_mappers()

    # Cria todos os dados de mapeamento no banco
    metadata.create_all(engine)

    # Sessão individualizada
    session = SessionLocal()

    # Entregando sessão as rotas
    yield session

    # Fechando sessão
    session.close()

    # Limpando mapeamento
    clear_mappers()

# Incluir rotas
@app.get("/")
def teste_mensagem():
    return {"message": "KNN Barber API"} 