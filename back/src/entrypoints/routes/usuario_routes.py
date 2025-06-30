from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from database.connection import get_uow
from src.service.unit_of_work import UnidadeDeTrabalho
from src.service.services.usuario import (
    criar_usuario,
    consultar_usuario,
    atualizar_usuario,
    remover_usuario,
)

class UsuarioCreate(BaseModel):
    cpf: str
    nome: str
    email: str
    senha: str
    telefone: str | None = None
    eh_barbeiro: bool = False

class UsuarioUpdate(BaseModel):
    nome: str | None = None
    email: str | None = None
    senha: str | None = None
    telefone: str | None = None

router = APIRouter(
    prefix="/usuario",
    tags=["Usuarios"],
)

@router.post("/criar")
def criacao_de_usuario(
    usuario: UsuarioCreate,
    uow: UnidadeDeTrabalho = Depends(get_uow),
):
    criar_usuario(
        uow=uow,
        cpf=usuario.cpf,
        nome=usuario.nome,
        email=usuario.email,
        senha=usuario.senha,
        telefone=usuario.telefone,
        eh_barbeiro=usuario.eh_barbeiro,
    )

    return JSONResponse(
        status_code=201,
        content={"mensagem":"Sucesso ao criar usuário!"}
    )

@router.get("/{cpf}", response_model=dict)
def recuperando_usuario(
    cpf: str,
    uow: UnidadeDeTrabalho = Depends(get_uow),
):
    usuario = consultar_usuario(
        uow=uow,
        cpf=cpf,
    )

    return JSONResponse(
        status_code=200,
        content=usuario
    )

@router.patch("/{cpf}")
def atualizando_usuario(
    cpf: str,
    novo_usuario: UsuarioUpdate,
    uow: UnidadeDeTrabalho = Depends(get_uow),
):
    atualizar_usuario(
        uow=uow,
        cpf=cpf,
        novo_nome=novo_usuario.nome,
        novo_email=novo_usuario.email,
        novo_telefone=novo_usuario.telefone,
        nova_senha=novo_usuario.senha,
    )

    return JSONResponse(
        status_code=200,
        content={"mensagem":"Usuário atualizado com sucesso!"}
    )

@router.delete("/{cpf}")
def removendo_usuario(
    cpf: str,
    uow: UnidadeDeTrabalho = Depends(get_uow),
):
    remover_usuario(
        uow=uow,
        cpf=cpf
    )

    return JSONResponse(
        status_code=200,
        content={"mensagem":"O usuário foi excluído do sistema!"}
    )