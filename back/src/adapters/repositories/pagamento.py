from src.domain.models import Pagamento, Agendamento, Usuario
from src.adapters.repository import AbstractSQLAlchemyRepository
import abc

class AbstractPagamentoRepository():
    @abc.abstractmethod
    def adicionar(self, pagamento: Pagamento):
        raise NotImplementedError

    @abc.abstractmethod
    def remover(self, cpf: str):
        raise NotImplementedError

    @abc.abstractmethod
    def consultar(self, id: str) -> Pagamento | None:
        raise NotImplementedError

    @abc.abstractmethod
    def consultar_por_agendamento(self, agendamento_id: str) -> Pagamento | None:
        raise NotImplementedError

    @abc.abstractmethod
    def listar_pagamentos_de_cliente(self, cpf: str) -> list[Pagamento]:
        raise NotImplementedError


class PagamentoRepository(AbstractPagamentoRepository, AbstractSQLAlchemyRepository):
    def adicionar(self, pagamento: Pagamento):
        self.session.add(pagamento)

    def remover(self, cpf: str):
        pagamento = self.consultar(cpf)
        self.session.delete(pagamento)

    def consultar(self, id: str) -> Pagamento | None:
        pagamento = self.session.query(Pagamento).filter(Pagamento.id == id).first()
        return pagamento
    
    def consultar_por_agendamento(self, agendamento_id: str) -> Pagamento | None:
        pagamentos = self.session.query(Pagamento).filter(Pagamento.agendamento_id == agendamento_id).first()
        return pagamentos

    def listar_pagamentos_de_cliente(self, cpf: str) -> list[Pagamento]:
        pagamentos = (
            self.session.query(Pagamento)
            .join(Agendamento, Agendamento.id == Pagamento.agendamento_id)
            .join(Usuario, Usuario.cpf == Agendamento.cliente_cpf)
            .filter(
                Usuario.cpf == cpf,
            )
        ).all()
        return pagamentos
