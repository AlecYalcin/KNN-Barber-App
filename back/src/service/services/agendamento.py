from src.service.unit_of_work import AbstractUnidadeDeTrabalho
from src.domain.models import Agendamento, Usuario, Servico, criar_agendamento as model_criar_agendamento


from datetime import datetime

def criar_agendamento(
    uow: AbstractUnidadeDeTrabalho,
    horario_inicio: datetime,
    horario_fim: datetime,
    barbeiro_cpf: str,
    cliente_cpf: str,  
    servicos_id: list[str]            
) -> None:
    with uow:
        
        cliente = uow.usuarios.consultar(cpf=cliente_cpf)
        barbeiro = uow.barbeiros.consultar(cpf=barbeiro_cpf)
        servicos = [uow.servicos.consultar(id) for id in servicos_id]
        
        agendamento = model_criar_agendamento(cliente, barbeiro, servicos, (horario_inicio,horario_fim))
        