from tests.mock import mock_criar_jornada_de_trabalho, mock_criar_barbeiro
from .mock_api import criar_usuario_e_token, criador_de_usuario, retrieve_token
from datetime import time

def test_criando_jornada_api(
    client,
    criador_de_usuario,
    criar_usuario_e_token,
):
    # Criando usuário e token
    _, token = criar_usuario_e_token(cpf="qualquer-cpf", email="qualquer-email")

    # PermissaoNegada: O usuário não possui permissões para realizar essa operação.
    response = client.post("jornada/criar", json={
        "barbeiro_cpf":"25811756054",
        "dia_da_semana":"Segunda",
        "horario_inicio":time(hour=17).isoformat(),
        "horario_fim":time(hour=7).isoformat(),
    }, headers={
        'Authorization': f'Bearer {token}',
    })

    assert response.status_code == 401
    assert response.json() == {"error":"PermissaoNegada","mensagem":"O usuário não possui permissões para realizar essa operação."}

    # Criando usuário e token de barbeiros
    usuario, token = criar_usuario_e_token(eh_barbeiro=True)

    # HorarioDaJornadaInvalido: "O horário de início é maior que o horário de fim." 
    response = client.post("jornada/criar", json={
        "barbeiro_cpf":usuario.cpf,
        "dia_da_semana":"Segunda",
        "horario_inicio":time(hour=17).isoformat(),
        "horario_fim":time(hour=7).isoformat(),
    }, headers={
        'Authorization': f'Bearer {token}',
    })

    assert response.status_code == 400
    assert response.json() == {"error":"HorarioDaJornadaInvalido","mensagem":"O horário de início é maior que o horário de fim."}

    # HorarioDaJornadaInvalido: "Caso haja uma pausa, é necessário ter um retorno. O inverso também." 
    response = client.post("jornada/criar", json={
        "barbeiro_cpf":usuario.cpf,
        "dia_da_semana":"Segunda",
        "horario_inicio":time(hour=7).isoformat(),
        "horario_pausa":time(hour=12).isoformat(),
        "horario_fim":time(hour=17).isoformat(),
    }, headers={
        'Authorization': f'Bearer {token}',
    })

    assert response.status_code == 400
    assert response.json() == {"error":"HorarioDaJornadaInvalido","mensagem":"Caso haja uma pausa, é necessário ter um retorno. O inverso também."}

    # HorarioDaJornadaInvalido: "O horário de pausa não pode ser maior que o horário de retorno." 
    response = client.post("jornada/criar", json={
        "barbeiro_cpf":usuario.cpf,
        "dia_da_semana":"Segunda",
        "horario_inicio":time(hour=7).isoformat(),
        "horario_pausa":time(hour=14).isoformat(),
        "horario_retorno":time(hour=12).isoformat(),
        "horario_fim":time(hour=17).isoformat(),
    }, headers={
        'Authorization': f'Bearer {token}',
    })

    assert response.status_code == 400
    assert response.json() == {"error":"HorarioDaJornadaInvalido","mensagem":"O horário de pausa não pode ser maior que o horário de retorno."}

    # HorarioDaJornadaInvalido: "O horário de pausa/retorno não deve estar fora da faixa do horário de início e fim." 
    response = client.post("jornada/criar", json={
        "barbeiro_cpf":usuario.cpf,
        "dia_da_semana":"Segunda",
        "horario_inicio":time(hour=7).isoformat(),
        "horario_pausa":time(hour=16).isoformat(),
        "horario_retorno":time(hour=18).isoformat(),
        "horario_fim":time(hour=17).isoformat(),
    }, headers={
        'Authorization': f'Bearer {token}',
    })

    assert response.status_code == 400
    assert response.json() == {"error":"HorarioDaJornadaInvalido","mensagem":"O horário de pausa/retorno não deve estar fora da faixa do horário de início e fim."}

    # DiaDaSemanaInvalido: "O dia da semana fornecido não condiz com nenhum valor salvo. Tente: Segunda, Terça, Quarta, Quinta, Sexta, Sábado ou Domingo."
    response = client.post("jornada/criar", json={
        "barbeiro_cpf":usuario.cpf,
        "dia_da_semana":"Sedomingo",
        "horario_inicio":time(hour=7).isoformat(),
        "horario_pausa":time(hour=12).isoformat(),
        "horario_retorno":time(hour=14).isoformat(),
        "horario_fim":time(hour=17).isoformat(),
    }, headers={
        'Authorization': f'Bearer {token}',
    })

    assert response.status_code == 400
    assert response.json() == {"error":"DiaDaSemanaInvalido","mensagem":"O dia da semana fornecido não condiz com nenhum valor salvo. Tente: Segunda, Terça, Quarta, Quinta, Sexta, Sábado ou Domingo."}

    # BarbeiroNaoEncontrado: "Não foi encontrado nenhum barbeiro com esse identificador."
    response = client.post("jornada/criar", json={
        "barbeiro_cpf":"1234567890",
        "dia_da_semana":"Segunda",
        "horario_inicio":time(hour=7).isoformat(),
        "horario_pausa":time(hour=12).isoformat(),
        "horario_retorno":time(hour=14).isoformat(),
        "horario_fim":time(hour=17).isoformat(),
    }, headers={
        'Authorization': f'Bearer {token}',
    })

    assert response.status_code == 404
    assert response.json() == {"error":"BarbeiroNaoEncontrado","mensagem":"Não foi encontrado nenhum barbeiro com esse identificador."}

    # Criando outro barbeiro existente no sistema
    usuario_2 = criador_de_usuario(cpf="55493147033", email="email@diferente.com", eh_barbeiro=True)

    # PermissaoNegada: Não é possível criar a jornada de outro barbeiro.
    response = client.post("jornada/criar", json={
        "barbeiro_cpf":usuario_2.cpf,
        "dia_da_semana":"Segunda",
        "horario_inicio":time(hour=7).isoformat(),
        "horario_fim":time(hour=17).isoformat(),
    }, headers={
        'Authorization': f'Bearer {token}',
    })

    assert response.status_code == 401
    assert response.json() == {"error":"PermissaoNegada","mensagem":"Não é possível criar a jornada de outro barbeiro."}

    # Criar jornada com pausa e retorno
    response = client.post("jornada/criar", json={
        "barbeiro_cpf":usuario.cpf,
        "dia_da_semana":"Segunda",
        "horario_inicio":time(hour=7).isoformat(),
        "horario_pausa":time(hour=12).isoformat(),
        "horario_retorno":time(hour=14).isoformat(),
        "horario_fim":time(hour=17).isoformat(),
    }, headers={
        'Authorization': f'Bearer {token}',
    })

    assert response.status_code == 201
    assert response.json() == {"mensagem":"Jornada criado com sucesso!"}

    # JornadaJaExistenteNoMesmoDia: "Já existe uma jornada para esse barbeiro no mesmo dia."
    response = client.post("jornada/criar", json={
        "barbeiro_cpf":usuario.cpf,
        "dia_da_semana":"Segunda",
        "horario_inicio":time(hour=7).isoformat(),
        "horario_pausa":time(hour=12).isoformat(),
        "horario_retorno":time(hour=14).isoformat(),
        "horario_fim":time(hour=17).isoformat(),
    }, headers={
        'Authorization': f'Bearer {token}',
    })

    assert response.status_code == 400
    assert response.json() == {"error":"JornadaJaExistenteNoMesmoDia","mensagem":"Já existe uma jornada para esse barbeiro no mesmo dia."}

    # Criar jornada sem pausa e retorno
    response = client.post("jornada/criar", json={
        "barbeiro_cpf":usuario.cpf,
        "dia_da_semana":"Domingo",
        "horario_inicio":time(hour=7).isoformat(),
        "horario_fim":time(hour=17).isoformat(),
    }, headers={
        'Authorization': f'Bearer {token}',
    })

    assert response.status_code == 201
    assert response.json() == {"mensagem":"Jornada criado com sucesso!"}

def test_consultando_jornada_api(
    client,
    mock_criar_jornada_de_trabalho
):
    # Consultando jornada existente
    response = client.get("jornada/jornada-001")
    assert response.status_code == 200
    assert response.json() == {
        "id":"jornada-001",
        "ativa":True,
        "barbeiro":{
            'cpf':'25811756054',
            'nome':'Barbeiro 01',
            'senha':'123',
            'email':'barbeiro1@teste.com',
            'telefone':None,
            'eh_barbeiro':True,
        },
        'dia_da_semana':"Segunda",
        'horario_inicio':time(hour=8).isoformat(),
        'horario_fim':time(hour=12).isoformat(),
        'horario_pausa':None,
        'horario_retorno':None,
    }

    # Consultando jornada inexistente
    response = client.get("jornada/jornada-999")
    assert response.status_code == 200
    assert response.json() == {}

def test_consultando_jornada_de_trabalho_api(
    client,
    mock_criar_jornada_de_trabalho
):
    # Consultando jornada de barbeiro existente
    response = client.get("jornada/barbeiro/25811756054")
    assert response.status_code == 200
    assert len(response.json()) == 7
    assert response.json()[0] == {
        "id":"jornada-001",
        "ativa":True,
        "barbeiro":{
            'cpf':'25811756054',
            'nome':'Barbeiro 01',
            'senha':'123',
            'email':'barbeiro1@teste.com',
            'telefone':None,
            'eh_barbeiro':True,
        },
        'dia_da_semana':"Segunda",
        'horario_inicio':time(hour=8).isoformat(),
        'horario_fim':time(hour=12).isoformat(),
        'horario_pausa':None,
        'horario_retorno':None,
    }

    # Consultando jornada de barbeiro inexistente
    response = client.get("jornada/barbeiro/123456789")
    assert response.status_code == 200
    assert response.json() == []

def test_alterando_jornada_api(
    client,
    criar_usuario_e_token,
    retrieve_token,
    mock_criar_barbeiro,
    mock_criar_jornada_de_trabalho,
):
    # Criando usuário e token
    _, token = criar_usuario_e_token(cpf="qualquer-cpf", email="qualquer-email")

    # PermissaoNegada: O usuário não possui permissões para realizar essa operação.
    response = client.patch("jornada/jornada-001", headers={
        'Authorization': f'Bearer {token}',
    })

    assert response.status_code == 401
    assert response.json() == {"error":"PermissaoNegada","mensagem":"O usuário não possui permissões para realizar essa operação."}

    # Criando usuário e token de barbeiros
    token = retrieve_token(email="barbeiro1@teste.com", senha="123")

    # Alterando jornada com sucesso
    response = client.patch("jornada/jornada-001", headers={
        'Authorization': f'Bearer {token}',
    })

    assert response.status_code == 200
    assert response.json() == {"mensagem":"Jornada alterada com sucesso!"}

    # PermissaoNegada: Não é possível alterar a jornada de outro barbeiro.
    response = client.patch("jornada/jornada-002", headers={
        'Authorization': f'Bearer {token}',
    })

    assert response.status_code == 401
    assert response.json() == {"error":"PermissaoNegada","mensagem":"Não é possível alterar a jornada de outro barbeiro."}

    # Adicionando jornada em um dia desativado
    response = client.post("jornada/criar", json={
        "barbeiro_cpf":"25811756054",
        "dia_da_semana":"Segunda",
        "horario_inicio":time(hour=6).isoformat(),
        "horario_pausa":time(hour=11).isoformat(),
        "horario_retorno":time(hour=13).isoformat(),
        "horario_fim":time(hour=16).isoformat(),
    }, headers={
        'Authorization': f'Bearer {token}',
    })

    assert response.status_code == 201
    assert response.json() == {"mensagem":"Jornada criado com sucesso!"}

    # Consultando jornada de barbeiro existente
    response = client.get("jornada/barbeiro/25811756054")
    
    assert response.status_code == 200
    assert len(response.json()) == 7

    # JornadaJaExistenteNoMesmoDia: Se essa jornada for ativada, existirão duas jornadas no mesmo dia. Jornada: {jornada_id}
    jornadas_do_barbeiro = response.json()

    response = client.patch("jornada/jornada-001", headers={
        'Authorization': f'Bearer {token}',
    })
    
    assert response.status_code == 400
    assert response.json() == {
        "error":"JornadaJaExistenteNoMesmoDia",
        "mensagem":f"Se essa jornada for ativada, existirão duas jornadas no mesmo dia. Desative a jornada: {jornadas_do_barbeiro[6]['id']}"
    }

    # JornadaNaoEncontrada: A jornada especificada não foi encontrada
    response = client.patch("jornada/jornada-999", headers={
        'Authorization': f'Bearer {token}',
    })
    assert response.status_code == 404
    assert response.json() == {"error":"JornadaNaoEncontrada","mensagem":"A jornada especificada não foi encontrada."}

def test_excluindo_jornada_api(
    client,
    criar_usuario_e_token,
    retrieve_token,
    mock_criar_barbeiro,
    mock_criar_jornada_de_trabalho,
):
    # Criando usuário e token
    _, token = criar_usuario_e_token(cpf="qualquer-cpf", email="qualquer-email")

    # PermissaoNegada: O usuário não possui permissões para realizar essa operação.
    response = client.patch("jornada/jornada-001", headers={
        'Authorization': f'Bearer {token}',
    })

    assert response.status_code == 401
    assert response.json() == {"error":"PermissaoNegada","mensagem":"O usuário não possui permissões para realizar essa operação."}

    # Criando usuário e token de barbeiros
    token = retrieve_token(email="barbeiro1@teste.com", senha="123")    

    # Excluindo jornada existente
    response = client.delete("jornada/jornada-001", headers={
        'Authorization': f'Bearer {token}',
    })
    
    assert response.status_code == 200
    assert response.json() == {"mensagem":"Jornada excluída com sucesso!"}

    # JornadaNaoEncontrada: A jornada especificada não foi encontrada
    response = client.delete("jornada/jornada-999", headers={
        'Authorization': f'Bearer {token}',
    })
    
    assert response.status_code == 404
    assert response.json()  == {"error":"JornadaNaoEncontrada","mensagem":"A jornada especificada não foi encontrada."}

    # PermissaoNegada: Não é possível alterar a jornada de outro barbeiro.
    response = client.delete("jornada/jornada-002", headers={
        'Authorization': f'Bearer {token}',
    })

    assert response.status_code == 401
    assert response.json() == {"error":"PermissaoNegada","mensagem":"Não é possível excluir a jornada de outro barbeiro."}