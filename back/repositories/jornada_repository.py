from back.domain.models import Barbeiro, Jornada, Horario
from datetime import date, time

class JornadaRepository:
    
    
    def definir_jornada(self, barbeiro: Barbeiro, dia: date, turno: str):
        jornada = Jornada(dia, turno)
        barbeiro.definir_jornada(jornada)
        return jornada

    def editar_jornada(self, jornada: Jornada, novo_dia: date = None, novo_turno: str = None):
        if novo_dia is not None:
            jornada.dia = novo_dia
        if novo_turno is not None:
            jornada.turno = novo_turno
        return jornada

    def desativar_jornada(self, jornada: Jornada):
        for horario in jornada.horarios:
            horario.disponivel = False

    def registrar_indisponibilidade(self, jornada: Jornada, hora_inicio: time, hora_fim: time, justificativa: str = None):
        horario = Horario(hora_inicio, hora_fim)
        horario.disponivel = False
        jornada.adicionar_horario(horario)
        return horario

    def editar_horario_indisponivel(self, horario: Horario, novo_inicio: time = None, novo_fim: time = None, disponivel: bool = None):
        if novo_inicio is not None:
            horario.inicio = novo_inicio
        if novo_fim is not None:
            horario.fim = novo_fim
        if disponivel is not None:
            horario.disponivel = disponivel
        return horario

    def excluir_horario_indisponivel(self, jornada: Jornada, horario: Horario):
        if horario in jornada.horarios:
            jornada.horarios.remove(horario)
            return True
        return False 