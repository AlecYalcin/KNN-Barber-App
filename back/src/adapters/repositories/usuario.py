from src.adapters.repository import AbstractSQLAlchemyRepository
from src.domain.models import Usuario

class UsuarioRepository(AbstractSQLAlchemyRepository):
    def adicionar(self, usuario: Usuario):
        self.session.add(usuario)

    def remover(self, cpf: str):
        usuario = self.consultar_por_cpf(cpf)
        self.session.delete(usuario)

    def consultar_por_cpf(self, cpf: str) -> Usuario | None:
        usuario = self.session.query(Usuario).filter(Usuario.cpf == cpf).first()
        return usuario

    def retornar_clientes(self) -> list[Usuario]:
        usuarios = self.session.query(Usuario).filter(Usuario.eh_barbeiro == False).all()
        return usuarios
    
    def retornar_barbeiros(self) -> list[Usuario]:
        usuarios = self.session.query(Usuario).filter(Usuario.eh_barbeiro == True).all()
        return usuarios