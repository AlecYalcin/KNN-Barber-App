from typing import List, Optional
from back.domain.models import Cliente

class ClienteRepository:
    
    def __init__(self):
        self.clientes: List[Cliente] = []

    def criar_cliente(self, cpf: str, nome: str, email: str, telefone: str, senha: str) -> Cliente:
        cliente = Cliente(cpf, nome, email, telefone, senha)
        self.clientes.append(cliente)
        return cliente

    def buscar_cliente_por_cpf(self, cpf: str) -> Optional[Cliente]:
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                return cliente
        return None

    def buscar_cliente_por_email(self, email: str) -> Optional[Cliente]:
        for cliente in self.clientes:
            if cliente.email == email:
                return cliente
        return None

    def listar_clientes(self) -> List[Cliente]:
        return self.clientes

    def atualizar_dados(self, cpf: str, nome=None, email=None, telefone=None, senha=None) -> Optional[Cliente]:
        cliente = self.buscar_cliente_por_cpf(cpf)
        if not cliente:
            return None
            
        if nome is not None:
            cliente.nome = nome
        if email is not None:
            cliente.email = email
        if telefone is not None:
            cliente.telefone = telefone
        if senha is not None:
            cliente.senha = senha
            
        return cliente

    def remover_cliente(self, cpf: str) -> bool:
        cliente = self.buscar_cliente_por_cpf(cpf)
        if cliente:
            self.clientes.remove(cliente)
            return True
        return False 