class pessoa():
    def __init__(self, cpf, nome, email, telefone, senha):
        self._cpf = cpf
        self._nome = nome
        self._email = email
        self._telefone = telefone
        self._senha = senha

class barbeiro(pessoa):
    def __init__(self, cpf, nome, email, telefone, senha, tel_trabalho):
        super().__init__(cpf, nome, email, telefone, senha)
        self._tel_trabalho = tel_trabalho
    
class servico():
    def __init__(self, id, nome, descricao, valor_base):
        self._id = id
        self._nome = nome
        self._descricao = descricao
        self._valor_base = valor_base
        

    