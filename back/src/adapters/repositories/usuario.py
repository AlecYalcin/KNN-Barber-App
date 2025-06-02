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
    def consultar(self, cpf: str) -> Usuario | None:
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

    def consultar(self, cpf: str) -> Usuario | None:
        usuario = self.session.query(Usuario).filter(Usuario.cpf == cpf).first()
        return usuario

    def listar_clientes(self) -> list[Usuario]:
        usuarios = self.session.query(Usuario).filter(Usuario.eh_barbeiro == False).all()
        return usuarios
    
    def listar_barbeiros(self) -> list[Usuario]:
        usuarios = self.session.query(Usuario).filter(Usuario.eh_barbeiro == True).all()
        return usuarios