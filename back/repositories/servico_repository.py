from back.domain.models import Servico

class ServicoRepository:
    
    
    def __init__(self):
        self.servicos = []

    def cadastrar_servico(self, servico):
        self.servicos.append(servico)

    def editar_servico(self, servico, nome=None, descricao=None, valor_base=None, duracao=None):
        if nome is not None:
            servico.nome = nome
        if descricao is not None:
            servico.descricao = descricao
        if valor_base is not None:
            servico.valor_base = valor_base
        if duracao is not None:
            servico.duracao = duracao
        return servico

    def excluir_servico(self, servico):
        self.servicos.remove(servico)

    def listar_servicos(self):
        return self.servicos

    def buscar_servico_por_id(self, id):
        for servico in self.servicos:
            if servico.id == id:
                return servico
        return None 