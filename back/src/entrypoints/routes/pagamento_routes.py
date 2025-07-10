from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from database.connection import get_uow
from src.service.unit_of_work import UnidadeDeTrabalho
from src.service.services.pagamento import (
    criar_pagamento,
    consultar_pagamento,
    consultar_pagamento_por_agendamento,
    listar_pagamentos_de_cliente,
    atualizar_pagamento,
    remover_pagamento,
)
from src.domain.value_objects import MetodoPagamento
from .autenticacao_router import obter_usuario_atual

class PagamentoCreate(BaseModel):
    valor: float
    metodo: MetodoPagamento
    agendamento_id: str

class PagamentoUpdate(BaseModel):
    valor: float | None = None
    metodo: MetodoPagamento | None = None

router = APIRouter(
    prefix="/pagamento",
    tags=["pagamentos"],
)

@router.post("/criar")
def criacao_de_pagamento(
    pagamento: PagamentoCreate,
    uow: UnidadeDeTrabalho = Depends(get_uow),
    usuario: dict = Depends(obter_usuario_atual),
):
    criar_pagamento(
        uow=uow,
        valor=pagamento.valor,
        metodo=pagamento.metodo,
        agendamento_id=pagamento.agendamento_id,
        solicitante=usuario,
    )

    return JSONResponse(
        status_code=201,
        content={"mensagem":"Pagamento cadastrado com sucesso!"}
    )

@router.get("/listar/{cpf}", response_model=list[dict])
def listando_pagamentos_de_cliente(
    cpf: str,
    uow: UnidadeDeTrabalho = Depends(get_uow),
):
    pagamentos = listar_pagamentos_de_cliente(
        uow=uow,
        cpf=cpf
    )

    return JSONResponse(
        status_code=200,
        content=pagamentos,
    )

@router.get("/{id}", response_model=dict)
def consultando_pagamento_por_id(
    id: str,
    uow: UnidadeDeTrabalho = Depends(get_uow),
):
    pagamento = consultar_pagamento(
        uow=uow,
        id=id,
    )

    return JSONResponse(
        status_code=200,
        content=pagamento,
    )

@router.get("/agendamento/{agendamento_id}", response_model=dict | None)
def consultando_pagamento_por_agendamento(
    agendamento_id: str,
    uow: UnidadeDeTrabalho = Depends(get_uow),
):
    pagamento = consultar_pagamento_por_agendamento(
        uow=uow,
        agendamento_id=agendamento_id,
    )

    return JSONResponse(
        status_code=200,
        content=pagamento,
    )

@router.patch("/{id}")
def atualizando_pagamento(
    id: str,
    novo_pagamento: PagamentoUpdate,
    uow: UnidadeDeTrabalho = Depends(get_uow),
    usuario: dict = Depends(obter_usuario_atual),
):
    atualizar_pagamento(
        uow=uow,
        id=id,
        novo_valor=novo_pagamento.valor,
        novo_metodo=novo_pagamento.metodo,
        solicitante=usuario,
    )    

    return JSONResponse(
        status_code=200,
        content={"mensagem":"Pagamento atualizado com sucesso."}
    )

@router.delete("/{id}")
def excluindo_pagamento(
    id: str,
    uow: UnidadeDeTrabalho = Depends(get_uow),
    usuario: dict = Depends(obter_usuario_atual),
):
    remover_pagamento(
        uow=uow,
        id=id,
        solicitante=usuario,
    )

    return JSONResponse(
        status_code=200,
        content={"mensagem":"Pagamento excluído com sucesso."}
    ) 