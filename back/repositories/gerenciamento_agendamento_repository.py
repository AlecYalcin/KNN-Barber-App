from back.domain.models import Barbeiro, HorarioDeAtendimento, Jornada, StatusServico
from datetime import date, time

class GerenciamentoAgendamentoRepository:
    
    def listar_agendamentos_do_dia(self, agendamentos: list, barbeiro: Barbeiro, dia: date):
        
        resultados = []
        for ag in agendamentos:
            if ag.barbeiro == barbeiro and ag.jornada.dia == dia:
                resultados.append(ag)
        return resultados

    def listar_historico_agendamentos(self, agendamentos: list, barbeiro: Barbeiro, status: StatusServico = None):

        resultados = [ag for ag in agendamentos if ag.barbeiro == barbeiro]
        if status:
            resultados = [ag for ag in resultados if ag.status == status]
        return resultados

    def cancelar_agendamento(self, agendamento: HorarioDeAtendimento, justificativa: str):

        agendamento.status = StatusServico.CANCELADO
        agendamento.justificativa = justificativa
        return agendamento

    def registrar_indisponibilidade_emergencial(self, jornada: Jornada, hora_inicio: time, hora_fim: time, justificativa: str = None):

        horario = Horario(hora_inicio, hora_fim)
        horario.disponivel = False
        horario.justificativa = justificativa
        jornada.adicionar_horario(horario)
        return horario

    def checar_conflitos(self, jornada: Jornada, hora_inicio: time, hora_fim: time):

        for horario in jornada.horarios:
            if (hora_inicio <= horario.fim and hora_fim >= horario.inicio):
                return True
        return False 