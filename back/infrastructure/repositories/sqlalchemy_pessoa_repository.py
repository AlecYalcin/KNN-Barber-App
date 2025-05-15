from typing import List, Optional
from sqlalchemy.orm import Session
from back.domain.models import Pessoa
from back.domain.repositories.pessoa_repository import AbstractPessoaRepository
from back.infrastructure.database.connection import SessionLocal

class SQLAlchemyPessoaRepository(AbstractPessoaRepository):
    def __init__(self):
        self.session: Session = SessionLocal()

    def criar_pessoa(self, cpf: str, nome: str, email: str, telefone: str, senha: str) -> Pessoa:
        pessoa = Pessoa(cpf, nome, email, telefone, senha)
        self.session.add(pessoa)
        self.session.commit()
        return pessoa

    def buscar_pessoa_por_cpf(self, cpf: str) -> Optional[Pessoa]:
        return self.session.query(Pessoa).filter(Pessoa.cpf == cpf).first()

    def buscar_pessoa_por_email(self, email: str) -> Optional[Pessoa]:
        return self.session.query(Pessoa).filter(Pessoa.email == email).first()

    def listar_pessoas(self) -> List[Pessoa]:
        return self.session.query(Pessoa).all()

    def atualizar_dados(self, cpf: str, nome: str = None, email: str = None, 
                       telefone: str = None, senha: str = None) -> Optional[Pessoa]:
        pessoa = self.buscar_pessoa_por_cpf(cpf)
        if not pessoa:
            return None

        if nome:
            pessoa.nome = nome
        if email:
            pessoa.email = email
        if telefone:
            pessoa.telefone = telefone
        if senha:
            pessoa.senha = senha

        self.session.commit()
        return pessoa

    def remover_pessoa(self, cpf: str) -> bool:
        pessoa = self.buscar_pessoa_por_cpf(cpf)
        if not pessoa:
            return False

        self.session.delete(pessoa)
        self.session.commit()
        return True

    def __del__(self):
        self.session.close() 