class pessoa():
    def __init__(self, cpf, nome, email, telefone, senha):
        self._cpf = cpf
        self._nome = nome
        self._email = email
        self._telefone = telefone
        self._senha = senha

class barbeiro(pessoa):
    def __init__(self, cpf, nome, email, telefone, senha, tel_trabalho):
        #Barbeiro herda os atributos da classe pessoa
        super().__init__(cpf, nome, email, telefone, senha)
        self._tel_trabalho = tel_trabalho
    
class servico():
    def __init__(self, id, nome, descricao, valor_base):
        self._id = id
        self._nome = nome
        self._descricao = descricao
        self._valor_base = valor_base
        
class horario():
    def __init__(self, id, data, hora, disponibilidade):
        self._id = id
        self._data = data
        self._hora = hora
        self._disponibilidade = disponibilidade

class pagamento():
    def __init__(self, id, data, adicional, metodo, valor):
        self._id = id
        self._data = data  

class horario_de_atendimento():
    def __init__(self, id, status_servico, status_pagamento, confirmado, justificativa, cliente, barbeiro, servico, horario, pagamento):
        self._id = id
        self._status_servico = status_servico
        self._status_pagamento = status_pagamento
        self._confirmado = confirmado
        self._justificativa = justificativa
        
        #Classes Externas
        self._cliente = cliente
        self._barbeiro = barbeiro
        self._servico = servico
        self._horario = horario
        self._pagamento = pagamento