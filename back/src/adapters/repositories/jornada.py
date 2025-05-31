from src.adapters.repository import AbstractSQLAlchemyRepository
from src.domain.models import Jornada

class JornadaRepository(AbstractSQLAlchemyRepository):
    def adicionar(self, jornada: Jornada):
        self.session.add(jornada)
    
    def remover(self, id: str):
        jornada = self.consultar_por_id(id)
        self.session.delete(jornada)

    def consultar_por_id(self, id: str) -> Jornada|None:
        jornada = self.session.query(Jornada).filter(Jornada.id == id).first()
        return jornada
    
    def consultar_por_barbeiro_e_vigente(self, cpf: str) -> list[Jornada]:
        jornada = self.session.query(Jornada).filter(Jornada.barbeiro_cpf == cpf).all()
        return jornada
        