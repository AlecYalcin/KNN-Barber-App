from src.domain.models import Pagamento, Agendamento, Usuario
from src.adapters.repository import AbstractSQLAlchemyRepository

class PagamentoRepository(AbstractSQLAlchemyRepository):
    def adicionar(self, pagamento: Pagamento):
        self.session.add(pagamento)

    def remover(self, cpf: str):
        pagamento = self.consultar_por_id(cpf)
        self.session.delete(pagamento)

    def consultar_por_id(self, id: str) -> Pagamento | None:
        pagamento = self.session.query(Pagamento).filter(Pagamento.id == id).first()
        return pagamento
    
    def consultar_por_agendamento(self, agendamento_id: str) -> Pagamento | None:
        pagamentos = self.session.query(Pagamento).filter(Pagamento.agendamento_id == agendamento_id).first()
        return pagamentos

    def retornar_pagamentos_de_cliente(self, cpf: str) -> list[Pagamento]:
        pagamentos = (
            self.session.query(Pagamento)
            .join(Agendamento, Agendamento.id == Pagamento.agendamento_id)
            .join(Usuario, Usuario.cpf == Agendamento.cliente_cpf)
            .filter(
                Usuario.cpf == cpf,
            )
        ).all()
        return pagamentos
