from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date

from back.services.barbeiro_service import BarbeiroService
from back.infrastructure.database.connection import get_db
from back.api.schemas.barbeiro_schema import (
    BarbeiroCreate,
    BarbeiroUpdate,
    BarbeiroResponse
)

router = APIRouter(tags=["barbeiros"])

@router.post("/", response_model=BarbeiroResponse)
def criar_barbeiro(barbeiro: BarbeiroCreate, db: Session = Depends(get_db)):
    service = BarbeiroService(db)
    try:
        novo_barbeiro = service.criar_barbeiro(
            cpf=barbeiro.cpf,
            nome=barbeiro.nome,
            email=barbeiro.email,
            telefone=barbeiro.telefone,
            senha=barbeiro.senha,
            tel_trabalho=barbeiro.tel_trabalho
        )
        db.commit()
        return novo_barbeiro
    except ValueError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{cpf}", response_model=BarbeiroResponse)
def buscar_barbeiro(cpf: str, db: Session = Depends(get_db)):
    service = BarbeiroService(db)
    barbeiro = service.buscar_barbeiro_por_cpf(cpf)
    if not barbeiro:
        raise HTTPException(status_code=404, detail="Barbeiro não encontrado")
    return barbeiro

@router.get("/", response_model=List[BarbeiroResponse])
def listar_barbeiros(db: Session = Depends(get_db)):
    service = BarbeiroService(db)
    return service.listar_barbeiros()

@router.put("/{cpf}", response_model=BarbeiroResponse)
def atualizar_barbeiro(cpf: str, barbeiro: BarbeiroUpdate, db: Session = Depends(get_db)):
    service = BarbeiroService(db)
    try:
        barbeiro_atualizado = service.atualizar_dados(
            cpf=cpf,
            **barbeiro.model_dump(exclude_unset=True)
        )
        if not barbeiro_atualizado:
            raise HTTPException(status_code=404, detail="Barbeiro não encontrado")
        db.commit()
        return barbeiro_atualizado
    except ValueError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{cpf}")
def remover_barbeiro(cpf: str, db: Session = Depends(get_db)):
    service = BarbeiroService(db)
    try:
        if not service.remover_barbeiro(cpf):
            raise HTTPException(status_code=404, detail="Barbeiro não encontrado")
        db.commit()
        return {"message": "Barbeiro removido com sucesso"}
    except ValueError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/disponiveis/{data}")
def buscar_barbeiros_disponiveis(data: date, db: Session = Depends(get_db)):
    service = BarbeiroService(db)
    return service.buscar_barbeiros_disponiveis(data) 