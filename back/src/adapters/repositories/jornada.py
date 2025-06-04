from src.adapters.repository import AbstractSQLAlchemyRepository
from src.domain.models import Jornada
import abc

class AbstractJornadaRepository():
    @abc.abstractmethod
    def adicionar(self, jornada: Jornada):
        raise NotImplementedError
    
    @abc.abstractmethod
    def remover(self, id: str):
        raise NotImplementedError

    @abc.abstractmethod
    def consultar(self, id: str) -> Jornada|None:
        raise NotImplementedError

    @abc.abstractmethod
    def listar_jornada_de_barbeiro(self, cpf: str) -> list[Jornada]:
        raise NotImplementedError        

class JornadaRepository(AbstractJornadaRepository, AbstractSQLAlchemyRepository):
    def adicionar(self, jornada: Jornada):
        self.session.add(jornada)
    
    def remover(self, id: str):
        jornada = self.consultar(id)
        self.session.delete(jornada)

    def consultar(self, id: str) -> Jornada|None:
        jornada = self.session.query(Jornada).filter(Jornada.id == id).first()
        return jornada
    
    def listar_jornada_de_barbeiro(self, cpf: str) -> list[Jornada]:
        jornada = self.session.query(Jornada).filter(
            Jornada.barbeiro_cpf == cpf,
            Jornada.ativa,
        ).all()
        return jornada
        