from uuid import uuid4
from dataclasses import dataclass, field
from datetime import time, datetime, timedelta

from .value_objects import *
from .exceptions import *

# Models

@dataclass
class Usuario:    
    cpf: str
    nome: str
    email: str
    senha: str
    eh_barbeiro: bool = False
    telefone: str | None = None

@dataclass
class Servico:
    nome: str
    descricao: str
    preco: float
    duracao: int
    id: str = field(default_factory=lambda: str(uuid4()))

@dataclass
class Jornada:
    ativa: bool
    dia_da_semana: DiaDaSemana
    barbeiro: Usuario
    horario_inicio: time
    horario_fim: time
    horario_retorno: time | None = None
    horario_pausa: time | None = None
    id: str = field(default_factory=lambda: str(uuid4()))

@dataclass
class HorarioIndisponivel:
    horario_inicio: datetime 
    horario_fim: datetime
    justificativa: str
    barbeiro: Usuario
    id: str = field(default_factory=lambda: str(uuid4()))

@dataclass
class Agendamento:
    horario_inicio: datetime
    horario_fim: datetime
    barbeiro: Usuario
    cliente: Usuario
    servicos: list[Servico]
    id: str = field(default_factory=lambda: str(uuid4()))

@dataclass
class Pagamento:
    valor: float
    data: datetime
    metodo: MetodoPagamento
    agendamento: Agendamento
    id: str = field(default_factory=lambda: str(uuid4()))

# Agregados
@dataclass
class Barbeiro():
    usuario: Usuario = field(default_factory=Usuario)
    jornada_de_trabalho: list[Jornada] = field(default_factory=list)
    horarios_indisponiveis: list[HorarioIndisponivel] = field(default_factory=list)

    def verificar_se_horario_esta_na_jornada(self, horario: tuple[datetime]) -> bool:
        horario_inicio, _ = horario
        for jornada in self.jornada_de_trabalho:
            if jornada.dia_da_semana == DiaDaSemana.horario_para_dia(horario_inicio):
                return True
        return False
    
    def verificar_se_horario_esta_disponivel(self, horario: tuple[datetime]) -> bool:
        horario_inicio, horario_fim = horario
        for h_indisponivel in self.horarios_indisponiveis:
            if horario_inicio < h_indisponivel.horario_fim and horario_fim > h_indisponivel.horario_inicio:
                return False
        return True
    
    def __eq__(self, value: Usuario) -> bool:
        if isinstance(value, Barbeiro) and value.usuario.cpf == self.usuario.cpf:
            return True
        return False

# Funções
def criar_agendamento(cliente: Usuario, barbeiro: Barbeiro, servicos: list[Servico], horario: tuple[datetime]) -> Agendamento:
    """
    Realiza o agendamento de horário com um serviço para um cliente, verificando a disponibilidade do horário a partir do 
    barbeiro que está sendo contatado.

    Args:
        cliente (Usuario): Cliente que deseja marcar um agendamento.
        barbeiro (Barbeiro): Barbeiro que terá seus serviços agendados.
        servicos (list[Servico]): Lista de Serviços a serem agendados.
        horario (tuple[datetime]): Tupla com o horário de início e fim do atendimento.
    Returns:
        Agendamento: novo agendamento criado
    Raises:
        HorarioForaDaJornada: caso os horários escolhidos estejam fora da jornada do barbeiro.
        HorarioIndisponivelException: caso os horários escolhidos estejam dentro de uma faixa de horários indisponiveis.
        HorarioInsuficiente: caso o tempo disponível não seja suficiente para realizar todos os serviços.
    """

    # Formatando horário para modelo ideal
    horario = normalizar_horarios(horario)

    # Verificar se o horário é suficiente para os serviços
    tempo_necessario = timedelta(minutes=sum(servico.duracao for servico in servicos))
    if tempo_necessario > (horario[1] - horario[0]):
        raise HorarioInsuficiente("Os horários escolhidos não cobrem a quantidade de tempo mínimo para realizar os serviçs.")

    # Verifica se está dentro da jornada de trabalho do barbeiro
    if not barbeiro.verificar_se_horario_esta_na_jornada(horario):
        raise HorarioForaDaJornada("O horário escolhido está fora da jornada do barbeiro.")

    # Verifica se está dentro de algum horário indisponível
    if not barbeiro.verificar_se_horario_esta_disponivel(horario):
        raise HorarioIndisponivelException("O horário escolhido está indisponível de acordo com a disponibilidade do barbeiro.")

    return Agendamento(
        id=str(uuid4()),
        horario_inicio=horario[0],
        horario_fim=horario[1],
        barbeiro=barbeiro.usuario,
        cliente=cliente,
        servicos=servicos,
    )

def normalizar_horarios(horario: tuple[datetime]) -> tuple[datetime]:
    """
    Função para normalizar horários de consulta em valores de 30min em 30min. Exemplo: 10h20~10h50 -> 10h30~11h00.
    Sempre realiza a aproximação com o horário mais próximo. 30min se >= 15min, 0min se < 15min.

    Args:
        horario (tuple[datetime]): Tupla com o horário de início e fim do atendimento.
    Returns:
        tuple: Tupla de horários com o primeiro sendo horario_inicio formatado e o segundo horario_fim formatado.
    Raises:
        HorarioInvalido: caso os horários fornecidos de alguma forma não sejam autenticos.
    """

    # Verificar se horário é válido
    if horario[0].date() != horario[1].date():
        raise HorarioInvalido("O horário acontece em dias diferentes.")
    if horario[0].time() >= horario[1].time():
        raise HorarioInvalido("O horário de início é igual ou maior que o horário de fim.")

    # Seperando data de horário
    horario_inicio = horario[0].time()
    horario_fim = horario[1].time()

    # Separando por minutos
    inicio_minutos = horario_inicio.hour * 60 + horario_inicio.minute
    fim_minutos = horario_fim.hour * 60 + horario_fim.minute
    duracao_total = fim_minutos - inicio_minutos

    # Verficiando a quantidade de intervalos necessários para esse horário
    intervalo = duracao_total//30
    intervalo = intervalo + 1 if duracao_total % 30 > 0 else intervalo

    # Após a verificação de intervalos, aproximar o menor horário conforme a lógica imbutida
    novo_horario_inicio = horario[0]
    if (horario_inicio.minute >= 15):
        novo_horario_inicio = novo_horario_inicio.replace(minute=30)
    else:
        novo_horario_inicio = novo_horario_inicio.replace(minute=0)
    novo_horario_fim = novo_horario_inicio + timedelta(minutes=(intervalo * 30))

    return novo_horario_inicio, novo_horario_fim