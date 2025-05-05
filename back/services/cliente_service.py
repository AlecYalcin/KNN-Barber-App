from typing import List, Optional
from back.domain.models import Cliente
from ..repositories.cliente_repository import ClienteRepository

class ClienteService:
    
    def __init__(self):
        self.repository = ClienteRepository()

    def criar_cliente(self, cpf: str, nome: str, email: str, telefone: str, senha: str) -> Cliente:
        if not self.validar_cpf(cpf):
            raise Exception("CPF inválido")
        
        if not self.validar_email(email):
            raise Exception("Email inválido")
        
        if self.repository.buscar_cliente_por_cpf(cpf):
            raise Exception("CPF já cadastrado")
        
        if self.repository.buscar_cliente_por_email(email):
            raise Exception("Email já cadastrado")

        return self.repository.criar_cliente(cpf, nome, email, telefone, senha)

    def buscar_cliente_por_cpf(self, cpf: str) -> Optional[Cliente]:
        return self.repository.buscar_cliente_por_cpf(cpf)

    def buscar_cliente_por_email(self, email: str) -> Optional[Cliente]:
        return self.repository.buscar_cliente_por_email(email)

    def listar_clientes(self) -> List[Cliente]:
        return self.repository.listar_clientes()

    def atualizar_dados(self, cpf: str, nome=None, email=None, telefone=None, senha=None) -> Optional[Cliente]:
        if email and not self.validar_email(email):
            raise Exception("Email inválido")
        
        if email and self.repository.buscar_cliente_por_email(email):
            raise Exception("Email já cadastrado")

        return self.repository.atualizar_dados(cpf, nome, email, telefone, senha)

    def remover_cliente(self, cpf: str) -> bool:
        cliente = self.repository.buscar_cliente_por_cpf(cpf)
        if not cliente:
            return False

        if not self.validar_remocao_cliente(cliente):
            raise Exception("Não é possível remover o cliente devido a restrições de negócio")

        return self.repository.remover_cliente(cpf)

    def autenticar_cliente(self, email: str, senha: str) -> Optional[Cliente]:
        cliente = self.repository.buscar_cliente_por_email(email)
        if cliente and cliente.senha == senha:
            return cliente
        return None

    def excluir_conta(self, cliente: Cliente, agendamentos_pendentes: bool) -> bool:
        if agendamentos_pendentes:
            return False
        return True

    def validar_cpf(self, cpf: str) -> bool:
        # Implementar lógica de validação
        return True

    def validar_email(self, email: str) -> bool:
        # Implementar lógica de validação
        return True

    def validar_remocao_cliente(self, cliente: Cliente) -> bool:
        # Implementar lógica de validação
        return True 