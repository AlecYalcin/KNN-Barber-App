from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from back.services.pessoa_service import PessoaService
from back.infrastructure.database.connection import get_db
from back.api.schemas.pessoa_schema import (
    PessoaCreate,
    PessoaUpdate,
    PessoaResponse
)

router = APIRouter()

@router.post("", response_model=PessoaResponse)
def criar_pessoa(pessoa: PessoaCreate, db: Session = Depends(get_db)):
    service = PessoaService()
    try:
        nova_pessoa = service.criar_pessoa(
            cpf=pessoa.cpf,
            nome=pessoa.nome,
            email=pessoa.email,
            telefone=pessoa.telefone,
            senha=pessoa.senha
        )
        return nova_pessoa
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("", response_model=List[PessoaResponse])
def listar_pessoas(db: Session = Depends(get_db)):
    service = PessoaService()
    return service.listar_pessoas()

@router.get("/{cpf}", response_model=PessoaResponse)
def buscar_pessoa(cpf: str, db: Session = Depends(get_db)):
    service = PessoaService()
    pessoa = service.buscar_pessoa_por_cpf(cpf)
    if not pessoa:
        raise HTTPException(status_code=404, detail="Pessoa não encontrada")
    return pessoa

@router.put("/{cpf}", response_model=PessoaResponse)
def atualizar_pessoa(cpf: str, pessoa: PessoaUpdate, db: Session = Depends(get_db)):
    service = PessoaService()
    try:
        pessoa_atualizada = service.atualizar_dados(
            cpf=cpf,
            **pessoa.model_dump(exclude_unset=True)
        )
        if not pessoa_atualizada:
            raise HTTPException(status_code=404, detail="Pessoa não encontrada")
        return pessoa_atualizada
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{cpf}")
def remover_pessoa(cpf: str, db: Session = Depends(get_db)):
    service = PessoaService()
    if not service.remover_pessoa(cpf):
        raise HTTPException(status_code=404, detail="Pessoa não encontrada")
    return {"message": "Pessoa removida com sucesso"}

@router.post("/login")
def login(email: str, senha: str, db: Session = Depends(get_db)):
    service = PessoaService()
    pessoa = service.autenticar_pessoa(email, senha)
    if not pessoa:
        raise HTTPException(status_code=401, detail="Email ou senha inválidos")
    return {"message": "Login realizado com sucesso"} 