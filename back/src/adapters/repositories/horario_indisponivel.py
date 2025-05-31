from src.adapters.repository import AbstractSQLAlchemyRepository
from src.domain.models import HorarioIndisponivel
from datetime import datetime

class HorarioIndisponivelRepository(AbstractSQLAlchemyRepository):
    def adicionar(self, HorarioIndisponivel: HorarioIndisponivel):
        self.session.add(HorarioIndisponivel)
    
    def remover(self, id: str):
        HorarioIndisponivel = self.consultar_por_id(id)
        self.session.delete(HorarioIndisponivel)

    def consultar_por_id(self, id: str) -> HorarioIndisponivel|None:
        horario_indisponivel = self.session.query(HorarioIndisponivel).filter(HorarioIndisponivel.id == id).first()
        return horario_indisponivel
    
    def consultar_por_barbeiro(self, cpf: str) -> list[HorarioIndisponivel]:
        horarios_indisponiveis = self.session.query(HorarioIndisponivel).filter(HorarioIndisponivel.barbeiro_cpf == cpf).all()
        return horarios_indisponiveis
    
    def consultar_por_horario(self, horarios: tuple[datetime,datetime]) -> list[HorarioIndisponivel]:
        horarios_indisponiveis = self.session.query(HorarioIndisponivel).filter(
            horarios[1] > HorarioIndisponivel.horario_inicio,
            horarios[0] < HorarioIndisponivel.horario_fim  
        ).all()
        return horarios_indisponiveis
