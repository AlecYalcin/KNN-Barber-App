from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from .exceptions import TokenInvalido

import os
import jwt

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
    SEGUNDA = "Segunda"
    TERCA = "Terça"
    QUARTA = "Quarta"
    QUINTA = "Quinta"
    SEXTA = "Sexta"
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

class JWTToken():
    secret_key_padrao: str = os.getenv("SECRET_KEY") or "alecdennerguilhermesteniojulio"

    def __init__(self, info: dict, secret_key: str | None = None):
        self.secret_key = secret_key or self.secret_key_padrao
        self.token = jwt.encode(info, self.secret_key, algorithm="HS256")

    @property
    def token_extraido(self) -> dict:
        """ Função para extrair informações de um TokenJWT """
        try: 
            return jwt.decode(
                self.token, 
                self.secret_key, 
                algorithms=["HS256"],
            )
        except jwt.exceptions.InvalidTokenError:
            raise TokenInvalido("O token colocado não foi reconhecido.")
        
    @classmethod
    def extrair_token(cls, token: str, secret_key: str | None = None) -> dict:
        """ Função para extrair informações de um token """
        try: 
            return jwt.decode(
                token, 
                secret_key or cls.secret_key_padrao, 
                algorithms=["HS256"],
            )
        except jwt.exceptions.InvalidTokenError:
            raise TokenInvalido("O token colocado não foi reconhecido.")