from src.service.unit_of_work import AbstractUnidadeDeTrabalho
from src.domain.models import Servico
from src.domain.exceptions import (
    DuracaoInvalida,
    PermissaoNegada,
    PrecoInvalido,
    ServicoNaoEncontrado,
)
from sqlalchemy.orm.exc import UnmappedInstanceError

def criar_servico(
    uow: AbstractUnidadeDeTrabalho,
    nome: str,
    descricao: str,
    preco: float,
    duracao: int,
    solicitante: dict | None = None,
) -> None:
    """
    Serviço de criação de novos serviços da barbearia

    Args:
        uow(AbstractUnidadeDeTrabalho): Unidade de trabalho abstrata
        nome(str): Nome do serviço
        descricao(str): Descrição do serviço
        preco(float): Preço do serviço
        duracao(int): Duração do serviço em minutos
        solicitante(dict): Usuário que está solicitando a operação
    Raises:
        PermissaoNegada: O usuário não possui permissões para realizar essa operação.
        DuracaoInvalida: A duração do serviço não está entre 5min ou 120min
        PrecoInvalido: O preço do serviço precisa ser maior que zero.
    """

    # Verificando permissão de usuário
    if ( 
        solicitante 
        and solicitante['eh_barbeiro'] == False
    ):
        raise PermissaoNegada()

    # Verificando validade de duração
    if not (5 <= duracao <= 120):
        raise DuracaoInvalida("A duração do serviço não está entre 5min ou 120min")

    # Verificando a validade do preço
    if preco <= 0:
        raise PrecoInvalido("O preço do serviço precisa ser maior que zero.")

    servico = Servico(nome=nome, descricao=descricao, preco=preco, duracao=duracao)
    with uow:
        uow.servicos.adicionar(servico)
        uow.commit()

def consultar_servico(
    uow: AbstractUnidadeDeTrabalho,
    id: str,
) -> dict:
    """
    Serviço de consulta de serviços existentes no sistema.

    Args:
        uow(AbstractUnidadeDeTrabalho): Unidade de trabalho abstrata
        id(str): Identificador do serviço
    Returns:
        dict: dicionário de dados com as informações do serviço para o endpoint.
        Caso não exista serviço, será enviado um dicionário vazio.
    """

    servico = None
    with uow:
        if id:
            servico = uow.servicos.consultar(id)
        if not servico:
            return {}
        return servico.to_dict()

def listar_servicos(
    uow: AbstractUnidadeDeTrabalho,
    filtro: str | None = None,
) -> list[dict]:
    """
    Serviço de listagem de todos os serviços existentes no sistema.

    Args:
        uow(AbstractUnidadeDeTrabalho): Unidade de trabalho abstrata
        filtro(str | None): (Opcional) Nome dos serviços que se busca de forma parecida.
    """

    servicos = []
    with uow:
        if filtro:
            servicos_encontrados = uow.servicos.consultar_por_nome(nome=filtro)
        else:
            servicos_encontrados = uow.servicos.listar()
        if len(servicos_encontrados) > 0:
            servicos.extend([servico.to_dict() for servico in servicos_encontrados])
        return servicos

def atualizar_servico(
    uow: AbstractUnidadeDeTrabalho,
    id: str,
    novo_nome: str | None = None,
    nova_descricao: str | None = None,
    novo_preco: float | None = None,
    nova_duracao: int | None = None,
    solicitante: dict | None = None,
) -> None:
    """
    Serviço de criação de novos serviços da barbearia

    Args:
        uow(AbstractUnidadeDeTrabalho): Unidade de trabalho abstrata
        id(str): Identificador do serviço a ser alterado
        novo_nome(str): Novo nome do serviço
        nova_descricao(str): Nova descrição do serviço
        novo_preco(float): Novo preço do serviço
        nova_duracao(int): Nova duração do serviço em minutos
        solicitante(dict): Usuário que está solicitando a operação
    Raises:
        PermissaoNegada: O usuário não possui permissões para realizar essa operação.
        DuracaoInvalida: A duração do serviço não está entre 5min ou 120min
        PrecoInvalido: O preço do serviço precisa ser maior que zero.
        ServicoNaoEncontrado: Serviço não foi encontrado para a alteração
    """

    # Verificando permissão de usuário
    if ( 
        solicitante 
        and solicitante['eh_barbeiro'] == False
    ):
        raise PermissaoNegada()

    # Verificando validade de duração
    if nova_duracao and not (5 <= nova_duracao <= 120):
        raise DuracaoInvalida("A duração do serviço não está entre 5min ou 120min")

    # Verificando a validade do preço
    if novo_preco and novo_preco <= 0:
        raise PrecoInvalido("O preço do serviço precisa ser maior que zero.")
    
    # Criando serviço base
    novo_servico = Servico(
        id=id,
        nome=novo_nome, 
        descricao=nova_descricao, 
        preco=novo_preco, 
        duracao=nova_duracao
    )

    # Realizando alteração
    with uow:
        try:
            uow.servicos.alterar(id=id, novo_servico=novo_servico)
            uow.commit()
        except AttributeError:
            raise ServicoNaoEncontrado("Serviço não foi encontrado para a alteração.")


def remover_servico(
    uow: AbstractUnidadeDeTrabalho,
    id: str,
    solicitante: dict | None = None,
) -> None:
    """
    Serviço de exclusão de serviços existentes no sistema.

    Args:
        uow(AbstractUnidadeDeTrabalho): Unidade de trabalho abstrata
        id(str): Identificador do serviço a ser deletado
        solicitante(dict): Usuário que está solicitando a operação
    Raises:
        PermissaoNegada: O usuário não possui permissões para realizar essa operação.
        ServicoNaoEncontrado: Serviço não foi encontrado para exclusão
    """

    # Verificando permissão de usuário
    if ( 
        solicitante 
        and solicitante['eh_barbeiro'] == False
    ):
        raise PermissaoNegada()

    with uow:
        try:
            uow.servicos.remover(id)
            uow.commit()
        except UnmappedInstanceError:
            raise ServicoNaoEncontrado("Serviço não foi encontrado para exclusão.")
