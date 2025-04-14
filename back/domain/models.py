import uuid
from datetime import datetime, time, date
from enum import Enum

# ----------------------------- ENUMs -----------------------------
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

# -------------------------- EXCEPTION ----------------------------
class HorarioIndisponivelParaBarbeiro(Exception):
    pass

# --------------------------- CLASSES -----------------------------
class Pessoa:
    def __init__(self, cpf, nome, email, telefone, senha):
        self._cpf = cpf
        self._nome = nome
        self._email = email
        self._telefone = telefone
        self._senha = senha

class Barbeiro(Pessoa):
    def __init__(self, cpf, nome, email, telefone, senha, tel_trabalho):
        super().__init__(cpf, nome, email, telefone, senha)
        self._tel_trabalho = tel_trabalho
        self.jornadas = []

    def definir_jornada(self, jornada):
        self.jornadas.append(jornada)

    def verificar_disponibilidade(self, horario):
        if not horario.disponivel:
            raise HorarioIndisponivelParaBarbeiro("Horário indisponível para o barbeiro")

class Cliente(Pessoa):
    pass

class Servico:
    def __init__(self, id, nome, descricao, valor_base, duracao=30):
        self._id = id
        self._nome = nome
        self._descricao = descricao
        self._valor_base = valor_base
        self._duracao = duracao

class Jornada:
    def __init__(self, dia: date, turno: str):
        self.dia = dia
        self.turno = turno  # "manhã", "tarde", "noite", "madrugada"
        self.horarios = []

    def adicionar_horario(self, horario):
        self.horarios.append(horario)

    def buscar_horario(self, inicio):
        for h in self.horarios:
            if h.inicio == inicio:
                return h
        return None

class Horario:
    def __init__(self, hora_inicio: time, hora_fim: time):
        self.inicio = hora_inicio
        self.fim = hora_fim
        self.disponivel = True

class Pagamento:
    def __init__(self, metodo: MetodoPagamento, servico: Servico, adicional=0):
        self._metodo = metodo
        self._adicional = adicional
        self._valor = servico._valor_base + adicional
        self._status = StatusPagamento.PENDENTE

    def confirmar(self):
        self._status = StatusPagamento.CONCLUIDO

    def falhar(self):
        self._status = StatusPagamento.FALHOU

class HorarioDeAtendimento:
    def __init__(self, id, status_servico: StatusServico, justificativa, cliente: Cliente, barbeiro: Barbeiro, servico: Servico, jornada: Jornada, horario: Horario, pagamento: Pagamento):
        self._id = id
        self._status_servico = status_servico
        self._justificativa = justificativa
        self._cliente = cliente
        self._barbeiro = barbeiro
        self._servico = servico
        self._jornada = jornada
        self._horario = horario
        self._pagamento = pagamento

    def cancelar(self, justificativa):
        self._horario.disponivel = True
        self._status_servico = StatusServico.CANCELADO
        self._justificativa = justificativa
        self._pagamento._status = StatusPagamento.FALHOU

# ---------------------- FUNÇÕES AUXILIARES ------------------------
def gerar_id():
    return str(uuid.uuid4())

def criar_horario_de_atendimento(cliente: Cliente, barbeiro: Barbeiro, jornada: Jornada, horario: Horario, servico: Servico, metodo_pagamento: MetodoPagamento, adicional=0):
    barbeiro.verificar_disponibilidade(horario)
    pagamento = Pagamento(metodo_pagamento, servico, adicional)
    atendimento = HorarioDeAtendimento(
        id=gerar_id(),
        status_servico=StatusServico.AGENDADO,
        justificativa=None,
        cliente=cliente,
        barbeiro=barbeiro,
        servico=servico,
        jornada=jornada,
        horario=horario,
        pagamento=pagamento
    )
    horario.disponivel = False
    return atendimento
