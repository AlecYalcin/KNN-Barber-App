from back.domain.models import HorarioDeAtendimento, MetodoPagamento

class PagamentoRepository:
    
    
    def exibir_valor_total(self, agendamento: HorarioDeAtendimento):
        return agendamento.pagamento.valor

    def listar_formas_pagamento(self):
        return [m.value for m in MetodoPagamento]

    def selecionar_forma_pagamento(self, agendamento: HorarioDeAtendimento, metodo: MetodoPagamento):
        agendamento.pagamento.metodo = metodo
        return agendamento

    def alterar_forma_pagamento(self, agendamento: HorarioDeAtendimento, novo_metodo: MetodoPagamento):
        agendamento.pagamento.metodo = novo_metodo
        return agendamento

    def confirmar_detalhes_pagamento(self, agendamento: HorarioDeAtendimento):
        return {
            "valor_total": agendamento.pagamento.valor,
            "forma_pagamento": agendamento.pagamento.metodo.value
        } 