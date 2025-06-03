from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from infrastructure.database.connection import engine
from src.adapters.orm import start_mappers, metadata
from sqlalchemy.orm import clear_mappers

from .routes.usuario_routes import router as usuario_router


# Configurar banco de dados
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Configura o mapeamento do banco de dados
    start_mappers()
    metadata.create_all(engine)

    # Retornando para a aplicação
    yield

    # Limpando mapeamento
    clear_mappers()

# Aplicação FastAPI
app = FastAPI(title="KNN Barber API", lifespan=lifespan)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Adicionando rotas
app.include_router(usuario_router)