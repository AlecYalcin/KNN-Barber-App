from enum import Enum

# Enums para padronizar status
class StatusServico(Enum):
    AGENDADO = "Agendado"
    CONCLUIDO = "Concluído"
    CANCELADO = "Cancelado"

class StatusPagamento(Enum):
    PENDENTE = "Pendente"
    PAGO = "Pago"
    CANCELADO = "Cancelado"

class Disponibilidade(Enum):
    DISPONIVEL = "Disponível"
    INDISPONIVEL = "Indisponível"

# Exceção personalizada para horário indisponível
class HorarioIndisponivelParaBarbeiro(Exception):
    def __init__(self):
        super().__init__("Horário indisponível para o barbeiro")

# Classe base pessoa
class Pessoa:
    def __init__(self, cpf, nome, email, telefone, senha):
        self._cpf = cpf
        self._nome = nome
        self._email = email
        self._telefone = telefone
        self._senha = senha

# Barbeiro herda de pessoa
class Barbeiro(Pessoa):
    def __init__(self, cpf, nome, email, telefone, senha, tel_trabalho):
        super().__init__(cpf, nome, email, telefone, senha)
        self._tel_trabalho = tel_trabalho

    def verificar_disponibilidade(self, horario):
        if horario._disponibilidade == Disponibilidade.INDISPONIVEL:
            raise HorarioIndisponivelParaBarbeiro()
        return True

# Serviço oferecido
class Servico:
    def __init__(self, id, nome, descricao, valor_base):
        self._id = id
        self._nome = nome
        self._descricao = descricao
        self._valor_base = valor_base

# Horário
class Horario:
    def __init__(self, id, data, hora, disponibilidade: Disponibilidade):
        self._id = id
        self._data = data
        self._hora = hora
        self._disponibilidade = disponibilidade

# Pagamento
class Pagamento:
    def __init__(self, id, data, adicional, metodo, valor):
        self._id = id
        self._data = data
        self._adicional = adicional
        self._metodo = metodo
        self._valor = valor

# Agendamento
class HorarioDeAtendimento:
    def __init__(self, id, status_servico: StatusServico, status_pagamento: StatusPagamento, confirmado: bool,
                 justificativa, cliente: Pessoa, barbeiro: Barbeiro, servico: Servico, 
                 horario: Horario, pagamento: Pagamento = None):
        self._id = id
        self._status_servico = status_servico
        self._status_pagamento = status_pagamento
        self._confirmado = confirmado
        self._justificativa = justificativa
        self._cliente = cliente
        self._barbeiro = barbeiro
        self._servico = servico
        self._horario = horario
        self._pagamento = pagamento
