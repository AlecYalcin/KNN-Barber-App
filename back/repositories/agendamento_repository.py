from back.domain.models import (
    Cliente, Barbeiro, Servico, Jornada, Horario, MetodoPagamento,
    criar_horario_de_atendimento, StatusServico
)

class AgendamentoRepository:
    
    @staticmethod
    def listar_servicos(servicos: list):
        return [s for s in servicos] 

    @staticmethod
    def listar_horarios_disponiveis(jornada: Jornada):
        return [h for h in jornada.horarios if h.disponivel]

    @staticmethod
    def calcular_duracao_total(servicos: list):
        return sum(s.duracao for s in servicos)

    @staticmethod
    def calcular_valor_total(servicos: list):
        return sum(s.valor_base for s in servicos)

    @staticmethod
    def agendar(
        cliente: Cliente,
        barbeiro: Barbeiro,
        jornada: Jornada,
        horario: Horario,
        servico: Servico,
        metodo_pagamento: MetodoPagamento,
        adicional: float = 0
    ):
        if not horario.disponivel:
            raise Exception("Horário não está mais disponível")
        atendimento = criar_horario_de_atendimento(
            cliente, barbeiro, jornada, horario, servico, metodo_pagamento, adicional
        )
        return atendimento

    @staticmethod
    def cancelar_agendamento(agendamento, justificativa: str):
        agendamento.cancelar(justificativa)
        return agendamento 