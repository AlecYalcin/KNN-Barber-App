from back.domain.models import Barbeiro, HorarioDeAtendimento, StatusPagamento, MetodoPagamento
from datetime import date

class RelatorioFinanceiroRepository:
    
    
    def listar_pagamentos_realizados(self, agendamentos: list, barbeiro: Barbeiro, data_inicio: date = None, data_fim: date = None, metodo: MetodoPagamento = None):
        resultados = []
        for ag in agendamentos:
            if ag.barbeiro == barbeiro and ag.pagamento.status == StatusPagamento.CONCLUIDO:
                resultados.append(ag)
        
        if data_inicio:
            resultados = [ag for ag in resultados if ag.jornada.dia >= data_inicio]
        if data_fim:
            resultados = [ag for ag in resultados if ag.jornada.dia <= data_fim]
        if metodo:
            resultados = [ag for ag in resultados if ag.pagamento.metodo == metodo]
        return resultados

    def confirmar_pagamento(self, agendamento: HorarioDeAtendimento):
        agendamento.pagamento.confirmar()
        return agendamento

    def calcular_metricas(self, agendamentos: list, barbeiro: Barbeiro):
        pagamentos = [ag for ag in agendamentos if ag.barbeiro == barbeiro and ag.pagamento.status == StatusPagamento.CONCLUIDO]
        total = sum(ag.pagamento.valor for ag in pagamentos)
        media = total / len(pagamentos) if pagamentos else 0
        return {
            "total_recebido": total,
            "media_por_pagamento": media,
            "quantidade_pagamentos": len(pagamentos)
        } 