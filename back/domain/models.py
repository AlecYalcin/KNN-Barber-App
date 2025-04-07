import uuid
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

    def verificar_disponibilidade(self, horario):
        if horario._disponibilidade != 'Disponível':
            raise HorarioIndisponivelParaBarbeiro("Horário indisponível para o barbeiro")

class Cliente(Pessoa):
    pass

class Servico:
    def __init__(self, id, nome, descricao, valor_base):
        self._id = id
        self._nome = nome
        self._descricao = descricao
        self._valor_base = valor_base

class Horario:
    def __init__(self, id, data, hora, disponibilidade):
        self._id = id
        self._data = data
        self._hora = hora
        self._disponibilidade = disponibilidade

class Pagamento:
    def __init__(self, id, metodo: MetodoPagamento, servico: Servico, adicional=0):
        self._id = id
        self._metodo = metodo
        self._adicional = adicional
        self._valor = 0
        self._definir_valor(servico)

    def _definir_valor(self, servico):
        self._valor = servico._valor_base + self._adicional

class HorarioDeAtendimento:
    def __init__(self, id, status_servico: StatusServico, status_pagamento: StatusPagamento, justificativa, cliente: Cliente, barbeiro: Barbeiro, servico: Servico, horario: Horario, pagamento: Pagamento):
        self._id = id
        self._status_servico = status_servico
        self._status_pagamento = status_pagamento
        self._justificativa = justificativa
        self._cliente = cliente
        self._barbeiro = barbeiro
        self._servico = servico
        self._horario = horario
        self._pagamento = pagamento

# ---------------------- FUNÇÕES AUXILIARES ------------------------
def gerar_id():
    return str(uuid.uuid4())

def criar_horario_de_atendimento(cliente: Cliente, barbeiro: Barbeiro, horario: Horario, servico: Servico, metodo_pagamento: MetodoPagamento, adicional=0):
    barbeiro.verificar_disponibilidade(horario)
    pagamento = Pagamento(gerar_id(), metodo_pagamento, servico, adicional)
    atendimento = HorarioDeAtendimento(
        id=gerar_id(),
        status_servico=StatusServico.AGENDADO,
        status_pagamento=StatusPagamento.PENDENTE,
        justificativa=None,
        cliente=cliente,
        barbeiro=barbeiro,
        servico=servico,
        horario=horario,
        pagamento=pagamento
    )
    return atendimento
