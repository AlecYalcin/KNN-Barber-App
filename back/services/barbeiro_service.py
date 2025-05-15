from typing import List, Optional
from datetime import date
from back.domain.models import Barbeiro
from back.infrastructure.repositories.sqlalchemy_barbeiro_repository import SQLAlchemyBarbeiroRepository
from sqlalchemy.orm import Session

class BarbeiroService:
    def __init__(self, session: Session):
        self.repository = SQLAlchemyBarbeiroRepository(session)

    def criar_barbeiro(self, cpf: str, nome: str, email: str, telefone: str, senha: str, tel_trabalho: str) -> Barbeiro:
        # Validações
        if not self.validar_cpf(cpf):
            raise ValueError("CPF inválido")
        
        if not self.validar_email(email):
            raise ValueError("Email inválido")
        
        if not self.validar_telefone(tel_trabalho):
            raise ValueError("Telefone de trabalho inválido")
        
        if self.repository.buscar_por_cpf(cpf):
            raise ValueError("CPF já cadastrado")
        
        if self.repository.buscar_por_email(email):
            raise ValueError("Email já cadastrado")

        # Criar barbeiro
        barbeiro = Barbeiro(
            cpf=cpf,
            nome=nome,
            email=email,
            telefone=telefone,
            senha=senha,
            tel_trabalho=tel_trabalho
        )
        
        # Persistir
        self.repository.adicionar(barbeiro)
        return barbeiro

    def buscar_barbeiro_por_cpf(self, cpf: str) -> Optional[Barbeiro]:
        return self.repository.buscar_por_cpf(cpf)

    def buscar_barbeiro_por_email(self, email: str) -> Optional[Barbeiro]:
        return self.repository.buscar_por_email(email)

    def listar_barbeiros(self) -> List[Barbeiro]:
        return self.repository.listar()

    def atualizar_dados(self, cpf: str, nome=None, email=None, telefone=None, senha=None, tel_trabalho=None) -> Optional[Barbeiro]:
        barbeiro = self.repository.buscar_por_cpf(cpf)
        if not barbeiro:
            return None

        if email and not self.validar_email(email):
            raise ValueError("Email inválido")
        
        if tel_trabalho and not self.validar_telefone(tel_trabalho):
            raise ValueError("Telefone de trabalho inválido")
        
        if email and email != barbeiro.email:
            if self.repository.buscar_por_email(email):
                raise ValueError("Email já cadastrado")
            barbeiro.email = email

        if nome:
            barbeiro.nome = nome
        if telefone:
            barbeiro.telefone = telefone
        if senha:
            barbeiro.senha = senha
        if tel_trabalho:
            barbeiro.tel_trabalho = tel_trabalho

        return barbeiro

    def remover_barbeiro(self, cpf: str) -> bool:
        barbeiro = self.repository.buscar_por_cpf(cpf)
        if not barbeiro:
            return False

        if not self.validar_remocao_barbeiro(barbeiro):
            raise ValueError("Não é possível remover o barbeiro devido a restrições de negócio")

        self.repository.remover(cpf)
        return True

    def autenticar_barbeiro(self, email: str, senha: str) -> Optional[Barbeiro]:
        barbeiro = self.repository.buscar_por_email(email)
        if barbeiro and barbeiro.senha == senha:
            return barbeiro
        return None

    def buscar_barbeiros_disponiveis(self, data: date) -> List[Barbeiro]:
        return self.repository.buscar_disponiveis_por_data(data)

    def buscar_barbeiros_com_jornadas(self) -> List[Barbeiro]:
        return self.repository.buscar_com_jornadas()

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
