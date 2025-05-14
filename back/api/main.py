from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from back.api.routes.pessoa_routes import router as pessoa_router
from back.api.routes.barbeiro_routes import router as barbeiro_router
from back.infrastructure.database.connection import engine
from back.infrastructure.database.mappings import configure_mappers, metadata

app = FastAPI(title="KNN Barber API")

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especifique as origens permitidas
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configurar banco de dados
@app.on_event("startup")
async def startup():
    configure_mappers()
    metadata.create_all(engine)

# Incluir rotas
app.include_router(pessoa_router, prefix="/pessoas", tags=["pessoas"])
app.include_router(barbeiro_router, prefix="/barbeiros", tags=["barbeiros"])

@app.get("/")
def read_root():
    return {"message": "KNN Barber API"} 