from datetime import datetime

from database.connection import get_uow
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from src.service.services.agendamento import (
    consultar_agendamento, consultar_agendamentos_por_barbeiro,
    consultar_agendamentos_por_horario, criar_agendamento, listar_agendamentos,
    remover_agendamento)
from src.service.unit_of_work import UnidadeDeTrabalho


class AgendamentoCreate(BaseModel):
    barbeiro_cpf: str
    cliente_cpf: str
    servicos_id: list[str]
    horario_inicio: datetime
    horario_fim: datetime | None = None

router = APIRouter(
    prefix="/agendamento",
    tags=["agendamento"],
)

@router.post("/criar")
def criar_agendamento_route(
    agendamento: AgendamentoCreate,
    uow: UnidadeDeTrabalho = Depends(get_uow),
):
    """
    Cria um novo agendamento.
    
    Args:
        agendamento(AgendamentoCreate): Dados do agendamento a ser criado
        uow(UnidadeDeTrabalho): Unidade de Trabalho abstrata
    Returns:
        JSONResponse: Mensagem de sucesso ou erro
    """
    
    criar_agendamento(
        uow=uow,
        barbeiro_cpf=agendamento.barbeiro_cpf,
        cliente_cpf=agendamento.cliente_cpf,
        servicos_id=agendamento.servicos_id,
        horario_inicio=agendamento.horario_inicio,
        horario_fim=agendamento.horario_fim,
    )
    return JSONResponse(
        status_code=201,
        content={"mensagem": "Agendamento criado com sucesso!"}
    )



@router.get("/barbeiro/{barbeiro_cpf}")
def consultar_agendamentos_por_barbeiro_route(
    barbeiro_cpf: str,
    uow: UnidadeDeTrabalho = Depends(get_uow),
):
    """
    Consulta todos os agendamentos de um barbeiro específico.
   """

    agendamentos = consultar_agendamentos_por_barbeiro(uow=uow, barbeiro_cpf=barbeiro_cpf)
    return JSONResponse(
        status_code=200,
        content=agendamentos
    )


@router.get("/horario")
def consultar_agendamentos_por_horario_route(
    horario_inicio: datetime,
    horario_fim: datetime,
    uow: UnidadeDeTrabalho = Depends(get_uow),
):
    """
    Consulta todos os agendamentos em um determinado horário.
    
    Args:
        horario_inicio(datetime): Horário de início do agendamento
        horario_fim(datetime): Horário de fim do agendamento
        uow(UnidadeDeTrabalho): Unidade de Trabalho abstrata
    """

    
    horarios = (horario_inicio, horario_fim)
    agendamentos = consultar_agendamentos_por_horario(uow=uow, horarios=horarios)
    return JSONResponse(
        status_code=200,
        content=agendamentos
    )


@router.get("/listar", response_model=list[dict])
def listar_agendamentos_route(
    uow: UnidadeDeTrabalho = Depends(get_uow),
):
    """
    Lista todos os agendamentos existentes no sistema.
    
    Args:
        uow(UnidadeDeTrabalho): Unidade de Trabalho abstrata
    Returns:
        JSONResponse: Lista de agendamentos ou mensagem de erro
    """
    agendamentos = listar_agendamentos(uow=uow)
    return JSONResponse(
        status_code=200,
        content=agendamentos
    )

@router.delete("/{id}")
def remover_agendamento_route(
    id: str,
    uow: UnidadeDeTrabalho = Depends(get_uow),
):
    """
    Remove um agendamento pelo ID.
    
    Args:
        id(str): ID do agendamento a ser removido
        uow(UnidadeDeTrabalho): Unidade de Trabalho abstrata
    Returns:
        JSONResponse: Mensagem de sucesso ou erro
    """

    remover_agendamento(uow=uow, id=id)
    return JSONResponse(
        status_code=200,
        content={"mensagem": "Agendamento removido com sucesso!"}
    )

@router.get("/{id}")
def consultar_agendamento_route(
    id: str,
    uow: UnidadeDeTrabalho = Depends(get_uow),
):
    """
    Consulta um agendamento pelo ID.
    
    Args:
        id(str): ID do agendamento a ser consultado
        uow(UnidadeDeTrabalho): Unidade de Trabalho abstrata
    Returns:
        JSONResponse: Detalhes do agendamento ou mensagem de erro
    """

    agendamento = consultar_agendamento(uow=uow, id=id)

    return JSONResponse(
        status_code=200,
        content=agendamento
    )
