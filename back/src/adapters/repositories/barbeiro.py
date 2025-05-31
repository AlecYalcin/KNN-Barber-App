from src.adapters.repository import AbstractSQLAlchemyRepository, Session
from src.domain.models import Barbeiro
from . import UsuarioRepository, JornadaRepository, HorarioIndisponivelRepository

class BarbeiroRepository(AbstractSQLAlchemyRepository):
    def __init__(self, session: Session):
        self.session = session
        self.usuario_repo = UsuarioRepository(self.session)
        self.jornada_repo = JornadaRepository(self.session)
        self.horario_indisponivel_repo = HorarioIndisponivelRepository(self.session)

    def consultar_por_cpf(self, cpf: str) -> Barbeiro | None:
        usuario = self.usuario_repo.consultar_por_cpf(cpf)
        jornada_de_trabalho = self.jornada_repo.consultar_por_barbeiro_e_vigente(cpf)
        horarios_indisponivies = self.horario_indisponivel_repo.consultar_por_barbeiro(cpf) 

        return Barbeiro(
            usuario=usuario,
            jornada_de_trabalho=jornada_de_trabalho,
            horarios_indisponiveis=horarios_indisponivies,
        )

    def lista_de_barbeiros(self) -> list[Barbeiro]:
        barbeiros: list[Barbeiro] = []
        for barbeiro in self.usuario_repo.retornar_barbeiros():
            jornada_de_trabalho = self.jornada_repo.consultar_por_barbeiro_e_vigente(barbeiro.cpf)
            horarios_indisponivies = self.horario_indisponivel_repo.consultar_por_barbeiro(barbeiro.cpf)
            barbeiros.append(Barbeiro(
                usuario=barbeiro,
                jornada_de_trabalho=jornada_de_trabalho,
                horarios_indisponiveis=horarios_indisponivies
            )) 
            
        return barbeiros