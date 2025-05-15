from typing import List, Optional
from sqlalchemy.orm import Session
from back.domain.models import Pessoa
from back.domain.repositories.pessoa_repository import AbstractPessoaRepository
from back.infrastructure.database.connection import SessionLocal
from back.infrastructure.database.mappings import PessoaModel

class SQLAlchemyPessoaRepository(AbstractPessoaRepository):
    def __init__(self):
        self.session: Session = SessionLocal()

    def _to_domain(self, model: PessoaModel) -> Pessoa:
        return Pessoa(
            cpf=model.cpf,
            nome=model.nome,
            email=model.email,
            telefone=model.telefone,
            senha=model.senha
        )

    def _to_model(self, pessoa: Pessoa) -> PessoaModel:
        return PessoaModel(
            cpf=pessoa.cpf,
            nome=pessoa.nome,
            email=pessoa.email,
            telefone=pessoa.telefone,
            senha=pessoa.senha
        )

    def criar_pessoa(self, cpf: str, nome: str, email: str, telefone: str, senha: str) -> Pessoa:
        pessoa = Pessoa(cpf, nome, email, telefone, senha)
        pessoa_model = self._to_model(pessoa)
        self.session.add(pessoa_model)
        self.session.commit()
        return pessoa

    def buscar_pessoa_por_cpf(self, cpf: str) -> Optional[Pessoa]:
        pessoa_model = self.session.query(PessoaModel).filter(PessoaModel.cpf == cpf).first()
        return self._to_domain(pessoa_model) if pessoa_model else None

    def buscar_pessoa_por_email(self, email: str) -> Optional[Pessoa]:
        pessoa_model = self.session.query(PessoaModel).filter(PessoaModel.email == email).first()
        return self._to_domain(pessoa_model) if pessoa_model else None

    def listar_pessoas(self) -> List[Pessoa]:
        pessoas_model = self.session.query(PessoaModel).all()
        return [self._to_domain(p) for p in pessoas_model]

    def atualizar_dados(self, cpf: str, nome: str = None, email: str = None, 
                       telefone: str = None, senha: str = None) -> Optional[Pessoa]:
        pessoa_model = self.session.query(PessoaModel).filter(PessoaModel.cpf == cpf).first()
        if not pessoa_model:
            return None

        if nome:
            pessoa_model.nome = nome
        if email:
            pessoa_model.email = email
        if telefone:
            pessoa_model.telefone = telefone
        if senha:
            pessoa_model.senha = senha

        self.session.commit()
        return self._to_domain(pessoa_model)

    def remover_pessoa(self, cpf: str) -> bool:
        pessoa_model = self.session.query(PessoaModel).filter(PessoaModel.cpf == cpf).first()
        if not pessoa_model:
            return False

        self.session.delete(pessoa_model)
        self.session.commit()
        return True

    def __del__(self):
        self.session.close() 