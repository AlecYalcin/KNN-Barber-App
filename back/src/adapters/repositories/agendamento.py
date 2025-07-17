from src.domain.models import Agendamento
from src.adapters.repository import AbstractSQLAlchemyRepository
from datetime import datetime
import abc

class AbstractAgendamentoRepository():
    @abc.abstractmethod
    def adicionar(self, agendamento: Agendamento):
        raise NotImplementedError

    @abc.abstractmethod
    def remover(self, id: str):
        raise NotImplementedError

    @abc.abstractmethod
    def consultar(self, id: str) -> Agendamento | None:
        raise NotImplementedError

    @abc.abstractmethod
    def listar(self) -> list[Agendamento]:
        raise NotImplementedError

    @abc.abstractmethod
    def listar_por_horario(self, horarios: tuple[datetime,datetime]) -> list[Agendamento]:
        raise NotImplementedError
    
    @abc.abstractmethod
    def listar_por_barbeiro(self, barbeiro_id: str) -> list[Agendamento]:
        raise NotImplementedError
    
    @abc.abstractmethod
    def listar_por_cliente(self, cliente_cpf: str) -> list[Agendamento]:
        raise NotImplementedError

class AgendamentoRepository(AbstractAgendamentoRepository, AbstractSQLAlchemyRepository):
    def adicionar(self, agendamento: Agendamento):
        self.session.add(agendamento)

    def remover(self, id: str):
        agendamento = self.consultar(id)
        self.session.delete(agendamento)

    def consultar(self, id: str) -> Agendamento | None:
        agendamento = self.session.query(Agendamento).filter(Agendamento.id == id).first()
        return agendamento

    def listar(self) -> list[Agendamento]:
        agendamentos = self.session.query(Agendamento).all()
        return agendamentos
    
    def listar_por_horario(self, horarios: tuple[datetime,datetime]) -> list[Agendamento]:
        agendamentos = self.session.query(Agendamento).filter(
            horarios[1] > Agendamento.horario_inicio,
            horarios[0] < Agendamento.horario_fim  
        ).all()
        return agendamentos
    
    def listar_por_barbeiro(self, barbeiro_cpf: str) -> list[Agendamento]:
        agendamentos = self.session.query(Agendamento).filter(Agendamento.barbeiro_cpf == barbeiro_cpf).all()
        return agendamentos
    
    def listar_por_cliente(self, cliente_cpf: str) -> list[Agendamento]:
        agendamentos = self.session.query(Agendamento).filter(Agendamento.cliente_cpf == cliente_cpf).all()
        return agendamentos
