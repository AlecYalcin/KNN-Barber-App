from src.service.unit_of_work import AbstractUnidadeDeTrabalho
from src.domain.models import (
    HorarioIndisponivel,
)
from src.domain.exceptions import (
    BarbeiroNaoEncontrado,
)
from sqlalchemy.orm.exc import UnmappedInstanceError
from datetime import time

# Serviços de Horário Indisponível

def criar_horario_indisponivel(
    uow: AbstractUnidadeDeTrabalho,
):
    """Cria um dia indisponivel"""

def consultar_horario_indisponivel(
    uow: AbstractUnidadeDeTrabalho,
):
    """Pega um dia indisponivel"""

def consultar_horario_indisponivel_por_horario(
    uow: AbstractUnidadeDeTrabalho,
):
    """Pega uma lista de dias indisponiveis em uma faixa de horarios/dias"""

def editar_horario_indisponivel(
    uow: AbstractUnidadeDeTrabalho,
):
    """Altera um dia indisponivel"""

def excluir_horario_indisponivel(
    uow: AbstractUnidadeDeTrabalho,
):
    """Tira um dia indisponivel"""

# Serviços de Barbeiro