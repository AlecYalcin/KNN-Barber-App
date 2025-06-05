from src.domain.models import Servico
from src.adapters.repository import *
import abc

class AbstractServicoRepository():
    @abc.abstractmethod
    def adicionar(self, servico: Servico):
        raise NotImplementedError
    
    @abc.abstractmethod
    def remover(self, id: str):
        raise NotImplementedError

    @abc.abstractmethod
    def alterar(self, id: str, novo_servico: Servico):
        raise NotImplementedError

    @abc.abstractmethod
    def consultar(self, id: str) -> Servico | None:
        raise NotImplementedError

    @abc.abstractmethod
    def consultar_por_nome(self, nome: str) -> list[Servico]:
        raise NotImplementedError

    @abc.abstractmethod
    def listar(self) -> list[Servico]:
        raise NotImplementedError

class ServicoRepository(AbstractServicoRepository, AbstractSQLAlchemyRepository):
    def adicionar(self, servico: Servico):
        self.session.add(servico)

    def remover(self, id: str):
        servico = self.consultar(id)
        self.session.delete(servico)

    def alterar(self, id: str, novo_servico: Servico):
        servico = self.consultar(id)
        servico.nome = novo_servico.nome or servico.nome
        servico.descricao = novo_servico.descricao or servico.descricao
        servico.preco = novo_servico.preco or servico.preco
        servico.duracao = novo_servico.duracao or servico.duracao

    def consultar(self, id: str) -> Servico | None:
        servico = self.session.query(Servico).filter(Servico.id == id).first()
        return servico
    
    def consultar_por_nome(self, nome: str) -> list[Servico]:
        servicos = self.session.query(Servico).filter(Servico.nome.like(f'%{nome}%')).all()
        return servicos

    def listar(self) -> list[Servico]:
        servicos = self.session.query(Servico).all()
        return servicos
