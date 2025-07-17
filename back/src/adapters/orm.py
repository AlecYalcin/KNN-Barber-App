from sqlalchemy.orm import registry, relationship
from sqlalchemy import (
    Table, 
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
    Boolean,
    Enum,
    Time,
    Float,
    func,
    text,
)

from src.domain.value_objects import DiaDaSemana, MetodoPagamento
from src.domain.models import (
    Usuario, 
    Servico, 
    Jornada, 
    HorarioIndisponivel, 
    Agendamento, 
    Pagamento,
)

# Create registry
mapper_registry = registry()
metadata = mapper_registry.metadata

# Tables

usuarios = Table(
    'usuario',
    metadata,
    Column('cpf', String, primary_key=True),
    Column('nome', String, nullable=False),
    Column('senha', String, nullable=False),
    Column('telefone', String, nullable=True),
    Column('email', String, nullable=False, unique=True),
    Column('eh_barbeiro', Boolean, server_default=text('FALSE')),
    Column('created_at', DateTime, default=func.now(), nullable=True),
    Column('updated_at', DateTime, default=func.now(), onupdate=func.now(), nullable=True),
)

servicos = Table(
    'servico',
    metadata,
    Column('id', String, primary_key=True),
    Column('nome', String, nullable=False),
    Column('descricao', String, nullable=True),
    Column('preco', Float, nullable=False),
    Column('duracao', Integer, nullable=False, default=30),
    Column('created_at', DateTime, default=func.now(), nullable=True),
    Column('updated_at', DateTime, default=func.now(), onupdate=func.now(), nullable=True),
)

jornadas = Table(
    'jornada',
    metadata,
    Column('id', String, primary_key=True),
    Column('ativa', Boolean, default=True),
    Column('horario_inicio', Time, nullable=False),
    Column('horario_pausa', Time, nullable=True),
    Column('horario_retorno', Time, nullable=True),
    Column('horario_fim', Time, nullable=False),
    Column('dia_da_semana', Enum(DiaDaSemana, values_callable=lambda obj: [e.value for e in obj]), nullable=False),
    Column('barbeiro_cpf', String, ForeignKey('usuario.cpf', ondelete="CASCADE")),
    Column('created_at', DateTime, default=func.now(), nullable=True),
    Column('updated_at', DateTime, default=func.now(), onupdate=func.now(), nullable=True),
)

horarios_indisponiveis = Table(
    'horario_indisponivel',
    metadata,
    Column('id', String, primary_key=True),
    Column('horario_inicio', DateTime, nullable=False),
    Column('horario_fim', DateTime, nullable=False),
    Column('justificativa', String, nullable=True),
    Column('barbeiro_cpf', String, ForeignKey('usuario.cpf', ondelete="CASCADE")),
    Column('created_at', DateTime, default=func.now(), nullable=True),
    Column('updated_at', DateTime, default=func.now(), onupdate=func.now(), nullable=True),
)

agendamentos = Table(
    'agendamento',
    metadata,
    Column('id', String, primary_key=True),
    Column('horario_inicio', DateTime, nullable=False),
    Column('horario_fim', DateTime, nullable=False),
    Column('barbeiro_cpf', String, ForeignKey('usuario.cpf', ondelete="SET NULL"), nullable=True),
    Column('cliente_cpf', String, ForeignKey('usuario.cpf', ondelete="SET NULL"), nullable=True),
    Column('created_at', DateTime, default=func.now(), nullable=True),
    Column('updated_at', DateTime, default=func.now(), onupdate=func.now(), nullable=True),
)

servicos_do_agendamento = Table(
    'servicos_do_agendamento',
    metadata,
    Column('agendamento', String, ForeignKey('agendamento.id', ondelete="CASCADE"), primary_key=True),
    Column('servico', String, ForeignKey('servico.id', ondelete="SET NULL"), primary_key=True, nullable=True),
    Column('created_at', DateTime, default=func.now(), nullable=True),
    Column('updated_at', DateTime, default=func.now(), onupdate=func.now(), nullable=True),
)

pagamentos = Table(
    'pagamento',
    metadata,
    Column('id', String, primary_key=True),
    Column('valor', Float, nullable=False),
    Column('data', DateTime, nullable=False),
    Column('metodo', Enum(MetodoPagamento, values_callable=lambda obj: [e.value for e in obj]), nullable=False),
    Column('agendamento_id', String, ForeignKey('agendamento.id', ondelete="SET NULL"), nullable=True),
    Column('created_at', DateTime, default=func.now(), nullable=True),
    Column('updated_at', DateTime, default=func.now(), onupdate=func.now(), nullable=True),
)

# Mappings
def start_mappers():
    # Usuários
    mapper_registry.map_imperatively(
        Usuario,
        usuarios
    )

    # Serviços
    mapper_registry.map_imperatively(
        Servico,
        servicos,
    )

    # Jornadas
    mapper_registry.map_imperatively(
        Jornada,
        jornadas,
        properties={
            'barbeiro': relationship(
                Usuario,
                primaryjoin=jornadas.c.barbeiro_cpf == usuarios.c.cpf,
                passive_deletes=True
            )
        }
    )

    # Horários Indisponíveis
    mapper_registry.map_imperatively(
        HorarioIndisponivel,
        horarios_indisponiveis,
        properties={
            'barbeiro': relationship(
                Usuario,
                primaryjoin=horarios_indisponiveis.c.barbeiro_cpf == usuarios.c.cpf,
                passive_deletes=True
            )
        }
    )

    # Agendamentos
    mapper_registry.map_imperatively(
        Agendamento,
        agendamentos,
        properties={
            'barbeiro': relationship(
                Usuario,
                primaryjoin=agendamentos.c.barbeiro_cpf == usuarios.c.cpf,
            ),
            'cliente': relationship(
                Usuario,
                primaryjoin=agendamentos.c.cliente_cpf == usuarios.c.cpf,
            ),
            'servicos': relationship(
                Servico,
                secondary=servicos_do_agendamento,
                primaryjoin=agendamentos.c.id == servicos_do_agendamento.c.agendamento,
                secondaryjoin=servicos_do_agendamento.c.servico == Servico.id,
            ),
        }
    )

    # Pagamentos
    mapper_registry.map_imperatively(
        Pagamento,
        pagamentos,
        properties={
            'agendamento': relationship(
                Agendamento,
                primaryjoin=pagamentos.c.agendamento_id == agendamentos.c.id,
            )
        }
    )