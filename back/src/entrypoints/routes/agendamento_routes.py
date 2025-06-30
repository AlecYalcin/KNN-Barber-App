from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from infrastructure.database.connection import get_uow
from src.service.unit_of_work import UnidadeDeTrabalho
from src.service.services.agendamento import (
    criar_agendamento,
    consultar_agendamento,
    listar_agendamentos,
    remover_agendamento,
    consultar_agendamentos_por_barbeiro,
    consultar_agendamentos_por_horario,
)
from datetime import time

class AgendamentoCreate(BaseModel):
    barbeiro_cpf: str
    usuario_cpf: str
    servico_id: str
    horario_inicio: time
    horario_fim: time | None = None

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
    try:
        criar_agendamento(
            uow=uow,
            barbeiro_cpf=agendamento.barbeiro_cpf,
            usuario_cpf=agendamento.usuario_cpf,
            servico_id=agendamento.servico_id,
            horario_inicio=agendamento.horario_inicio,
            horario_fim=agendamento.horario_fim,
        )
        return JSONResponse(
            status_code=201,
            content={"mensagem": "Agendamento criado com sucesso!"}
        )
    except Exception as e:
        return JSONResponse(
            status_code=400,
            content={"erro": str(e)}
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
    try:
        agendamento = consultar_agendamento(uow=uow, id=id)
        if not agendamento:
            return JSONResponse(
                status_code=404,
                content={"erro": "Agendamento não encontrado"}
            )
        return JSONResponse(
            status_code=200,
            content=agendamento.to_dict()
        )
    except Exception as e:
        return JSONResponse(
            status_code=400,
            content={"erro": str(e)}
        )

@router.get("/barbeiro/{barbeiro_cpf}")
def consultar_agendamentos_por_barbeiro_route(
    barbeiro_cpf: str,
    uow: UnidadeDeTrabalho = Depends(get_uow),
):
    """
    Consulta todos os agendamentos de um barbeiro específico.
    
    Args:
        barbeiro_cpf(str): CPF do barbeiro
        uow(UnidadeDeTrabalho): Unidade de Trabalho abstrata
    Returns:
        JSONResponse: Lista de agendamentos ou mensagem de erro
    """
    try:
        agendamentos = consultar_agendamentos_por_barbeiro(uow=uow, barbeiro_cpf=barbeiro_cpf)
        return JSONResponse(
            status_code=200,
            content=agendamentos
        )
    except Exception as e:
        return JSONResponse(
            status_code=400,
            content={"erro": str(e)}
        )

@router.get("/horario")
def consultar_agendamentos_por_horario_route(
    horario_inicio: time,
    horario_fim: time,
    uow: UnidadeDeTrabalho = Depends(get_uow),
):
    """
    Consulta todos os agendamentos em um determinado horário.
    
    Args:
        horario_inicio(time): Horário de início do agendamento
        horario_fim(time): Horário de fim do agendamento
        uow(UnidadeDeTrabalho): Unidade de Trabalho abstrata
    Returns:
        JSONResponse: Lista de agendamentos ou mensagem de erro
    """
    try:
        horarios = (horario_inicio, horario_fim)
        agendamentos = consultar_agendamentos_por_horario(uow=uow, horarios=horarios)
        return JSONResponse(
            status_code=200,
            content=agendamentos
        )
    except Exception as e:
        return JSONResponse(
            status_code=400,
            content={"erro": str(e)}
        )

@router.get("/listar")
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
    try:
        agendamentos = listar_agendamentos(uow=uow)
        return JSONResponse(
            status_code=200,
            content=agendamentos
        )
    except Exception as e:
        return JSONResponse(
            status_code=400,
            content={"erro": str(e)}
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
    try:
        remover_agendamento(uow=uow, id=id)
        return JSONResponse(
            status_code=200,
            content={"mensagem": "Agendamento removido com sucesso!"}
        )
    except Exception as e:
        return JSONResponse(
            status_code=400,
            content={"erro": str(e)}
        )