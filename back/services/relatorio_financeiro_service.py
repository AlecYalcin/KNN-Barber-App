from back.domain.models import Barbeiro, HorarioDeAtendimento, StatusPagamento, MetodoPagamento
from datetime import date
from ..repositories.relatorio_financeiro_repository import RelatorioFinanceiroRepository

class RelatorioFinanceiroService:
    
    def __init__(self):
        self.repository = RelatorioFinanceiroRepository()

    def listar_pagamentos_realizados(self, agendamentos: list, barbeiro: Barbeiro, data_inicio: date = None, data_fim: date = None, metodo: MetodoPagamento = None):

        if not self.validar_datas(data_inicio, data_fim):
            raise Exception("Datas inválidas para o período de consulta")
        
        if not self.validar_barbeiro(barbeiro):
            raise Exception("Barbeiro inválido")
        
        if metodo and not self.validar_metodo_pagamento(metodo):
            raise Exception("Método de pagamento inválido")

        return self.repository.listar_pagamentos_realizados(agendamentos, barbeiro, data_inicio, data_fim, metodo)

    def confirmar_pagamento(self, agendamento: HorarioDeAtendimento):

        if not self.validar_agendamento(agendamento):
            raise Exception("Agendamento inválido")
        
        if not self.validar_confirmacao_pagamento(agendamento):
            raise Exception("Não é possível confirmar o pagamento neste momento")
        
        return self.repository.confirmar_pagamento(agendamento)

    def calcular_metricas(self, agendamentos: list, barbeiro: Barbeiro):

        if not self.validar_barbeiro(barbeiro):
            raise Exception("Barbeiro inválido")
        
        if not self.validar_agendamentos(agendamentos):
            raise Exception("Lista de agendamentos inválida")
        
        return self.repository.calcular_metricas(agendamentos, barbeiro)

    def validar_datas(self, data_inicio: date, data_fim: date) -> bool:
        
        if data_inicio and data_fim and data_inicio > data_fim:
            return False
        return True

    def validar_barbeiro(self, barbeiro: Barbeiro) -> bool:
        
        # Implementar lógica de validação
        return True

    def validar_metodo_pagamento(self, metodo: MetodoPagamento) -> bool:
        
        # Implementar lógica de validação
        return True

    def validar_agendamento(self, agendamento: HorarioDeAtendimento) -> bool:
        
        # Implementar lógica de validação
        return True

    def validar_confirmacao_pagamento(self, agendamento: HorarioDeAtendimento) -> bool:
        
        # Implementar lógica de validação
        return True

    def validar_agendamentos(self, agendamentos: list) -> bool:
        
        # Implementar lógica de validação
        return True 