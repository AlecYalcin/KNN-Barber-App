from back.domain.models import Cliente, HorarioDeAtendimento
from datetime import date

class HistoricoRepository:
    
    def listar_historico(self, agendamentos: list, cliente: Cliente, data_inicio: date = None, data_fim: date = None):
        resultados = [ag for ag in agendamentos if ag.cliente == cliente]
        if data_inicio:
            resultados = [ag for ag in resultados if ag.jornada.dia >= data_inicio]
        if data_fim:
            resultados = [ag for ag in resultados if ag.jornada.dia <= data_fim]
        return resultados

    def filtrar_por_servico(self, agendamentos: list, servico_id: str):
        return [ag for ag in agendamentos if ag.servico.id == servico_id]

    def visualizar_detalhes(self, agendamento: HorarioDeAtendimento):
        return {
            "servico": agendamento.servico.nome,
            "valor": agendamento.pagamento.valor,
            "status_pagamento": agendamento.pagamento.status.value,
            "forma_pagamento": agendamento.pagamento.metodo.value,
            "data": agendamento.jornada.dia,
            "horario": (agendamento.horario.inicio, agendamento.horario.fim)
        }

    def exportar_historico(self, agendamentos: list):
        return [
            {
                "servico": ag.servico.nome,
                "valor": ag.pagamento.valor,
                "status_pagamento": ag.pagamento.status.value,
                "forma_pagamento": ag.pagamento.metodo.value,
                "data": ag.jornada.dia,
                "horario": (ag.horario.inicio, ag.horario.fim)
            }
            for ag in agendamentos
        ] 