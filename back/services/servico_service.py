from back.domain.models import Servico
from ..repositories.servico_repository import ServicoRepository

class ServicoService:
    
    def __init__(self):
        self.repository = ServicoRepository()

    def cadastrar_servico(self, id: str, nome: str, descricao: str, valor_base: float, duracao: int = 30):
        
        if not self.validar_id(id):
            raise Exception("ID inválido")
        
        if not self.validar_nome(nome):
            raise Exception("Nome inválido")
        
        if not self.validar_valor(valor_base):
            raise Exception("Valor inválido")
        
        if not self.validar_duracao(duracao):
            raise Exception("Duração inválida")
        
        if self.repository.buscar_servico_por_id(id):
            raise Exception("ID já cadastrado")

        return self.repository.cadastrar_servico(id, nome, descricao, valor_base, duracao)

    def editar_servico(self, servico: Servico, nome: str = None, descricao: str = None, valor_base: float = None, duracao: int = None):

        if not self.validar_servico(servico):
            raise Exception("Serviço inválido")
        
        if nome and not self.validar_nome(nome):
            raise Exception("Nome inválido")
        
        if valor_base and not self.validar_valor(valor_base):
            raise Exception("Valor inválido")
        
        if duracao and not self.validar_duracao(duracao):
            raise Exception("Duração inválida")

        return self.repository.editar_servico(servico, nome, descricao, valor_base, duracao)

    def excluir_servico(self, servico: Servico):
        if not self.validar_servico(servico):
            raise Exception("Serviço inválido")
        
        if not self.validar_exclusao(servico):
            raise Exception("Não é possível excluir o serviço devido a restrições de negócio")

        return self.repository.excluir_servico(servico)

    def listar_servicos(self):
        return self.repository.listar_servicos()

    def buscar_servico_por_id(self, id: str):
        return self.repository.buscar_servico_por_id(id)

    def validar_id(self, id: str) -> bool:
        # Implementar lógica de validação
        return True

    def validar_nome(self, nome: str) -> bool:
        # Implementar lógica de validação
        return True

    def validar_valor(self, valor: float) -> bool:
        # Implementar lógica de validação
        return True

    def validar_duracao(self, duracao: int) -> bool:
        # Implementar lógica de validação
        return True

    def validar_servico(self, servico: Servico) -> bool:
        # Implementar lógica de validação
        return True

    def validar_exclusao(self, servico: Servico) -> bool:
        # Implementar lógica de validação
        return True 