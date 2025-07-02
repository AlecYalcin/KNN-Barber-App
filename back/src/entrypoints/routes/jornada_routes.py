from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from back.src.entrypoints.routes.autenticacao_router import obter_usuario_atual
from database.connection import get_uow
from src.service.unit_of_work import UnidadeDeTrabalho
from src.service.services import (
    criar_jornada,
    consultar_jornada,
    consultar_jornada_de_trabalho,
    alterar_ativacao_de_jornada,
    excluir_jornada,
)
from datetime import time

class JornadaCreateModel(BaseModel):
    barbeiro_cpf: str
    dia_da_semana: str
    horario_inicio: time
    horario_fim: time
    horario_pausa: time | None = None
    horario_retorno: time | None = None

class JornadaUpdateModel(BaseModel):
    dia_da_semana: str | None = None
    horario_inicio: time | None = None
    horario_fim: time | None = None
    horario_pausa: time | None = None
    horario_retorno: time | None = None

router = APIRouter(
    prefix="/jornada",
    tags=["jornada"],
)

@router.post("/criar")
def criando_jornada(
    jornada: JornadaCreateModel,
    uow: UnidadeDeTrabalho = Depends(get_uow),
    usuario: dict = Depends(obter_usuario_atual),
):
    criar_jornada(
        uow=uow,
        barbeiro_cpf=jornada.barbeiro_cpf,
        dia_da_semana=jornada.dia_da_semana,
        horario_inicio=jornada.horario_inicio,
        horario_fim=jornada.horario_fim,
        horario_pausa=jornada.horario_pausa,
        horario_retorno=jornada.horario_retorno,
        solicitante=usuario,
    )
    
    return JSONResponse(
        status_code=201,
        content={"mensagem":"Jornada criado com sucesso!"}
    )

@router.get("/barbeiro/{barbeiro_cpf}")
def consultando_jornada_de_tarbalho(
    barbeiro_cpf: str,
    uow: UnidadeDeTrabalho = Depends(get_uow),
):
    jornada_de_trabalho = consultar_jornada_de_trabalho(
        uow=uow,
        barbeiro_cpf=barbeiro_cpf,
    )

    return JSONResponse(
        status_code=200,
        content=jornada_de_trabalho,
    )

@router.get("/{id}")
def consultando_jornada(
    id: str,
    uow: UnidadeDeTrabalho = Depends(get_uow),
):
    jornada = consultar_jornada(
        uow=uow,
        id=id,
    )

    return JSONResponse(
        status_code=200,
        content=jornada,
    )

@router.patch("/{id}")
def alterando_jornada(
    id: str,
    uow: UnidadeDeTrabalho = Depends(get_uow),
    usuario: dict = Depends(obter_usuario_atual),
):
    alterar_ativacao_de_jornada(
        uow=uow,
        id=id,
        solicitante=usuario,
    )

    return JSONResponse(
        status_code=200,
        content={"mensagem":"Jornada alterada com sucesso!"},
    )

@router.delete("/{id}")
def excluindo_jornada(
    id: str,
    uow: UnidadeDeTrabalho = Depends(get_uow),
    usuario: dict = Depends(obter_usuario_atual),
):
    excluir_jornada(
        uow=uow,
        id=id,
        solicitante=usuario,
    )

    return JSONResponse(
        status_code=200,
        content={"mensagem":"Jornada excluída com sucesso!"},
    )
