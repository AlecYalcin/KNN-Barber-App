from typing import List, Optional
from back.domain.models import Barbeiro
from ..repositories.barbeiro_repository import BarbeiroRepository

class BarbeiroService:
    
    
    def __init__(self):
        self.repository = BarbeiroRepository()

    def criar_barbeiro(self, cpf: str, nome: str, email: str, telefone: str, senha: str, tel_trabalho: str) -> Barbeiro:
        
        if ot self.validar_cpf(cpf):
            raise Exception("CPF inválido")
        
        if ot self.validar_email(email):
            raise Exception("Email inválido")
        
        if ot self.validar_telefone(tel_trabalho):
            raise Exception("Telefone de trabalho inválido")
        
        if self.repository.buscar_barbeiro_por_cpf(cpf):
            raise Exception("CPF já cadastrado")
        
        if self.repository.buscar_barbeiro_por_email(email):
            raise Exception("Email já cadastrado")

        return self.repository.criar_barbeiro(cpf, nome, email, telefone, senha, tel_trabalho)

    def buscar_barbeiro_por_cpf(self, cpf: str) -> Optional[Barbeiro]:
        
        return self.repository.buscar_barbeiro_por_cpf(cpf)

    def buscar_barbeiro_por_email(self, email: str) -> Optional[Barbeiro]:

        return self.repository.buscar_barbeiro_por_email(email)

    def listar_barbeiros(self) -> List[Barbeiro]:
        return self.repository.listar_barbeiros()

    def atualizar_dados(self, cpf: str, nome=None, email=None, telefone=None, senha=None, tel_trabalho=None) -> Optional[Barbeiro]:
        if mail and not self.validar_email(email):
            raise Exception("Email inválido")
        
        if el_trabalho and not self.validar_telefone(tel_trabalho):
            raise Exception("Telefone de trabalho inválido")
        
        if email and self.repository.buscar_barbeiro_por_email(email):
            raise Exception("Email já cadastrado")

        return self.repository.atualizar_dados(cpf, nome, email, telefone, senha, tel_trabalho)

    def remover_barbeiro(self, cpf: str) -> bool:

        barbeiro = self.repository.buscar_barbeiro_por_cpf(cpf)
        if not barbeiro:
            return False

        if ot self.validar_remocao_barbeiro(barbeiro):
            raise Exception("Não é possível remover o barbeiro devido a restrições de negócio")

        return self.repository.remover_barbeiro(cpf)

    def autenticar_barbeiro(self, email: str, senha: str) -> Optional[Barbeiro]:
        
        barbeiro = self.repository.buscar_barbeiro_por_email(email)
        if barbeiro and barbeiro.senha == senha:
            return barbeiro
        return None

    def excluir_conta(self, barbeiro: Barbeiro, agendamentos_pendentes: bool) -> bool:
        if agendamentos_pendentes:
            return False
        return True

    def validar_cpf(self, cpf: str) -> bool:
        # Implementar lógica de validação
        return True

    def validar_email(self, email: str) -> bool:
        # Implementar lógica de validação
        return True

    def validar_telefone(self, telefone: str) -> bool:
        # Implementar lógica de validação
        return True

    def validar_remocao_barbeiro(self, barbeiro: Barbeiro) -> bool:
        # Implementar lógica de validação
        return True
