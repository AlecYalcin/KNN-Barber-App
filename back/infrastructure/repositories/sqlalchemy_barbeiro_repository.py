from datetime import date
from typing import List, Optional
from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from back.domain.models import Barbeiro
from back.domain.repositories.barbeiro_repository import IBarbeiroRepository

class SQLAlchemyBarbeiroRepository(IBarbeiroRepository):
    def __init__(self, session: Session):
        self.session = session

    def adicionar(self, barbeiro: Barbeiro) -> None:
        self.session.add(barbeiro)
        
    def obter(self, id: str) -> Optional[Barbeiro]:
        return self.session.get(Barbeiro, id)
        
    def listar(self) -> List[Barbeiro]:
        stmt = select(Barbeiro)
        return list(self.session.execute(stmt).scalars())
        
    def remover(self, id: str) -> None:
        barbeiro = self.obter(id)
        if barbeiro:
            self.session.delete(barbeiro)
            
    def buscar_por_email(self, email: str) -> Optional[Barbeiro]:
        stmt = select(Barbeiro).where(Barbeiro.email == email)
        return self.session.execute(stmt).scalar_one_or_none()
        
    def buscar_por_cpf(self, cpf: str) -> Optional[Barbeiro]:
        return self.session.get(Barbeiro, cpf)
        
    def buscar_disponiveis_por_data(self, data: date) -> List[Barbeiro]:
        stmt = (
            select(Barbeiro)
            .join(Barbeiro.jornadas)
            .where(Barbeiro.jornadas.any(dia=data))
        )
        return list(self.session.execute(stmt).scalars())
        
    def buscar_com_jornadas(self) -> List[Barbeiro]:
        stmt = (
            select(Barbeiro)
            .options(joinedload(Barbeiro.jornadas))
        )
        return list(self.session.execute(stmt).scalars()) 