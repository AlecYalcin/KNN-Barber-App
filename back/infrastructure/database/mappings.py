from sqlalchemy import Table, Column, Integer, String, ForeignKey, DateTime, Boolean, Enum, Date, Time, Float
from sqlalchemy.orm import registry, relationship
from back.domain.models import (
    Barbeiro, Cliente, Servico, Jornada, Horario,
    Pagamento, HorarioDeAtendimento, StatusServico,
    StatusPagamento, MetodoPagamento
)

# Create registry
mapper_registry = registry()
metadata = mapper_registry.metadata

# Tables
barbeiros = Table(
    'barbeiros',
    metadata,
    Column('cpf', String, primary_key=True),
    Column('nome', String, nullable=False),
    Column('email', String, nullable=False, unique=True),
    Column('telefone', String, nullable=False),
    Column('senha', String, nullable=False),
    Column('tel_trabalho', String, nullable=False)
)

clientes = Table(
    'clientes',
    metadata,
    Column('cpf', String, primary_key=True),
    Column('nome', String, nullable=False),
    Column('email', String, nullable=False, unique=True),
    Column('telefone', String, nullable=False),
    Column('senha', String, nullable=False)
)

servicos = Table(
    'servicos',
    metadata,
    Column('id', String, primary_key=True),
    Column('nome', String, nullable=False),
    Column('descricao', String),
    Column('valor_base', Float, nullable=False),
    Column('duracao', Integer, nullable=False, default=30)
)

jornadas = Table(
    'jornadas',
    metadata,
    Column('id', String, primary_key=True),
    Column('dia', Date, nullable=False),
    Column('turno', String, nullable=False),
    Column('barbeiro_cpf', String, ForeignKey('barbeiros.cpf'))
)

horarios = Table(
    'horarios',
    metadata,
    Column('id', String, primary_key=True),
    Column('inicio', Time, nullable=False),
    Column('fim', Time, nullable=False),
    Column('disponivel', Boolean, nullable=False, default=True),
    Column('jornada_id', String, ForeignKey('jornadas.id'))
)

pagamentos = Table(
    'pagamentos',
    metadata,
    Column('id', String, primary_key=True),
    Column('metodo', Enum(MetodoPagamento), nullable=False),
    Column('adicional', Float, default=0),
    Column('valor', Float, nullable=False),
    Column('status', Enum(StatusPagamento), nullable=False)
)

horarios_atendimento = Table(
    'horarios_atendimento',
    metadata,
    Column('id', String, primary_key=True),
    Column('status_servico', Enum(StatusServico), nullable=False),
    Column('justificativa', String),
    Column('cliente_cpf', String, ForeignKey('clientes.cpf')),
    Column('barbeiro_cpf', String, ForeignKey('barbeiros.cpf')),
    Column('servico_id', String, ForeignKey('servicos.id')),
    Column('jornada_id', String, ForeignKey('jornadas.id')),
    Column('horario_id', String, ForeignKey('horarios.id')),
    Column('pagamento_id', String, ForeignKey('pagamentos.id'))
)

# Mappings
def configure_mappers():
    mapper_registry.map_imperatively(
        Barbeiro,
        barbeiros,
        properties={
            'jornadas': relationship(Jornada, backref='barbeiro')
        }
    )

    mapper_registry.map_imperatively(
        Cliente,
        clientes
    )

    mapper_registry.map_imperatively(
        Servico,
        servicos
    )

    mapper_registry.map_imperatively(
        Jornada,
        jornadas,
        properties={
            'horarios': relationship(Horario, backref='jornada')
        }
    )

    mapper_registry.map_imperatively(
        Horario,
        horarios
    )

    mapper_registry.map_imperatively(
        Pagamento,
        pagamentos
    )

    mapper_registry.map_imperatively(
        HorarioDeAtendimento,
        horarios_atendimento,
        properties={
            'cliente': relationship(Cliente),
            'barbeiro': relationship(Barbeiro),
            'servico': relationship(Servico),
            'jornada': relationship(Jornada),
            'horario': relationship(Horario),
            'pagamento': relationship(Pagamento)
        }
    ) 