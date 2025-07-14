from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from database.connection import get_uow
from src.service.unit_of_work import UnidadeDeTrabalho
from src.service.services import (
    criar_horario_indisponivel,
    consultar_horario_indisponivel,
    consultar_horario_indisponivel_por_horario,
    alterar_horario_indisponivel,
    excluir_horario_indisponivel,
)
from datetime import datetime, timedelta
from .autenticacao_router import obter_usuario_atual

class HorarioIndisponivelCreateModel(BaseModel):
    barbeiro_cpf: str
    horario_inicio: datetime
    horario_fim: datetime
    justificativa: str

class HorarioIndisponivelUpdateModel(BaseModel):
    horario_inicio: datetime | None = None
    horario_fim: datetime | None = None
    justificativa: str | None = None

router = APIRouter(
    prefix="/horario-indisponivel",
    tags=["horario_indisponivel"],
)

@router.post('/criar')
def criando_horario_indisponivel(
    horario_indisponivel: HorarioIndisponivelCreateModel,
    uow: UnidadeDeTrabalho = Depends(get_uow),
    usuario: dict = Depends(obter_usuario_atual),
):
    criar_horario_indisponivel(
        uow=uow,
        barbeiro_cpf=horario_indisponivel.barbeiro_cpf,
        horario_inicio=horario_indisponivel.horario_inicio,
        horario_fim=horario_indisponivel.horario_fim,
        justificativa=horario_indisponivel.justificativa,
        solicitante=usuario,
    )

    return JSONResponse(
        status_code=201,
        content={"mensagem":"Horário indisponível cadastrado com sucesso!"},
    )

@router.get('/pesquisar-horarios')
def consultando_horario_indisponivel_por_faixa_de_horarios(
    horario_inicio: datetime | None = None,
    horario_fim: datetime | None = None,
    barbeiro_cpf: str | None = None,
    uow: UnidadeDeTrabalho = Depends(get_uow),
):
    agora = datetime.now()

    if horario_inicio is None:
        horario_inicio = agora - timedelta(days=7)
    
    if horario_fim is None:
        horario_fim = agora + timedelta(days=7)

    horarios_encontrados = consultar_horario_indisponivel_por_horario(
        uow=uow,
        horario_inicio=horario_inicio,
        horario_fim=horario_fim,
        barbeiro_cpf=barbeiro_cpf,
    )
    
    return JSONResponse(
        status_code=200,
        content=horarios_encontrados
    )

@router.get('/{id}')
def consultando_horario_indisponivel(
    id: str,
    uow: UnidadeDeTrabalho = Depends(get_uow),
):
    horario_encontrado = consultar_horario_indisponivel(
        uow=uow,
        id=id,
    )

    return JSONResponse(
        status_code=200,
        content=horario_encontrado,
    )

@router.patch('/{id}')
def atualizando_horario_indisponivel(
    id: str,
    novo_horario_indisponivel: HorarioIndisponivelUpdateModel,
    uow: UnidadeDeTrabalho = Depends(get_uow),
    usuario: dict = Depends(obter_usuario_atual),
):
    alterar_horario_indisponivel(
        uow=uow,
        id=id,
        horario_inicio=novo_horario_indisponivel.horario_inicio,
        horario_fim=novo_horario_indisponivel.horario_fim,
        justificativa=novo_horario_indisponivel.justificativa,
        solicitante=usuario,
    )

    return JSONResponse(
        status_code=200,
        content={"mensagem":"Horário indisponível alterado com sucesso!"}
    )

@router.delete('/{id}')
def excluindo_horario_indisponivel(
    id: str,
    uow: UnidadeDeTrabalho = Depends(get_uow),
    usuario: dict = Depends(obter_usuario_atual),
):
    excluir_horario_indisponivel(
        uow=uow,
        id=id,
        solicitante=usuario,
    )

    return JSONResponse(
        status_code=200,
        content={"mensagem":"Horário indisponível excluído com sucesso!"}
    )
