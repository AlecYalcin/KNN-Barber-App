from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager

from sqlalchemy.orm import clear_mappers

from database.error_map import ERROR_MAP
from database.connection import engine
from src.domain.exceptions import DomainError
from src.adapters.orm import start_mappers, metadata

from .routes import *

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
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173", "http://localhost:3000"],
    allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"],
    allow_headers=["*"],
)

# Adicionando rotas
app.include_router(usuario_router)
app.include_router(servico_router)
app.include_router(horario_router)
app.include_router(jornada_router)
app.include_router(autenticacao_router)
app.include_router(agendamento_router)
app.include_router(pagamento_router)

# Error Handling
@app.exception_handler(DomainError)
async def value_error_handler(request: Request, exc: DomainError):
    error_mapped = ERROR_MAP.get(exc.__class__.__name__, {
        "error":"Erro não encontrado.",
        "message":"Erro não mapeado.",
    })

    mensagem = str(exc)
    if not mensagem:
        mensagem = error_mapped['message']


    return JSONResponse(
        status_code=error_mapped['status_code'],
        content={"error": exc.__class__.__name__, "mensagem": mensagem},
    )