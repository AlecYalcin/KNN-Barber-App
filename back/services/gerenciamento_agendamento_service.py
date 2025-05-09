from back.domain.models import (
    Barbeiro, HorarioDeAtendimento, Jornada, Horario, StatusServico
)
from datetime import date
from ..repositories.gerenciamento_agendamento_repository import GerenciamentoAgendamentoRepository

class GerenciamentoAgendamentoService:
    
    def __init__(self):
        self.repository = GerenciamentoAgendamentoRepository()

    def listar_agendamentos_do_dia(self, agendamentos: list, barbeiro: Barbeiro, dia: date):
        if not self.validar_barbeiro(barbeiro):
            raise Exception("Barbeiro inválido")
        
        if not self.validar_data(dia):
            raise Exception("Data inválida")
        
        return self.repository.listar_agendamentos_do_dia(agendamentos, barbeiro, dia)

    def listar_historico_agendamentos(self, agendamentos: list, barbeiro: Barbeiro, status: StatusServico = None):
        if not self.validar_barbeiro(barbeiro):
            raise Exception("Barbeiro inválido")
        
        if status and not self.validar_status(status):
            raise Exception("Status inválido")
        
        return self.repository.listar_historico_agendamentos(agendamentos, barbeiro, status)

    def cancelar_agendamento(self, agendamento: HorarioDeAtendimento, justificativa: str):
        if not self.validar_agendamento(agendamento):
            raise Exception("Agendamento inválido")
        
        if not self.validar_justificativa(justificativa):
            raise Exception("Justificativa inválida")
        
        if not self.validar_cancelamento(agendamento):
            raise Exception("Não é possível cancelar o agendamento neste momento")
        
        return self.repository.cancelar_agendamento(agendamento, justificativa)

    def registrar_indisponibilidade_emergencial(self, jornada: Jornada, hora_inicio, hora_fim, justificativa: str = None):
        if not self.validar_jornada(jornada):
            raise Exception("Jornada inválida")
        
        if not self.validar_horario(hora_inicio, hora_fim):
            raise Exception("Horário inválido")
        
        if justificativa and not self.validar_justificativa(justificativa):
            raise Exception("Justificativa inválida")
        
        if self.verificar_conflitos(jornada, hora_inicio, hora_fim):
            raise Exception("Existem conflitos de horário")
        
        return self.repository.registrar_indisponibilidade_emergencial(jornada, hora_inicio, hora_fim, justificativa)

    def checar_conflitos(self, jornada: Jornada, hora_inicio, hora_fim):
        if not self.validar_jornada(jornada):
            raise Exception("Jornada inválida")
        
        if not self.validar_horario(hora_inicio, hora_fim):
            raise Exception("Horário inválido")
        
        return self.repository.checar_conflitos(jornada, hora_inicio, hora_fim)

    def validar_barbeiro(self, barbeiro: Barbeiro) -> bool:
        # Implementar lógica de validação
        return True

    def validar_data(self, data: date) -> bool:
        # Implementar lógica de validação
        return True

    def validar_status(self, status: StatusServico) -> bool:
        # Implementar lógica de validação
        return True

    def validar_agendamento(self, agendamento: HorarioDeAtendimento) -> bool:
        # Implementar lógica de validação
        return True

    def validar_justificativa(self, justificativa: str) -> bool:
        # Implementar lógica de validação
        return True

    def validar_cancelamento(self, agendamento: HorarioDeAtendimento) -> bool:
        # Implementar lógica de validação
        return True

    def validar_jornada(self, jornada: Jornada) -> bool:
        # Implementar lógica de validação
        return True

    def validar_horario(self, hora_inicio, hora_fim) -> bool:
        # Implementar lógica de validação
        return True

    def verificar_conflitos(self, jornada: Jornada, hora_inicio, hora_fim) -> bool:
        # Implementar lógica de verificação
        return False 