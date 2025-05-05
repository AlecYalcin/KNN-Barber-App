from back.domain.models import Barbeiro, Jornada, Horario
from datetime import date, time
from ..repositories.jornada_repository import JornadaRepository

class JornadaService:
    
    
    def __init__(self):
        self.repository = JornadaRepository()

    def definir_jornada(self, barbeiro: Barbeiro, dia: date, turno: str):
       
        if ot self.validar_barbeiro(barbeiro):
            raise Exception("Barbeiro inválido")
        
        if not self.validar_data(dia):
            raise Exception("Data inválida")
        
        if not self.validar_turno(turno):
            raise Exception("Turno inválido")
        
        if not self.validar_disponibilidade_barbeiro(barbeiro, dia):
            raise Exception("Barbeiro já possui jornada definida para esta data")

        return self.repository.definir_jornada(barbeiro, dia, turno)

    def editar_jornada(self, jornada: Jornada, novo_dia: date = None, novo_turno: str = None):
       
        if not self.validar_jornada(jornada):
            raise Exception("Jornada inválida")
        
        if novo_dia and not self.validar_data(novo_dia):
            raise Exception("Nova data inválida")
        
        if novo_turno and not self.validar_turno(novo_turno):
            raise Exception("Novo turno inválido")
        
        if not self.validar_edicao_jornada(jornada):
            raise Exception("Não é possível editar a jornada neste momento")

        return self.repository.editar_jornada(jornada, novo_dia, novo_turno)

    def desativar_jornada(self, jornada: Jornada):
       
        if not self.validar_jornada(jornada):
            raise Exception("Jornada inválida")
        
        if not self.validar_desativacao_jornada(jornada):
            raise Exception("Não é possível desativar a jornada neste momento")

        self.repository.desativar_jornada(jornada)

    def registrar_indisponibilidade(self, jornada: Jornada, hora_inicio: time, hora_fim: time, justificativa: str = None):
        if not self.validar_jornada(jornada):
            raise Exception("Jornada inválida")
        
        if not self.validar_horario(hora_inicio, hora_fim):
            raise Exception("Horário inválido")
        
        if not self.validar_justificativa(justificativa):
            raise Exception("Justificativa inválida")
        
        if self.verificar_conflitos(jornada, hora_inicio, hora_fim):
            raise Exception("Existem conflitos de horário")

        return self.repository.registrar_indisponibilidade(jornada, hora_inicio, hora_fim, justificativa)

    def editar_horario_indisponivel(self, horario: Horario, novo_inicio: time = None, novo_fim: time = None, disponivel: bool = None):
        
        if not self.validar_horario(horario.inicio, horario.fim):
            raise Exception("Horário inválido")
        
        if novo_inicio and novo_fim and not self.validar_horario(novo_inicio, novo_fim):
            raise Exception("Novo horário inválido")
        
        if not self.validar_edicao_horario(horario):
            raise Exception("Não é possível editar o horário neste momento")

        return self.repository.editar_horario_indisponivel(horario, novo_inicio, novo_fim, disponivel)

    def excluir_horario_indisponivel(self, jornada: Jornada, horario: Horario):
        if not self.validar_jornada(jornada):
            raise Exception("Jornada inválida")
        
        if not self.validar_horario(horario.inicio, horario.fim):
            raise Exception("Horário inválido")
        
        if not self.validar_exclusao_horario(horario):
            raise Exception("Não é possível excluir o horário neste momento")

        return self.repository.excluir_horario_indisponivel(jornada, horario)

    def validar_barbeiro(self, barbeiro: Barbeiro) -> bool:
        
        return True

    def validar_data(self, data: date) -> bool:

        return True

    def validar_turno(self, turno: str) -> bool:

        return True

    def validar_disponibilidade_barbeiro(self, barbeiro: Barbeiro, dia: date) -> bool:

        return True

    def validar_jornada(self, jornada: Jornada) -> bool:

        return True

    def validar_edicao_jornada(self, jornada: Jornada) -> bool:

        return True

    def validar_desativacao_jornada(self, jornada: Jornada) -> bool:

        return True

    def validar_horario(self, hora_inicio: time, hora_fim: time) -> bool:

        return True

    def validar_justificativa(self, justificativa: str) -> bool:

        return True

    def verificar_conflitos(self, jornada: Jornada, hora_inicio: time, hora_fim: time) -> bool:

        return False

    def validar_edicao_horario(self, horario: Horario) -> bool:

        return True

    def validar_exclusao_horario(self, horario: Horario) -> bool:

        return True 