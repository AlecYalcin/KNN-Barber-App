from src.service.unit_of_work import AbstractUnidadeDeTrabalho
from src.domain.models import Pagamento, Agendamento
from src.domain.value_objects import MetodoPagamento
from src.domain.exceptions import (
    PermissaoNegada,
    PagamentoNaoEncontrado,
    ValorInvalido,
    AgendamentoNaoEncontrado,
)
from sqlalchemy.orm.exc import UnmappedInstanceError
from datetime import datetime

def criar_pagamento(
    uow: AbstractUnidadeDeTrabalho,
    valor: float,
    metodo: MetodoPagamento,
    agendamento_id: str,
    solicitante: dict | None = None,
) -> None:
    """
    Serviço de criação de novos pagamentos da barbearia

    Args:
        uow(AbstractUnidadeDeTrabalho): Unidade de trabalho abstrata
        valor(float): Valor do pagamento
        metodo(MetodoPagamento): Método de pagamento utilizado
        agendamento_id(str): ID do agendamento associado ao pagamento
        solicitante(dict): Usuário que está solicitando a operação
    Raises:
        PermissaoNegada: O usuário não possui permissões para realizar essa operação.
        ValorInvalido: O valor do pagamento precisa ser maior que zero.
        AgendamentoNaoEncontrado: Agendamento não foi encontrado.
    """

    # Verificando permissão de usuário
    if ( 
        solicitante 
        and solicitante['eh_barbeiro'] == False
    ):
        raise PermissaoNegada()

    # Verificando a validade do valor
    if valor <= 0:
        raise ValorInvalido("O valor do pagamento precisa ser maior que zero.")

    # Verificando valor máximo
    if valor > 100000:
        raise ValorInvalido("O valor do pagamento não pode exceder R$ 100.000,00")

    # Verificando a validade do método de pagamento
    try:
        MetodoPagamento(metodo)
    except ValueError:
        raise ValueError(f"Método de pagamento inválido: {metodo}")

    with uow:
        # Verificando se o agendamento existe
        agendamento = uow.agendamentos.consultar(agendamento_id)
        if not agendamento:
            raise AgendamentoNaoEncontrado("Agendamento não foi encontrado.")

        pagamento = Pagamento(
            valor=valor,
            data=datetime.now(),
            metodo=metodo,
            agendamento=agendamento
        )
        
        uow.pagamentos.adicionar(pagamento)
        uow.commit()

def consultar_pagamento(
    uow: AbstractUnidadeDeTrabalho,
    id: str,
) -> dict:
    """
    Serviço de consulta de pagamentos existentes no sistema.

    Args:
        uow(AbstractUnidadeDeTrabalho): Unidade de trabalho abstrata
        id(str): Identificador do pagamento
    Returns:
        dict: dicionário de dados com as informações do pagamento para o endpoint.
        Caso não exista pagamento, será enviado um dicionário vazio.
    """

    pagamento = None
    with uow:
        if id:
            pagamento = uow.pagamentos.consultar(id)
        if not pagamento:
            return {}
        return pagamento.to_dict()

def consultar_pagamento_por_agendamento(
    uow: AbstractUnidadeDeTrabalho,
    agendamento_id: str,
) -> dict | None:
    """
    Serviço de consulta de pagamento por agendamento.

    Args:
        uow(AbstractUnidadeDeTrabalho): Unidade de trabalho abstrata
        agendamento_id(str): Identificador do agendamento
    Returns:
        dict | None: Pagamento do agendamento ou None se não houver pagamento.
    """

    with uow:
        pagamento = uow.pagamentos.consultar_por_agendamento(agendamento_id)
        if not pagamento:
            return None
        return pagamento.to_dict()

def listar_pagamentos_de_cliente(
    uow: AbstractUnidadeDeTrabalho,
    cpf: str,
) -> list[dict]:
    """
    Serviço de listagem de pagamentos de um cliente específico.

    Args:
        uow(AbstractUnidadeDeTrabalho): Unidade de trabalho abstrata
        cpf(str): CPF do cliente
    Returns:
        list[dict]: Lista de pagamentos do cliente
    """

    pagamentos = []
    with uow:
        pagamentos_encontrados = uow.pagamentos.listar_pagamentos_de_cliente(cpf)
        if len(pagamentos_encontrados) > 0:
            pagamentos.extend([pagamento.to_dict() for pagamento in pagamentos_encontrados])
        return pagamentos

def atualizar_pagamento(
    uow: AbstractUnidadeDeTrabalho,
    id: str,
    novo_valor: float | None = None,
    novo_metodo: MetodoPagamento | None = None,
    solicitante: dict | None = None,
) -> None:
    """
    Serviço de atualização de pagamentos existentes no sistema.

    Args:
        uow(AbstractUnidadeDeTrabalho): Unidade de trabalho abstrata
        id(str): Identificador do pagamento a ser alterado
        novo_valor(float): Novo valor do pagamento
        novo_metodo(MetodoPagamento): Novo método de pagamento
        solicitante(dict): Usuário que está solicitando a operação
    Raises:
        PermissaoNegada: O usuário não possui permissões para realizar essa operação.
        ValorInvalido: O valor do pagamento precisa ser maior que zero.
        PagamentoNaoEncontrado: Pagamento não foi encontrado para a alteração
    """

    # Verificando permissão de usuário
    if ( 
        solicitante 
        and solicitante['eh_barbeiro'] == False
    ):
        raise PermissaoNegada()

    # Verificando a validade do valor
    if novo_valor is not None and novo_valor <= 0:
        raise ValorInvalido("O valor do pagamento precisa ser maior que zero.")
    
    # Criando pagamento base
    novo_pagamento = Pagamento(
        id=id,
        valor=novo_valor,
        metodo=novo_metodo,
        data=datetime.now(),
        agendamento=None  # Será definido no método alterar
    )

    # Realizando alteração
    with uow:
        try:
            uow.pagamentos.alterar(id=id, novo_pagamento=novo_pagamento)
            uow.commit()
        except AttributeError:
            raise PagamentoNaoEncontrado("Pagamento não foi encontrado para a alteração.")

def remover_pagamento(
    uow: AbstractUnidadeDeTrabalho,
    id: str,
    solicitante: dict | None = None,
) -> None:
    """
    Serviço de exclusão de pagamentos existentes no sistema.

    Args:
        uow(AbstractUnidadeDeTrabalho): Unidade de trabalho abstrata
        id(str): Identificador do pagamento a ser deletado
        solicitante(dict): Usuário que está solicitando a operação
    Raises:
        PermissaoNegada: O usuário não possui permissões para realizar essa operação.
        PagamentoNaoEncontrado: Pagamento não foi encontrado para exclusão
    """

    # Verificando permissão de usuário
    if ( 
        solicitante 
        and solicitante['eh_barbeiro'] == False
    ):
        raise PermissaoNegada()

    with uow:
        try:
            uow.pagamentos.remover(id)
            uow.commit()
        except UnmappedInstanceError:
            raise PagamentoNaoEncontrado("Pagamento não foi encontrado para exclusão.")