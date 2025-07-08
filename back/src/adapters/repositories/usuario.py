from src.adapters.repository import AbstractSQLAlchemyRepository
from src.domain.models import Usuario
import abc

class AbstractUsuarioRepository():
    @abc.abstractmethod
    def adicionar(self, usuario: Usuario):
        raise NotImplementedError
    
    @abc.abstractmethod
    def remover(self, cpf: str):
        raise NotImplementedError

    @abc.abstractmethod
    def alterar(self, cpf: str, novo_usuario: Usuario):
        raise NotImplementedError

    @abc.abstractmethod
    def consultar(self, cpf: str) ->Usuario | None:
        raise NotImplementedError

    @abc.abstractmethod
    def consultar_por_email(self, email: str) -> Usuario | None:
        raise NotImplementedError

    @abc.abstractmethod
    def listar_clientes(self) -> list[Usuario]:
        raise NotImplementedError

    @abc.abstractmethod
    def listar_barbeiros(self) -> list[Usuario]:
        raise NotImplementedError

class UsuarioRepository(AbstractUsuarioRepository, AbstractSQLAlchemyRepository):
    def adicionar(self, usuario: Usuario):
        self.session.add(usuario)

    def remover(self, cpf: str):
        usuario = self.consultar(cpf)
        self.session.delete(usuario)

    def alterar(self, cpf: str, novo_usuario: Usuario):
        usuario = self.consultar(cpf=cpf)
        usuario.nome = novo_usuario.nome or usuario.nome
        usuario.email = novo_usuario.email or usuario.email 
        usuario.senha = novo_usuario.senha or usuario.senha
        usuario.telefone = novo_usuario.telefone or usuario.telefone

    def consultar(self, cpf: str) -> Usuario | None:
        usuario = self.session.query(Usuario).filter(Usuario.cpf == cpf).first()
        return usuario

    def consultar_por_email(self, email: str) -> Usuario | None:
        usuario = self.session.query(Usuario).filter(Usuario.email == email).first()
        return usuario

    def listar_clientes(self) -> list[Usuario]:
        usuarios = self.session.query(Usuario).filter(Usuario.eh_barbeiro == False).all()
        return usuarios
    
    def listar_barbeiros(self) -> list[Usuario]:
        usuarios = self.session.query(Usuario).filter(Usuario.eh_barbeiro == True).all()
        return usuarios