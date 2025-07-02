from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from database.connection import get_uow
from src.service.unit_of_work import UnidadeDeTrabalho
from src.service.services.servico import (
    criar_servico,
    consultar_servico,
    listar_servicos,
    atualizar_servico,
    remover_servico,
)
from .autenticacao_router import obter_usuario_atual

class ServicoCreate(BaseModel):
    nome: str
    descricao: str
    preco: float
    duracao: int

class ServicoUpdate(BaseModel):
    nome: str | None = None
    descricao: str | None = None
    preco: float | None = None
    duracao: int | None = None

router = APIRouter(
    prefix="/servico",
    tags=["servicos"],
)

@router.post("/criar")
def criacao_de_servico(
    servico: ServicoCreate,
    uow: UnidadeDeTrabalho = Depends(get_uow),
    usuario: dict = Depends(obter_usuario_atual),
):
    criar_servico(
        uow=uow,
        nome=servico.nome,
        descricao=servico.descricao,
        preco=servico.preco,
        duracao=servico.duracao,
        solicitante=usuario,
    )

    return JSONResponse(
        status_code=201,
        content={"mensagem":"Serviço cadastrado com sucesso!"}
    )

@router.get("/listar", response_model=list[dict])
def listando_servicos(
    nome: str | None = None,
    uow: UnidadeDeTrabalho = Depends(get_uow),
):
    servicos = listar_servicos(
        uow=uow,
        filtro=nome
    )

    return JSONResponse(
        status_code=200,
        content=servicos,
    )

@router.get("/{id}", response_model=dict)
def consultando_servico_por_id(
    id: str,
    uow: UnidadeDeTrabalho = Depends(get_uow),
):
    servico = consultar_servico(
        uow=uow,
        id=id,
    )

    return JSONResponse(
        status_code=200,
        content=servico,
    )


@router.patch("/{id}")
def atualizando_servico(
    id: str,
    novo_servico: ServicoUpdate,
    uow: UnidadeDeTrabalho = Depends(get_uow),
    usuario: dict = Depends(obter_usuario_atual),
):
    atualizar_servico(
        uow=uow,
        id=id,
        novo_nome=novo_servico.nome,
        nova_descricao=novo_servico.descricao,
        novo_preco=novo_servico.preco,
        nova_duracao=novo_servico.duracao,
        solicitante=usuario,
    )    

    return JSONResponse(
        status_code=200,
        content={"mensagem":"Serviço atualizado com sucesso."}
    )

@router.delete("/{id}")
def excluindo_servico(
    id: str,
    uow: UnidadeDeTrabalho = Depends(get_uow),
    usuario: dict = Depends(obter_usuario_atual),
):
    remover_servico(
        uow=uow,
        id=id,
        solicitante=usuario,
    )

    return JSONResponse(
        status_code=200,
        content={"mensagem":"Serviço excluído com sucesso."}
    )