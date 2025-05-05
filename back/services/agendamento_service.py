from back.domain.models import Agendamento, Cliente, Barbeiro, Servico, Jornada, Horario, MetodoPagamento, StatusServico
from datetime import date, time
from ..repositories.agendamento_repository import AgendamentoRepository

class AgendamentoService:
    
    def __init__(self):
        self.repository = AgendamentoRepository()

    def listar_servicos(self, servicos: list):
        return self.repository.listar_servicos(servicos)

    def listar_horarios_disponiveis(self, jornada: Jornada):
        return self.repository.listar_horarios_disponiveis(jornada)

    def calcular_duracao_total(self, servicos: list):
        return self.repository.calcular_duracao_total(servicos)

    def calcular_valor_total(self, servicos: list):
        return self.repository.calcular_valor_total(servicos)

    def agendar(
        self,
        cliente: Cliente,
        barbeiro: Barbeiro,
        jornada: Jornada,
        horario: Horario,
        servico: Servico,
        metodo_pagamento: MetodoPagamento,
        adicional: float = 0
    ):

        if not self.validar_disponibilidade_barbeiro(barbeiro, horario):
            raise Exception("Barbeiro não está disponível neste horário")
        
        if not self.validar_compatibilidade_servico(servico, barbeiro):
            raise Exception("Barbeiro não está habilitado para este serviço")
        
        if not self.validar_horario_servico(servico, horario):
            raise Exception("Horário não é compatível com a duração do serviço")

        return self.repository.agendar(
            cliente, barbeiro, jornada, horario, servico, metodo_pagamento, adicional
        )

    def cancelar_agendamento(self, agendamento, justificativa: str):

        if not self.validar_prazo_cancelamento(agendamento):
            raise Exception("Não é possível cancelar o agendamento neste momento")
        
        return self.repository.cancelar_agendamento(agendamento, justificativa)

    def validar_disponibilidade_barbeiro(self, barbeiro: Barbeiro, horario: Horario) -> bool:

        # Implementar lógica de validação
        return True

    def validar_compatibilidade_servico(self, servico: Servico, barbeiro: Barbeiro) -> bool:
        # Implementar lógica de validação
        return True

    def validar_horario_servico(self, servico: Servico, horario: Horario) -> bool:
        # Implementar lógica de validação
        return True

    def validar_prazo_cancelamento(self, agendamento) -> bool:
        # Implementar lógica de validação
        return True 