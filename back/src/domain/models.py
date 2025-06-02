from uuid import uuid4
from dataclasses import dataclass, field
from datetime import time, datetime, timedelta
import re

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

    @staticmethod
    def validar_cpf(cpf: str) -> bool:
        # Remove caracteres não numéricos
        cpf = re.sub(r'[^0-9]', '', cpf)

        # CPF precisa ter 11 dígitos
        if len(cpf) != 11:
            return False

        # Validação do primeiro dígito
        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        digito1 = (soma * 10 % 11) % 10

        # Validação do segundo dígito
        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        digito2 = (soma * 10 % 11) % 10

        # Verifica se os dígitos calculados batem com os informados
        if not cpf[-2:] == f"{digito1}{digito2}":
            return False
        
        return True

    @staticmethod
    def validar_email(email: str) -> bool:
        padrao = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(padrao, email):
            return False
        return True

    def __eq__(self, other: any):
        if not isinstance(other, Usuario):
            return False
        return self.cpf == other.cpf and self.email == other.email
    
    def __hash__(self):
        return hash(self.cpf, self.email)

@dataclass
class Servico:
    nome: str
    descricao: str
    preco: float
    duracao: int
    id: str = field(default_factory=lambda: str(uuid4()))

    def __eq__(self, other: any):
        if not isinstance(other, Servico):
            return False
        return self.id == other.id and self.nome == other.nome
    
    def __hash__(self):
        return hash((self.id, self.nome))

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

    def verificar_se_horario_esta_na_jornada(self, horarios: tuple[datetime]) -> bool:
        horario_1, horario_2 = horarios

        # Está no mesmo dia?
        if not (
            self.dia_da_semana == DiaDaSemana.horario_para_dia(horario=horario_1)
            and self.dia_da_semana == DiaDaSemana.horario_para_dia(horario=horario_2)
        ):
            return False

        # Está nos horários padrão?
        if not (
            horario_1.time() >= self.horario_inicio 
            and horario_2.time() <= self.horario_fim
        ):
            return False

        # Está fora da pausa?
        if (
            (self.horario_pausa and self.horario_retorno)
            and (horario_1.time() < self.horario_retorno
            and horario_2.time() > self.horario_pausa)
        ):
            return False

        return True

    def __eq__(self, other: any):
        if not isinstance(other, Jornada):
            return False
        return self.id == other.id and self.barbeiro == other.barbeiro
    
    def __hash__(self):
        return hash((self.id, self.barbeiro.cpf))

@dataclass
class HorarioIndisponivel:
    horario_inicio: datetime 
    horario_fim: datetime
    justificativa: str
    barbeiro: Usuario
    id: str = field(default_factory=lambda: str(uuid4()))

    def verificar_se_horario_esta_livre(self, horarios: tuple[datetime]) -> bool:
        horario_1, horario_2 = horarios

        # Acontece no intervalo de mesmo dia e horário?
        if horario_1 <= self.horario_fim and horario_2 >= self.horario_inicio:
            return False
        return True

    def __eq__(self, other: any):
        if not isinstance(other, HorarioIndisponivel):
            return False
        return self.id == other.id and self.barbeiro == other.barbeiro
    
    def __hash__(self):
        return hash((self.id, self.barbeiro.cpf))

@dataclass
class Agendamento:
    horario_inicio: datetime
    horario_fim: datetime
    barbeiro: Usuario
    cliente: Usuario
    servicos: list[Servico]
    id: str = field(default_factory=lambda: str(uuid4()))

    def __eq__(self, other: any):
        if not isinstance(other, Agendamento):
            return False
        return self.id == other.id and self.barbeiro == other.barbeiro and self.cliente == other.cliente
    
    def __hash__(self):
        return hash((self.id, self.barbeiro.cpf, self.cliente.cpf))

@dataclass
class Pagamento:
    valor: float
    data: datetime
    metodo: MetodoPagamento
    agendamento: Agendamento
    id: str = field(default_factory=lambda: str(uuid4()))

    def __eq__(self, other: any):
        if not isinstance(other, Pagamento):
            return False
        return self.id == other.id and self.agendamento == other.agendamento
    
    def __hash__(self):
        return hash((self.id, self.agendamento.id))

# Agregados
@dataclass
class Barbeiro():
    usuario: Usuario = field(default_factory=Usuario)
    jornada_de_trabalho: list[Jornada] = field(default_factory=list)
    horarios_indisponiveis: list[HorarioIndisponivel] = field(default_factory=list)

    def verificar_se_horario_esta_na_jornada(self, horarios: tuple[datetime]) -> bool:
        for jornada in self.jornada_de_trabalho:
            if jornada.verificar_se_horario_esta_na_jornada(horarios):
                return True
        return False
    
    def verificar_se_horario_esta_disponivel(self, horarios: tuple[datetime]) -> bool:
        for h_indisponivel in self.horarios_indisponiveis:
            if not h_indisponivel.verificar_se_horario_esta_livre(horarios):
                return False
        return True
    
    def __eq__(self, value: Usuario) -> bool:
        if isinstance(value, Barbeiro) and value.usuario.cpf == self.usuario.cpf:
            return True
        return False

# Funções
def criar_agendamento(cliente: Usuario, barbeiro: Barbeiro, servicos: list[Servico], horarios: tuple[datetime]) -> Agendamento:
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
    horarios = normalizar_horarios(horarios)

    # Verificar se o horário é suficiente para os serviços
    tempo_necessario = timedelta(minutes=sum(servico.duracao for servico in servicos))
    if tempo_necessario > (horarios[1] - horarios[0]):
        raise HorarioInsuficiente("Os horários escolhidos não cobrem a quantidade de tempo mínimo para realizar os serviçs.")

    # Verifica se está dentro da jornada de trabalho do barbeiro
    if not barbeiro.verificar_se_horario_esta_na_jornada(horarios):
        raise HorarioForaDaJornada("O horário escolhido está fora da jornada do barbeiro.")

    # Verifica se está dentro de algum horário indisponível
    if not barbeiro.verificar_se_horario_esta_disponivel(horarios):
        raise HorarioIndisponivelException("O horário escolhido está indisponível de acordo com a disponibilidade do barbeiro.")

    return Agendamento(
        id=str(uuid4()),
        horario_inicio=horarios[0],
        horario_fim=horarios[1],
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