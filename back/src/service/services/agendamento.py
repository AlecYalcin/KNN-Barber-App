from src.service.unit_of_work import AbstractUnidadeDeTrabalho
from src.domain.models import Agendamento, Usuario, Servico, normalizar_horarios,criar_agendamento as model_criar_agendamento

from src.domain.exceptions import(
    BarbeiroNaoEncontrado,
    UsuarioNaoEncontrado,
    ServicoNaoEncontrado,
    HorarioIndisponivelParaBarbeiro
    
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
    """
    Cria um agendamento único para um barbeiro e um cliente. Verificando se já
    existe um agendamento que crie conflito de horários para aquele mesmo barbeiro.
    
    Args:
        uow(AbstractUnidadeDeTrabalho): Unidade de Trabalho
        horario_inicio(datetime): Horário de inicio do agendamento
        horario_fim(datetime): Horário do fim do agendamendo
        barbeiro_cpf(str): CPF do Barbeiro do agendamento
        cliente_cpf(str): CPF do Cliente do agendamento
        serviços_id(list[[str]]): Lista que contém todos os identificadores dos serviços solicitados no agendamento
        
    Raises:
        BarbeiroNaoEncontrado: O barbeiro não foi encontrado
        UsuarioNaoEncontrado: O cliente não foi encontrado
        ServicoNaoEncontrado: Serviço não foi encontrado
        HorarioIndisponivelParaBarbeiro: O horário de agendamento entra em conflito com algum horário de agendamento já existente.
    """
    
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
        
        horarios = (horario_inicio, horario_fim)
        agendamentos_horario_barbeiro = [uow.agendamentos.listar_por_horario(horarios)]
        
        for agendamento_barbeiro in agendamentos_horario_barbeiro:
            if (horarios[1]>agendamento_barbeiro.horario_inicio and horarios[0] <= agendamento_barbeiro.horario_fim) and agendamento_barbeiro.barbeiro == barbeiro:
                raise HorarioIndisponivelParaBarbeiro("O horário selecionado encontra-se indisponível para o barbeiro.")
        
        agendamento = model_criar_agendamento(cliente, barbeiro, servicos, horarios)

def consultar_agendamento(
    uow: AbstractUnidadeDeTrabalho,
    id: str,
):
    """
    Consulta um agendamento existente pelo identificador.
    
    Args:
        uow(AbstractUnidadeDeTrabalho): Unidade de Trabalho abstrata
        id(str): identificador do agendamento
    Returns:
        dict: Dicionário com os dados retornados da consulta
    """
    
    with uow:
        agendamento = uow.agendamentos.consultar(id)
        if not agendamento:
            return {}
        return agendamento.to_dict()
    
def consultar_agendamentos_por_barbeiro(
    uow: AbstractUnidadeDeTrabalho,
    barbeiro_cpf: str,
) -> list[dict]:
    """
    Consulta todos os agendamentos existentes do barbeiro.
    
    Args:
        uow(AbstractUnidadeDeTrabalho): Unidade de Trabalho abstrata
        barbeiro_cpf(str): CPF do Barbeiro escolhido
    Returns:
        list[dict]: Lista de todos os agendamentos do barbeiro
    """
    
    with uow:
        agendamentos = uow.agendamentos.listar_por_barbeiro(barbeiro_cpf)
        return [agendamento.to_dict() for agendamento in agendamentos] if agendamentos else []
    
def consultar_agendamentos_por_horario(
    uow: AbstractUnidadeDeTrabalho,
    horarios: tuple[datetime, datetime],
) -> list[dict]:
    """
    Consulta todos os agendamentos existentes em um determinado horário.
    
    Args:
        uow(AbstractUnidadeDeTrabalho): Unidade de Trabalho abstrata
        horarios(tuple[datetime, datetime]): Horários de início e fim do agendamento
    Returns:
        list[dict]: Lista de todos os agendamentos no horário
    """
    
    with uow:
        agendamentos = uow.agendamentos.listar_por_horario(horarios)
        return [agendamento.to_dict() for agendamento in agendamentos] if agendamentos else []