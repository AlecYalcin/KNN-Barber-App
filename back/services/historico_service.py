from back.domain.models import Cliente, HorarioDeAtendimento
from datetime import date
from ..repositories.historico_repository import HistoricoRepository

class HistoricoService:
    
    def __init__(self):
        self.repository = HistoricoRepository()

    def listar_historico(self, agendamentos: list, cliente: Cliente, data_inicio: date = None, data_fim: date = None):
        if not self.validar_datas(data_inicio, data_fim):
            raise Exception("Datas inválidas para o período de consulta")
        
        return self.repository.listar_historico(agendamentos, cliente, data_inicio, data_fim)

    def filtrar_por_servico(self, agendamentos: list, servico_id: str):
        if not self.validar_servico_id(servico_id):
            raise Exception("ID do serviço inválido")
        
        return self.repository.filtrar_por_servico(agendamentos, servico_id)

    def visualizar_detalhes(self, agendamento: HorarioDeAtendimento):
        if not self.validar_agendamento(agendamento):
            raise Exception("Agendamento inválido")
        
        return self.repository.visualizar_detalhes(agendamento)

    def exportar_historico(self, agendamentos: list):
        if not self.validar_agendamentos(agendamentos):
            raise Exception("Lista de agendamentos inválida")
        
        return self.repository.exportar_historico(agendamentos)

    def validar_datas(self, data_inicio: date, data_fim: date) -> bool:
        if data_inicio and data_fim and data_inicio > data_fim:
            return False
        return True

    def validar_servico_id(self, servico_id: str) -> bool:
        # Implementar lógica de validação
        return True

    def validar_agendamento(self, agendamento: HorarioDeAtendimento) -> bool:
        # Implementar lógica de validação
        return True

    def validar_agendamentos(self, agendamentos: list) -> bool:
        # Implementar lógica de validação
        return True 