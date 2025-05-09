from typing import List, Optional
from back.domain.models import Barbeiro

class BarbeiroRepository:
    
    def __init__(self):
        self.barbeiros: List[Barbeiro] = []

    def criar_barbeiro(self, cpf: str, nome: str, email: str, telefone: str, senha: str, tel_trabalho: str) -> Barbeiro:
        barbeiro = Barbeiro(cpf, nome, email, telefone, senha, tel_trabalho)
        self.barbeiros.append(barbeiro)
        return barbeiro

    def buscar_barbeiro_por_cpf(self, cpf: str) -> Optional[Barbeiro]:
        for barbeiro in self.barbeiros:
            if barbeiro.cpf == cpf:
                return barbeiro
        return None

    def buscar_barbeiro_por_email(self, email: str) -> Optional[Barbeiro]:
        for barbeiro in self.barbeiros:
            if barbeiro.email == email:
                return barbeiro
        return None

    def listar_barbeiros(self) -> List[Barbeiro]:
        return self.barbeiros

    def atualizar_dados(self, cpf: str, nome=None, email=None, telefone=None, senha=None, tel_trabalho=None) -> Optional[Barbeiro]:
        barbeiro = self.buscar_barbeiro_por_cpf(cpf)
        if not barbeiro:
            return None
            
        if nome is not None:
            barbeiro.nome = nome
        if email is not None:
            barbeiro.email = email
        if telefone is not None:
            barbeiro.telefone = telefone
        if senha is not None:
            barbeiro.senha = senha
        if tel_trabalho is not None:
            barbeiro.tel_trabalho = tel_trabalho
            
        return barbeiro

    def remover_barbeiro(self, cpf: str) -> bool:
        barbeiro = self.buscar_barbeiro_por_cpf(cpf)
        if barbeiro:
            self.barbeiros.remove(barbeiro)
            return True
        return False 