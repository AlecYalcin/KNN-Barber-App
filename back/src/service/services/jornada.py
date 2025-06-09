from src.service.unit_of_work import AbstractUnidadeDeTrabalho
from src.domain.models import (
    Jornada,
)
from src.domain.exceptions import (
    JornadaNaoEncontrada,
    JornadaJaExistenteNoMesmoDia,
    HorarioDaJornadaInvalido,
    DiaDaSemanaInvalido,
    BarbeiroNaoEncontrado,
)
from src.domain.value_objects import (
    DiaDaSemana
)
from sqlalchemy.orm.exc import UnmappedInstanceError
from datetime import time

# Serviços de Jornada

def criar_jornada(
    uow: AbstractUnidadeDeTrabalho,
    barbeiro_cpf: str,
    dia_da_semana: str,
    horario_inicio: time,
    horario_fim: time,
    horario_retorno: time | None = None,
    horario_pausa: time | None = None,
):
    """
    Cria uma jornada única para um barbeiro. Verificando
    se já existe uma jornada nesse mesmo dia da semana.

    Args:
        uow(AbstractUnidadeDeTrabalho): Unidade de Trabalho
        barbeiro_cpf(str): CPF do barbeiro da jornada
        dia_da_semana(str): Dia da semana
        horario_inicio(time): Horário de início da jornada
        horario_fim(time): Horário de fim da jornada 
        horario_pausa(time): Horário de pausa da jornada
        horario_de_retorno(time): Horário de retorno da jornada.
    Raises:
        HorarioDaJornadaInvalido: O horário de alguma forma não segue diretrizes de horário
        DiaDaSemanaInvalido: O dia da semana escolhido não é válido
        BarbeiroNaoEncontrado: O barbeiro não foi encontrado
        JornadaJaExistenteNoMesmoDia: O dia da semana escolhido já possui uma jornada equivalente 
    """

    # Horário de Início > Fim
    if (horario_inicio > horario_fim):
        raise HorarioDaJornadaInvalido("O horário de início é maior que o horário de fim.")
    
    # Horario com Pausa e sem retorno ou com Retorno e sem pausa
    if (horario_pausa and not horario_retorno) or (horario_retorno and not horario_pausa):
        raise HorarioDaJornadaInvalido("Caso haja uma pausa, é necessário ter um retorno. O inverso também.")
    
    # Horário de Pausa > Retorno
    if (horario_retorno and horario_pausa) and horario_pausa > horario_retorno:
        raise HorarioDaJornadaInvalido("O horário de pausa não pode ser maior que o horário de retorno.")

    # Horário de não está em Fim > (Retorno > Pausa) > Inicio
    if (
        (horario_retorno and horario_pausa) 
        and not (horario_fim > horario_retorno > horario_pausa > horario_inicio)
    ):
        raise HorarioDaJornadaInvalido("O horário de pausa/retorno não deve estar fora da faixa do horário de início e fim.")

    # Dia da semana inválido
    try:
        dia_enum = DiaDaSemana(dia_da_semana)
    except ValueError:
        raise DiaDaSemanaInvalido("O dia da semana fornecido não condiz com nenhum valor salvo. Tente:" \
        "Segunda, Terça, Quarta, Quinta, Sexta, Sábado ou Domingo.")

    with uow:
        # Barbeiro não encontrado
        barbeiro = uow.barbeiros.consultar(barbeiro_cpf)
        if not barbeiro.usuario:
            raise BarbeiroNaoEncontrado("Não foi encontrado nenhum barbeiro com esse identificador.")
        
        # Jornada ativa em dia da semana    
        jornada_ja_existente = next((jornada for jornada in barbeiro.jornada_de_trabalho if jornada.dia_da_semana == dia_enum), None)
        if jornada_ja_existente and jornada_ja_existente.ativa:
            raise JornadaJaExistenteNoMesmoDia("Já existe uma jornada para esse barbeiro no mesmo dia.")
        
        # Criando jornada
        jornada = Jornada(
            barbeiro.usuario, 
            dia_enum, 
            horario_inicio=horario_inicio, 
            horario_pausa=horario_pausa, 
            horario_retorno=horario_retorno, 
            horario_fim=horario_fim
        )
        uow.jornadas.adicionar(jornada)
        uow.commit()

def consultar_jornada(
    uow: AbstractUnidadeDeTrabalho,
    id: str,
) -> dict:
    """
    Consulta uma jornada existente pelo identificador.

    Args:
        uow(AbstractUnidadeDeTrabalho): Unidade de Trabalho abstrata
        id(str): identificador da jornada
    Returns:
        dict: Dicionário com os dados retornados da consulta
    """

    with uow:
        jornada = uow.jornadas.consultar(id)
        if not jornada:
            return {}
        return jornada.to_dict()  

def consultar_jornada_de_trabalho(
    uow: AbstractUnidadeDeTrabalho,
    barbeiro_cpf: str,
) -> list[dict]:
    """
    Consulta todas as jornadas ativas existentes do barbeiro

    Args:
        uow(AbstractUnidadeDeTrabalho): Unidade de Trabalho abstrata
        barbeiro_cpf(str): CPF do Barbeiro escolhido
    Returns:
        list[dict]: Lista de todas as jornadas do barbeiro
    """

    jornada_de_trabalho = []
    with uow:
        jornadas_encontradas = uow.jornadas.listar_jornada_de_barbeiro(barbeiro_cpf)
        for jornada in jornadas_encontradas:
            jornada_de_trabalho.extend([jornada.to_dict()])
        return jornada_de_trabalho

def alterar_ativacao_de_jornada(
    uow: AbstractUnidadeDeTrabalho,
    id: str,
):
    """
    Altera o estado da jornada
    
    Args:
        uow(AbstractUnidadeDeTrabalho): Unidade de Trabalho
        id(str): Jornada que vai ser ativada/desativa
    Raises:
        JornadaJaExistenteNoMesmoDia: Se essa jornada for ativada, existirão duas jornadas no mesmo dia. Jornada: {jornada_id}
        JornadaNaoEncontrada: A jornada especificada não foi encontrada
    """

    with uow:
        jornada = uow.jornadas.consultar(id)
        if not jornada:
            raise JornadaNaoEncontrada("A jornada especificada não foi encontrada.")
        barbeiro = jornada.barbeiro
        jornadas_do_barbeiro = uow.jornadas.listar_jornada_de_barbeiro(barbeiro.cpf)
        for jornada_do_barbeiro in jornadas_do_barbeiro:
            if jornada_do_barbeiro.id != jornada.id and jornada_do_barbeiro.dia_da_semana == jornada.dia_da_semana:
                raise JornadaJaExistenteNoMesmoDia("Se essa jornada for ativada, existirão duas jornadas no mesmo dia. " \
                f"Desative a jornada: {jornada_do_barbeiro.id}")
        jornada.ativa = not jornada.ativa
        uow.commit()

def excluir_jornada(
    uow: AbstractUnidadeDeTrabalho,
    id: str,
):
    """
    Deleta uma jornada existente no sistema.

    Args:
        uow(AbstractUnidadeDeTrabalho): Unidade de Trabalho
        id(str): Identificador da jornada
    Raises:
        JornadaNaoEncontrada: A jornada especificada não foi encontrada
    """

    with uow:
        try:
            uow.jornadas.remover(id)
            uow.commit()
        except UnmappedInstanceError:
            raise JornadaNaoEncontrada("A jornada especificada não foi encontrada.")