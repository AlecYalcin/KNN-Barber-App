from src.adapters.repository import Session
from src.domain.models import Barbeiro
from .usuario import UsuarioRepository, AbstractUsuarioRepository
from .jornada import JornadaRepository, AbstractJornadaRepository
from .horario_indisponivel import HorarioIndisponivelRepository, AbstractHorarioIndisponivelRepository
import abc

class AbstractBarbeiroRepository():
    def __init__(
        self, 
        usuario_repo: AbstractUsuarioRepository,
        jornada_repo: AbstractJornadaRepository,
        horario_indisponivel_repo: AbstractHorarioIndisponivelRepository
    ):
        self.usuario_repo = usuario_repo
        self.jornada_repo = jornada_repo
        self.horario_indisponivel_repo = horario_indisponivel_repo

    @abc.abstractmethod
    def consultar(self, cpf: str) -> Barbeiro:
        raise NotImplementedError

    @abc.abstractmethod
    def listar(self) -> list[Barbeiro]:
        raise NotImplementedError

class BarbeiroRepository(AbstractBarbeiroRepository):
    def __init__(self, session: Session):
        self.session = session
        super().__init__(
            usuario_repo=UsuarioRepository(self.session),
            jornada_repo=JornadaRepository(self.session),
            horario_indisponivel_repo=HorarioIndisponivelRepository(self.session)
        )

    def consultar(self, cpf: str) -> Barbeiro | None:
        usuario = self.usuario_repo.consultar(cpf)
        jornada_de_trabalho = self.jornada_repo.listar_jornada_de_barbeiro(cpf)
        horarios_indisponivies = self.horario_indisponivel_repo.consultar_por_barbeiro(cpf) 

        return Barbeiro(
            usuario=usuario,
            jornada_de_trabalho=jornada_de_trabalho,
            horarios_indisponiveis=horarios_indisponivies,
        )

    def listar(self) -> list[Barbeiro]:
        barbeiros: list[Barbeiro] = []
        for barbeiro in self.usuario_repo.listar_barbeiros():
            jornada_de_trabalho = self.jornada_repo.listar_jornada_de_barbeiro(barbeiro.cpf)
            horarios_indisponivies = self.horario_indisponivel_repo.consultar_por_barbeiro(barbeiro.cpf)
            barbeiros.append(Barbeiro(
                usuario=barbeiro,
                jornada_de_trabalho=jornada_de_trabalho,
                horarios_indisponiveis=horarios_indisponivies
            )) 
            
        return barbeiros