from datetime import datetime
from enum import Enum

class StatusServico(Enum):
    AGENDADO = 'Agendado'
    CONFIRMADO = 'Confirmado'
    CANCELADO = 'Cancelado'

class StatusPagamento(Enum):
    PENDENTE = 'Pendente'
    CONCLUIDO = 'Concluído'
    FALHOU = 'Falhou'

class MetodoPagamento(Enum):
    DINHEIRO = 'Dinheiro'
    CARTAO = 'Cartão'
    PIX = 'PIX'

class DiaDaSemana(Enum):
    SEGUNDA = "Segunda-Feira"
    TERCA = "Terça-Feira"
    QUARTA = "Quarta-Feira"
    QUINTA = "Quinta-Feira"
    SEXTA = "Sexta-Feira"
    SABADO = "Sábado"
    DOMINGO = "Domingo"

    @staticmethod
    def horario_para_dia(horario: datetime) -> str:
        match horario.weekday():
            case 0:
                return DiaDaSemana.SEGUNDA
            case 1:
                return DiaDaSemana.TERCA
            case 2:
                return DiaDaSemana.QUARTA
            case 3:
                return DiaDaSemana.QUINTA
            case 4:
                return DiaDaSemana.SEXTA
            case 5:
                return DiaDaSemana.SABADO
            case 6:
                return DiaDaSemana.DOMINGO
            