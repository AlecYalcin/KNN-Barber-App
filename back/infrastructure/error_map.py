# Arquivo de mapeamento das mensagens de erro

ERROR_MAP = {
    "HorarioIndisponivelParaBarbeiro": {
        "status_code": 400,
        "message": "O horário escolhido não está disponível para o barbeiro.",
    },
    "HorarioIndisponivelParaCliente": {
        "status_code": 400,
        "message": "O horário escolhido não está disponível para o cliente.",
    },
    "HorarioInvalido": {
        "status_code": 400,
        "message": "O horário informado é inválido.",
    },
    "HorarioForaDaJornada": {
        "status_code": 400,
        "message": "O horário informado está fora da jornada de trabalho.",
    },
    "HorarioIndisponivelException": {
        "status_code": 400,
        "message": "O horário não está disponível para agendamento.",
    },
    "HorarioOcupado": {
        "status_code": 400,
        "message": "O horário já está ocupado.",
    },
    "HorarioInsuficiente": {
        "status_code": 400,
        "message": "O tempo de atendimento é insuficiente para o serviço.",
    },
    "CPFInvalido": {
        "status_code": 400,
        "message": "O CPF informado é inválido.",
    },
    "CPFEmUso": {
        "status_code": 400,
        "message": "O CPF informado já está em uso.",
    },
    "EmailInvalido": {
        "status_code": 400,
        "message": "O e-mail informado é inválido.",
    },
    "EmailEmUso": {
        "status_code": 400,
        "message": "O e-mail informado já está em uso.",
    },
    "UsuarioNaoEncontrado": {
        "status_code": 404,
        "message": "Usuário não encontrado.",
    },
    "DuracaoInvalida": {
        "status_code": 400,
        "message": "Duração do serviço precisa estar entre 5min e 120min",
    },
    "ServicoNaoEncontrado": {
        "status_code": 404,
        "message": "Serviço não encontrado.",
    },
    "PrecoInvalido":{
        "status_code": 400,
        "message": "O preço do serviço precisa ser maior que zero."
    }
}
