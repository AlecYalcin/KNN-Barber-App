from datetime import datetime, time
from src.domain.models import Jornada, DiaDaSemana, HorarioIndisponivel
from tests.mock import mock_usuario_teste

def test_verificador_de_horarios(mock_usuario_teste):
    usuario = mock_usuario_teste

    jornada = Jornada(
        ativa=True,
        dia_da_semana=DiaDaSemana.SEGUNDA,
        barbeiro=usuario,
        horario_inicio=time(7),
        horario_fim=time(17),
        horario_pausa=time(11),
        horario_retorno=time(13),
    )
    
    # Horários em dias diferentes da jornada
    horario_1, horario_2 = datetime(2025, 5, 27, 6), datetime(2025, 5, 27, 9)
    resultado = jornada.verificar_se_horario_esta_na_jornada((horario_1, horario_2))
    assert resultado == False

    # Horários fora do horário de início e dentro do horário de fim
    horario_1, horario_2 = datetime(2025, 5, 26, 6), datetime(2025, 5, 26, 9)
    resultado = jornada.verificar_se_horario_esta_na_jornada((horario_1, horario_2))
    assert resultado == False

    # Horários dentro do horário de início e fora do horário de fim
    horario_1, horario_2 = datetime(2025, 5, 26, 16), datetime(2025, 5, 26, 18)
    resultado = jornada.verificar_se_horario_esta_na_jornada((horario_1, horario_2))
    assert resultado == False

    # Horários fora do horário de início e fim
    horario_1, horario_2 = datetime(2025, 5, 26, 6), datetime(2025, 5, 26, 18)
    resultado = jornada.verificar_se_horario_esta_na_jornada((horario_1, horario_2))
    assert resultado == False

    # Horários dentro da jornada e dentro da pausa
    horario_1, horario_2 = datetime(2025, 5, 26, 11), datetime(2025, 5, 26, 13)
    resultado = jornada.verificar_se_horario_esta_na_jornada((horario_1, horario_2))
    assert resultado == False

    # Horários dentro da jornada e fora da pausa
    horario_1, horario_2 = datetime(2025, 5, 26, 7), datetime(2025, 5, 26, 10)
    resultado = jornada.verificar_se_horario_esta_na_jornada((horario_1, horario_2))
    assert resultado == True

def test_verificador_de_horario_indisponivel(mock_usuario_teste):
    usuario = mock_usuario_teste

    horario_indisponivel = HorarioIndisponivel(
        horario_inicio=datetime(2025, 5, 27, 0),
        horario_fim=datetime(2025, 5, 29, 0),
        justificativa="Aniversário",
        barbeiro=usuario,
    )

    # Horários fora do horário de início e dentro do horário de fim
    horario_1, horario_2 = datetime(2025, 5, 26, 12), datetime(2025, 5, 27, 12)
    resultado = horario_indisponivel.verificar_se_horario_esta_livre((horario_1, horario_2))
    assert resultado == False

    # Horários dentro do horário de início e fora do horário de fim
    horario_1, horario_2 = datetime(2025, 5, 28, 12), datetime(2025, 5, 29, 12)
    resultado = horario_indisponivel.verificar_se_horario_esta_livre((horario_1, horario_2))
    assert resultado == False

    # Horários dentro do horário de início e fim
    horario_1, horario_2 = datetime(2025, 5, 28, 0), datetime(2025, 5, 28, 12)
    resultado = horario_indisponivel.verificar_se_horario_esta_livre((horario_1, horario_2))
    assert resultado == False

    # Horários fora do horário de início e fim
    horario_1, horario_2 = datetime(2025, 5, 26, 12), datetime(2025, 5, 26, 14)
    resultado = horario_indisponivel.verificar_se_horario_esta_livre((horario_1, horario_2))
    assert resultado == True
    
    horario_1, horario_2 = datetime(2025, 5, 29, 12), datetime(2025, 5, 29, 14)
    resultado = horario_indisponivel.verificar_se_horario_esta_livre((horario_1, horario_2))
    assert resultado == True