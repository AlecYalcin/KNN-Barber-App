from src.domain.models import Servico
from src.adapters.repository import AbstractSQLAlchemyRepository

class ServicoRepository(AbstractSQLAlchemyRepository):
    def adicionar(self, servico: Servico):
        self.session.add(servico)

    def remover(self, cpf: str):
        servico = self.consultar_por_id(cpf)
        self.session.delete(servico)

    def consultar_por_id(self, id: str) -> Servico | None:
        servico = self.session.query(Servico).filter(Servico.id == id).first()
        return servico
    
    def consultar_por_nome(self, nome: str) -> list[Servico]:
        servicos = self.session.query(Servico).filter(Servico.nome.like(f'%{nome}%')).all()
        return servicos

    def retornar_servicos(self) -> list[Servico]:
        servicos = self.session.query(Servico).all()
        return servicos
