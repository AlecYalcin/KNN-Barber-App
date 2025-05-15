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
        self.cpf = cpf
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.senha = senha

class Barbeiro(Pessoa):
    def __init__(self, cpf, nome, email, telefone, senha, tel_trabalho):
        super().__init__(cpf, nome, email, telefone, senha)
        self.tel_trabalho = tel_trabalho
        self.jornadas = []

    def definir_jornada(self, jornada):
        self.jornadas.append(jornada)

    def verificar_disponibilidade(self, horario):
        if not horario.disponivel:
            raise HorarioIndisponivelParaBarbeiro("Horário indisponível para o barbeiro")

class Cliente(Pessoa):
    def __init__(self, cpf, nome, email, telefone, senha):
        super().__init__(cpf, nome, email, telefone, senha)

    def autenticar(self, senha: str) -> bool:
        return self.senha == senha

    def verificar_disponibilidade(self, horario):
        if not horario.disponivel:
            raise HorarioIndisponivelParaCliente("Horário indisponível para o cliente")

class Servico:
    def __init__(self, nome, descricao, valor_base, duracao=30):
        self.id = str(uuid.uuid4())
        self.nome = nome
        self.descricao = descricao
        self.valor_base = valor_base
        self.duracao = duracao

class Jornada:
    def __init__(self, dia: date, turno: str):
        self.id = str(uuid.uuid4())
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
        self.id = str(uuid.uuid4())
        self.inicio = hora_inicio
        self.fim = hora_fim
        self.disponivel = True

class Pagamento:
    def __init__(self, metodo: MetodoPagamento, servico: Servico, adicional=0):
        self.id = str(uuid.uuid4())
        self.metodo = metodo
        self.adicional = adicional
        self.valor = servico.valor_base + adicional
        self.status = StatusPagamento.PENDENTE

    def confirmar(self):
        self.status = StatusPagamento.CONCLUIDO

    def falhar(self):
        self.status = StatusPagamento.FALHOU

class HorarioDeAtendimento:
    def __init__(self, status_servico: StatusServico, justificativa, cliente: Cliente, barbeiro: Barbeiro, servico: Servico, jornada: Jornada, horario: Horario, pagamento: Pagamento):
        self.id = str(uuid.uuid4())
        self.status_servico = status_servico
        self.justificativa = justificativa
        self.cliente = cliente
        self.barbeiro = barbeiro
        self.servico = servico
        self.jornada = jornada
        self.horario = horario
        self.pagamento = pagamento

    def cancelar(self, justificativa):
        self.horario.disponivel = True
        self.status_servico = StatusServico.CANCELADO
        self.justificativa = justificativa
        self.pagamento.status = StatusPagamento.FALHOU

# ---------------------- FUNÇÕES AUXILIARES ------------------------
def criar_horario_de_atendimento(cliente: Cliente, barbeiro: Barbeiro, jornada: Jornada, horario: Horario, servico: Servico, metodo_pagamento: MetodoPagamento, adicional=0):
    barbeiro.verificar_disponibilidade(horario)
    pagamento = Pagamento(metodo_pagamento, servico, adicional)
    atendimento = HorarioDeAtendimento(
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
