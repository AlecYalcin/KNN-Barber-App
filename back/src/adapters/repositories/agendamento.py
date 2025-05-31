from src.domain.models import Agendamento
from src.adapters.repository import AbstractSQLAlchemyRepository
from datetime import datetime

class AgendamentoRepository(AbstractSQLAlchemyRepository):
    def adicionar(self, agendamento: Agendamento):
        self.session.add(agendamento)

    def remover(self, id: str):
        agendamento = self.consultar_por_id(id)
        self.session.delete(agendamento)

    def consultar_por_id(self, id: str) -> Agendamento | None:
        agendamento = self.session.query(Agendamento).filter(Agendamento.id == id).first()
        return agendamento

    def consultar_por_horario(self, horarios: tuple[datetime,datetime]) -> list[Agendamento]:
        agendamentos = self.session.query(Agendamento).filter(
            horarios[1] > Agendamento.horario_inicio,
            horarios[0] < Agendamento.horario_fim  
        ).all()
        return agendamentos

    def retornar_agendamentos(self) -> list[Agendamento]:
        agendamentos = self.session.query(Agendamento).all()
        return agendamentos

    