from typing import List, Optional
from back.domain.models import Pessoa
from back.infrastructure.repositories.sqlalchemy_pessoa_repository import SQLAlchemyPessoaRepository

class PessoaService:
    def __init__(self):
        self.repository = SQLAlchemyPessoaRepository()

    def criar_pessoa(self, cpf: str, nome: str, email: str, telefone: str, senha: str) -> Pessoa:
        if not self.validar_cpf(cpf):
            raise ValueError("CPF inválido")
        
        if not self.validar_email(email):
            raise ValueError("Email inválido")
        
        if self.repository.buscar_pessoa_por_cpf(cpf):
            raise ValueError("CPF já cadastrado")
        
        if self.repository.buscar_pessoa_por_email(email):
            raise ValueError("Email já cadastrado")

        return self.repository.criar_pessoa(cpf, nome, email, telefone, senha)

    def buscar_pessoa_por_cpf(self, cpf: str) -> Optional[Pessoa]:
        return self.repository.buscar_pessoa_por_cpf(cpf)

    def buscar_pessoa_por_email(self, email: str) -> Optional[Pessoa]:
        return self.repository.buscar_pessoa_por_email(email)

    def listar_pessoas(self) -> List[Pessoa]:
        return self.repository.listar_pessoas()

    def atualizar_dados(self, cpf: str, nome=None, email=None, telefone=None, senha=None) -> Optional[Pessoa]:
        if email and not self.validar_email(email):
            raise ValueError("Email inválido")
        
        if email and self.repository.buscar_pessoa_por_email(email):
            raise ValueError("Email já cadastrado")

        return self.repository.atualizar_dados(cpf, nome, email, telefone, senha)

    def remover_pessoa(self, cpf: str) -> bool:
        pessoa = self.repository.buscar_pessoa_por_cpf(cpf)
        if not pessoa:
            return False

        return self.repository.remover_pessoa(cpf)

    def autenticar_pessoa(self, email: str, senha: str) -> Optional[Pessoa]:
        pessoa = self.repository.buscar_pessoa_por_email(email)
        if pessoa and pessoa.senha == senha:  # Em produção, usar hash da senha
            return pessoa
        return None

    def validar_cpf(self, cpf: str) -> bool:
        # Implementar validação de CPF
        return True

    def validar_email(self, email: str) -> bool:
        # Implementar validação de email
        return True 