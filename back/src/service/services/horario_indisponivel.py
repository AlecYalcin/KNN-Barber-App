from src.service.unit_of_work import AbstractUnidadeDeTrabalho
from src.domain.models import (
    HorarioIndisponivel, Usuario
)
from src.domain.exceptions import (
    HorarioIndisponivelInvalido,
    HorarioIndisponivelNaoEncontrado,
    BarbeiroNaoEncontrado,
    PermissaoNegada,
)
from sqlalchemy.orm.exc import UnmappedInstanceError
from datetime import time, datetime

# Serviços de Horário Indisponível

def criar_horario_indisponivel(
    uow: AbstractUnidadeDeTrabalho,
    barbeiro_cpf: str,
    horario_inicio: datetime,
    horario_fim: datetime,
    justificativa: str,
    solicitante: dict | None = None,
):
    """
    Marca um horário indisponível na agenda de um barbeiro. Esse horário pode indicar dias de feriado, semanas de férias, ou horários 
    específicos. 

    Args:
        uow(AbstractUnidadeDeTrabalho): Unidade de Trabalho abstrata
        barbeiro_cpf(str): CPF do Barbeiro a ter o horário cadastrado.
        horario_inicio(datetime): Data e hora do início do horário indisponível.
        horario_fim(datetime): Data e hora do fim do horário indisponível.
        justificativa(str): Motivação para o horário estar indisponível.
        solicitante(dict): Usuário que está solicitando a operação
    Raises:
        PermissaoNegada: O usuário não possui permissões para realizar essa operação.
        PermissaoNegada: Não é possível criar o horário indisponível de outro barbeiro.
        HorarioIndisponivelInvalido: O horário de inicio tem que ser menor que o horário de fim.
        BarbeiroNaoEncontrado: O cpf informado não pertencem a um barbeiro do sistema.
    """

    # Verificando permissão de usuário
    if (solicitante and solicitante['eh_barbeiro'] == False):
        raise PermissaoNegada()

    # Validade dos horários
    if horario_inicio >= horario_fim:
        raise HorarioIndisponivelInvalido("O horário de inicio tem que ser menor que o horário de fim.")
    
    with uow:
        barbeiro = uow.usuarios.consultar(barbeiro_cpf)
        
        # Verificando existência do barbeiro
        if not barbeiro:
            raise BarbeiroNaoEncontrado("O cpf informado não pertencem a um barbeiro do sistema.")
        
        # Verificando se o barbeiro está criando um horário indisponível para para ele
        if (solicitante and solicitante['cpf'] != barbeiro.cpf):
            raise PermissaoNegada("Não é possível criar a jornada de outro barbeiro.")

        # Adicionando horário
        horario_indisponivel = HorarioIndisponivel(horario_inicio, horario_fim, justificativa, barbeiro)
        uow.horarios_indisponiveis.adicionar(horario_indisponivel)
        uow.commit()

def consultar_horario_indisponivel(
    uow: AbstractUnidadeDeTrabalho,
    id: str,
) -> dict:
    """
    Retorna um dia indisponível a partir de um identificador.

    Args:
        uow(AbstractUnidadeDeTrabalho): Unidade de Trabalho abstrata
        id(str): Identificador do dia indisponível
    Returns:
        dict: Dicionário com as informações do horário encontrado.
    """

    with uow:
        horario_indisponivel = uow.horarios_indisponiveis.consultar(id)
        if not horario_indisponivel:
            return {}
        return horario_indisponivel.to_dict()

def consultar_horario_indisponivel_por_horario(
    uow: AbstractUnidadeDeTrabalho,
    horario_inicio: datetime,
    horario_fim: datetime,
) -> list[dict]:
    """
    Retorna todos os dias indisponíveis em uma faixa de horários.
    
    Args:
        uow(AbstractUnidadeDeTrabalho): Unidade de Trabalho abstrata
        horario_inicio(datetime): Data e hora do início do horário indisponível.
        horario_fim(datetime): Data e hora do fim do horário indisponível.
    Returns:
        list[dict]: Uma lista de dicionários dos horários encontrados na faixa.
    """

    horarios_indisponiveis = []
    with uow:
        horarios = (horario_inicio, horario_fim)
        horarios_encontrados = uow.horarios_indisponiveis.consultar_por_horario(horarios)
        for horario in horarios_encontrados:
            horarios_indisponiveis.extend([horario.to_dict()])
        return horarios_indisponiveis

def alterar_horario_indisponivel(
    uow: AbstractUnidadeDeTrabalho,
    id: str,
    horario_inicio: datetime | None = None,
    horario_fim: datetime | None = None,
    justificativa: str | None = None,
    solicitante: dict | None = None,
):
    """
    Edita um dia indisponível.
    
    Args:
        uow(AbstractUnidadeDeTrabalho): Unidade de Trabalho abstrata
        id(str): Identificador do dia indisponível
        horario_inicio(datetime): Data e hora do início do horário indisponível.
        horario_fim(datetime): Data e hora do fim do horário indisponível.
        justificativa(str): Motivação para o horário estar indisponível.
        solicitante(dict): Usuário que está solicitando a operação
    Raises:
        PermissaoNegada: O usuário não possui permissões para realizar essa operação.
        PermissaoNegada: Não é possível alterar o horário indisponível de outro barbeiro.
        HorarioIndisponivelInvalido: O horário de inicio tem que ser menor que o horário de fim.
        HorarioIndisponivelNaoEncontrado: O horario indisponivel especificado não foi encontrado.
    """

    # Verificando permissão de usuário
    if (solicitante and solicitante['eh_barbeiro'] == False):
        raise PermissaoNegada()

    # Validade dos horários
    if horario_inicio >= horario_fim:
        raise HorarioIndisponivelInvalido("O horário de inicio tem que ser menor que o horário de fim.")
    
    novo_horario = HorarioIndisponivel(barbeiro=None, horario_inicio=horario_inicio, horario_fim=horario_fim, justificativa=justificativa)
    with uow:
        # Verificar existência de horário
        horario_indisponivel = uow.horarios_indisponiveis.consultar(id)
        if not horario_indisponivel:
            raise HorarioIndisponivelNaoEncontrado("O horario indisponivel especificado não foi encontrado.")

        # Verificando se o barbeiro está criando um horário indisponível para para ele
        if (solicitante and solicitante['cpf'] != horario_indisponivel.barbeiro.cpf):
            raise PermissaoNegada("Não é possível alterar a jornada de outro barbeiro.")

        # Alterar Horário    
        uow.horarios_indisponiveis.alterar(id, novo_horario)
        uow.commit()

def excluir_horario_indisponivel(
    uow: AbstractUnidadeDeTrabalho,
    id: str,
    solicitante: dict | None = None,
):
    """
    Exclui um dia indisponível.
    
    Args:
        uow(AbstractUnidadeDeTrabalho): Unidade de Trabalho abstrata
        id(str): Identificador do dia indisponível
        solicitante(dict): Usuário que está solicitando a operação
    Raises
        PermissaoNegada: O usuário não possui permissões para realizar essa operação.
        PermissaoNegada: Não é possível excluir o horário indisponível de outro barbeiro.
        HorarioIndisponivelNaoEncontrado: O horario indisponivel especificado não foi encontrado.
    """

    # Verificando permissão de usuário
    if (solicitante and solicitante['eh_barbeiro'] == False):
        raise PermissaoNegada()

    with uow:
        # Verificar existência de horário
        horario_indisponivel = uow.horarios_indisponiveis.consultar(id)
        if not horario_indisponivel:
            raise HorarioIndisponivelNaoEncontrado("O horario indisponivel especificado não foi encontrado.")

        # Verificando se o barbeiro está criando um horário indisponível para para ele
        if (solicitante and solicitante['cpf'] != horario_indisponivel.barbeiro.cpf):
            raise PermissaoNegada("Não é possível excluir a jornada de outro barbeiro.")

        uow.horarios_indisponiveis.remover(id)
        uow.commit()
