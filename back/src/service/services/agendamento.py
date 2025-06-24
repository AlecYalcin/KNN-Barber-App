from src.service.unit_of_work import AbstractUnidadeDeTrabalho
from src.domain.models import Agendamento, Usuario, Servico, criar_agendamento as model_criar_agendamento

from src.domain.exceptions import(
    BarbeiroNaoEncontrado,
    UsuarioNaoEncontrado,
    ServicoNaoEncontrado
    
)

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
        if not cliente.usuario:
            raise UsuarioNaoEncontrado("Não foi encontrado nenhum usuário com esse identificador.")
        
        barbeiro = uow.barbeiros.consultar(cpf=barbeiro_cpf)
        if not barbeiro.usuario:
            raise BarbeiroNaoEncontrado("Não foi encontrado nenhum barbeiro com esse identificador.")
        
        servicos = [uow.servicos.consultar(id) for id in servicos_id]
        if None in servicos:
            raise ServicoNaoEncontrado("Um dos identificadores não representa um serviço.")
        
        agendamento = model_criar_agendamento(cliente, barbeiro, servicos, (horario_inicio,horario_fim))
        