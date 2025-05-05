from back.domain.models import HorarioDeAtendimento, MetodoPagamento
from ..repositories.pagamento_repository import PagamentoRepository

class PagamentoService:
    
    
    def __init__(self):
        self.repository = PagamentoRepository()

    def exibir_valor_total(self, agendamento: HorarioDeAtendimento):
    
        if not self.validar_agendamento(agendamento):
            raise Exception("Agendamento inválido")
        
        return self.repository.exibir_valor_total(agendamento)

    def listar_formas_pagamento(self):
    
        return self.repository.listar_formas_pagamento()

    def selecionar_forma_pagamento(self, agendamento: HorarioDeAtendimento, metodo: MetodoPagamento):
    
        if not self.validar_agendamento(agendamento):
            raise Exception("Agendamento inválido")
        
        if not self.validar_metodo_pagamento(metodo):
            raise Exception("Método de pagamento inválido")
        
        return self.repository.selecionar_forma_pagamento(agendamento, metodo)

    def alterar_forma_pagamento(self, agendamento: HorarioDeAtendimento, novo_metodo: MetodoPagamento):
    
        if not self.validar_agendamento(agendamento):
            raise Exception("Agendamento inválido")
        
        if not self.validar_metodo_pagamento(novo_metodo):
            raise Exception("Método de pagamento inválido")
        
        if not self.validar_alteracao_pagamento(agendamento):
            raise Exception("Não é possível alterar o método de pagamento neste momento")
        
        return self.repository.alterar_forma_pagamento(agendamento, novo_metodo)

    def confirmar_detalhes_pagamento(self, agendamento: HorarioDeAtendimento):
    
        if not self.validar_agendamento(agendamento):
            raise Exception("Agendamento inválido")
        
        if not self.validar_pagamento(agendamento):
            raise Exception("Pagamento inválido")
        
        return self.repository.confirmar_detalhes_pagamento(agendamento)

    def validar_agendamento(self, agendamento: HorarioDeAtendimento) -> bool:
    
        # Implementar lógica de validação
        return True

    def validar_metodo_pagamento(self, metodo: MetodoPagamento) -> bool:
        
        # Implementar lógica de validação
        return True

    def validar_alteracao_pagamento(self, agendamento: HorarioDeAtendimento) -> bool:
        
        # Implementar lógica de validação
        return True

    def validar_pagamento(self, agendamento: HorarioDeAtendimento) -> bool:
        
        # Implementar lógica de validação
        return True 