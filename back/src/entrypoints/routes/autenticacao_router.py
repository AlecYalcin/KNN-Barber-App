from fastapi import APIRouter, Depends, HTTPException, Header
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from database.connection import get_uow
from src.service.unit_of_work import UnidadeDeTrabalho
from src.service.services import (
    autenticar,
    registrar,
    retornar_usuario,
)

class AutenticacaoModel(BaseModel):
    email: str
    senha: str

class RegistroModel(BaseModel):
    cpf: str
    nome: str
    email: str
    senha: str
    telefone: str | None = None

router = APIRouter(
    prefix="/auth",
    tags=["autenticacao"],
)

@router.post('/login')
def autenticando_usuario(
    autenticacao: AutenticacaoModel,
    uow: UnidadeDeTrabalho = Depends(get_uow),
):
    token = autenticar(
        uow=uow,
        email=autenticacao.email,
        senha=autenticacao.senha,
    )

    return JSONResponse(
        status_code=200,
        content={"token":token},
    )

@router.post("/register")
def registrando_usuario(
    registro: RegistroModel,
    uow: UnidadeDeTrabalho = Depends(get_uow),
):
    token = registrar(
        uow=uow,
        cpf=registro.cpf,
        nome=registro.nome,
        email=registro.email,
        senha=registro.senha,
        telefone=registro.telefone,
    )  

    return JSONResponse(
        status_code=200,
        content={"token":token},
    )

def obter_usuario_atual(
    uow: UnidadeDeTrabalho = Depends(get_uow),
    token: str | None = Header(None, alias="Authorization"),
) -> dict:
    if token is None or not token.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail="Token ausente ou malformado",
        )

    token = token.removeprefix("Bearer ").strip()
    usuario = retornar_usuario(uow=uow, token=token)
    
    return usuario