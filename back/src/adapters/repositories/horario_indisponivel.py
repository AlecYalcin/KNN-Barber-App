from src.adapters.repository import AbstractSQLAlchemyRepository
from src.domain.models import HorarioIndisponivel
from datetime import datetime
import abc

class AbstractHorarioIndisponivelRepository():
    @abc.abstractmethod
    def adicionar(self, horario_indisponivel: HorarioIndisponivel):
        raise NotImplementedError

    @abc.abstractmethod
    def remover(self, id: str):
        raise NotImplementedError
    
    @abc.abstractmethod
    def alterar(self, id: str, novo_horario_indisponivel: HorarioIndisponivel):
        raise NotImplementedError

    @abc.abstractmethod
    def consultar(self, id: str) -> HorarioIndisponivel|None:
        raise NotImplementedError
        
    @abc.abstractmethod
    def consultar_por_barbeiro(self, cpf: str) -> list[HorarioIndisponivel]:
        raise NotImplementedError

    @abc.abstractmethod
    def consultar_por_horario(self, horarios: tuple[datetime,datetime]) -> list[HorarioIndisponivel]:
        raise NotImplementedError

class HorarioIndisponivelRepository(AbstractHorarioIndisponivelRepository, AbstractSQLAlchemyRepository):
    def adicionar(self, horario_indisponivel: HorarioIndisponivel):
        self.session.add(horario_indisponivel)
    
    def remover(self, id: str):
        HorarioIndisponivel = self.consultar(id)
        self.session.delete(HorarioIndisponivel)

    def alterar(self, id: str, novo_horario_indisponivel: HorarioIndisponivel):
        horario_indisponivel = self.consultar(id)
        horario_indisponivel.horario_inicio = novo_horario_indisponivel.horario_inicio or horario_indisponivel.horario_inicio
        horario_indisponivel.horario_fim = novo_horario_indisponivel.horario_fim or horario_indisponivel.horario_fim
        horario_indisponivel.justificativa = novo_horario_indisponivel.justificativa or horario_indisponivel.justificativa

    def consultar(self, id: str) -> HorarioIndisponivel|None:
        horario_indisponivel = self.session.query(HorarioIndisponivel).filter(HorarioIndisponivel.id == id).first()
        return horario_indisponivel
    
    def consultar_por_barbeiro(self, cpf: str) -> list[HorarioIndisponivel]:
        horarios_indisponiveis = self.session.query(HorarioIndisponivel).filter(HorarioIndisponivel.barbeiro_cpf == cpf).all()
        return horarios_indisponiveis
    
    def consultar_por_horario(self, horarios: tuple[datetime,datetime]) -> list[HorarioIndisponivel]:
        horarios_indisponiveis = self.session.query(HorarioIndisponivel).filter(
            horarios[1] >= HorarioIndisponivel.horario_inicio,
            horarios[0] <= HorarioIndisponivel.horario_fim  
        ).all()
        return horarios_indisponiveis
