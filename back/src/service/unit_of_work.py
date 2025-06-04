from src.adapters.repositories import *
from sqlalchemy.orm import sessionmaker
import abc

class AbstractUnidadeDeTrabalho(abc.ABC):
    usuarios: AbstractUsuarioRepository
    servicos: AbstractServicoRepository
    jornadas: AbstractJornadaRepository
    barbeiros: AbstractBarbeiroRepository
    pagamentos: AbstractPagamentoRepository
    agendamentos: AbstractAgendamentoRepository
    horarios_indisponiveis: AbstractHorarioIndisponivelRepository

    def __enter__(self) -> 'AbstractUnidadeDeTrabalho':
        return self
    
    def __exit__(self, *args):
        self.rollback()

    @abc.abstractmethod
    def commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError
    
class UnidadeDeTrabalho(AbstractUnidadeDeTrabalho):
    def __init__(self, session_maker: sessionmaker):
        self.session_maker = session_maker

    def __enter__(self):
        self.session = self.session_maker()
        self.usuarios = UsuarioRepository(self.session)
        self.servicos = ServicoRepository(self.session)
        self.jornadas = JornadaRepository(self.session)
        self.barbeiros = BarbeiroRepository(self.session)
        self.pagamentos = PagamentoRepository(self.session)
        self.agendamentos = AgendamentoRepository(self.session)
        self.horarios_indisponiveis = HorarioIndisponivelRepository(self.session)
        return super().__enter__()
    
    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()
    
    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()