from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from back.api.routes.pessoa_routes import router as pessoa_router
from back.infrastructure.database.connection import engine
from back.domain.models import Pessoa

app = FastAPI(title="KNN Barber API")

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especifique as origens permitidas
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rotas
app.include_router(pessoa_router, prefix="/pessoas", tags=["pessoas"])

@app.get("/")
def read_root():
    return {"message": "KNN Barber API"} 