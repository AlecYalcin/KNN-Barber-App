class DomainError(Exception):
    pass

# Autorização

class TokenInvalido(DomainError):
    pass

# Agendamento

class HorarioIndisponivelParaBarbeiro(DomainError):
    pass

class HorarioIndisponivelParaCliente(DomainError):
    pass

class HorarioInvalido(DomainError):
    pass

class HorarioForaDaJornada(DomainError):
    pass

class HorarioIndisponivelException(DomainError):
    pass

class HorarioOcupado(DomainError):
    pass

class HorarioInsuficiente(DomainError):
    pass

# Usuario

class CPFInvalido(DomainError):
    pass

class CPFEmUso(DomainError):
    pass

class EmailInvalido(DomainError):
    pass

class EmailEmUso(DomainError):
    pass

class UsuarioNaoEncontrado(DomainError):
    pass

# Serviço

class DuracaoInvalida(DomainError):
    pass

class PrecoInvalido(DomainError):
    pass

class ServicoNaoEncontrado(DomainError):
    pass

# Jornada

class JornadaNaoEncontrada(DomainError):
    pass

class JornadaJaExistenteNoMesmoDia(DomainError):
    pass

class HorarioDaJornadaInvalido(DomainError):
    pass

class DiaDaSemanaInvalido(DomainError):
    pass

# Horário Indisponível

class HorarioIndisponivelNaoEncontrado(DomainError):
    pass

class HorarioIndisponivelInvalido(DomainError):
    pass

# Barbeiro

class BarbeiroNaoEncontrado(DomainError):
    pass