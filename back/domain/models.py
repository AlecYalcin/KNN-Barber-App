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
    
