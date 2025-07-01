import pytest
from src.domain.models import Servico
from src.domain.exceptions import *
from src.service.services.servico import *
from src.service.unit_of_work import UnidadeDeTrabalho
from tests.mock import *

def test_criar_servico_service(session_maker):
    servico = Servico(
        nome="Serviço Teste",
        descricao="Serviço de Teste",
        preco=0,
        duracao=0,
    )

    # Criação de Serviço com Duração Inválida
    with pytest.raises(DuracaoInvalida):
        criar_servico(
            uow=UnidadeDeTrabalho(session_maker),
            nome=servico.nome,
            descricao=servico.descricao,
            preco=servico.preco,
            duracao=servico.duracao,
        )

    # Criação de Serviço com Preço Inválido
    servico.duracao = 16
    with pytest.raises(PrecoInvalido):
        criar_servico(
            uow=UnidadeDeTrabalho(session_maker),
            nome=servico.nome,
            descricao=servico.descricao,
            preco=servico.preco,
            duracao=servico.duracao,
        )

    # Criação de Serviço Válido
    servico.preco = 16
    criar_servico(
        uow=UnidadeDeTrabalho(session_maker),
        nome=servico.nome,
        descricao=servico.descricao,
        preco=servico.preco,
        duracao=servico.duracao,
    )

    # Verificando criação
    with UnidadeDeTrabalho(session_maker) as uow:
        servico_encontrado = uow.servicos.consultar_por_nome(nome=servico.nome)[0]
        assert servico_encontrado.nome == servico.nome
        assert servico_encontrado.preco == servico.preco
        assert servico_encontrado.duracao == servico.duracao
        assert servico_encontrado.descricao == servico.descricao

def test_consultar_servico_service(session_maker, mock_servicos_teste):
    # Adicionando serviços
    servicos = mock_servicos_teste
    with UnidadeDeTrabalho(session_maker) as uow:
        for servico in servicos:
            uow.servicos.adicionar(servico)
        uow.commit()

    # Consultando serviços por nome
    for servico in servicos:
        servico_encontrado = consultar_servico(
            uow=UnidadeDeTrabalho(session_maker),
            id=servico.id,
        )
        assert servico_encontrado == servico.to_dict()

    # Consultando serviço inexistente
    servico_encontrado = consultar_servico(
        uow=UnidadeDeTrabalho(session_maker),
        id="12345667783ç4dfsdsad"
    )
    assert servico_encontrado == {}

def test_listar_servicos_service(session_maker, mock_servicos_teste):
    # Adicionando serviços
    servicos = mock_servicos_teste
    servicos_dict = [servico.to_dict() for servico in servicos]
    with UnidadeDeTrabalho(session_maker) as uow:
        for servico in servicos:
            uow.servicos.adicionar(servico)
        uow.commit()

    # Listar todos os serviços sem filtro
    servicos_encontrados = listar_servicos(
        uow=UnidadeDeTrabalho(session_maker),
    )

    assert servicos_encontrados == servicos_dict
    # Listar todos os serviços com filtro
    servicos_encontrados_por_nome = listar_servicos(
        uow=UnidadeDeTrabalho(session_maker),
        filtro="Corte"
    )

    assert servicos_encontrados_por_nome == [servicos_dict[0], servicos_dict[2]]

    # Listar os serviços com filtro inexistente
    servicos_encontrados_inexistentes = listar_servicos(
        uow=UnidadeDeTrabalho(session_maker),
        filtro="Serviço Inexistente",
    )

    assert servicos_encontrados_inexistentes == []

def test_alterar_servico_service(session_maker, mock_servicos_teste):
    # Adicionando serviço
    servico = mock_servicos_teste[0]
    with UnidadeDeTrabalho(session_maker) as uow:
        uow.servicos.adicionar(servico)
        uow.commit()

    # Alterando serviço inexistente
    with pytest.raises(ServicoNaoEncontrado):
        atualizar_servico(
            uow=UnidadeDeTrabalho(session_maker),
            id="1234567890abcdefghijklmnopqrstuv"
        )

    # Alterando serviço com horário inválido
    with pytest.raises(DuracaoInvalida):
        atualizar_servico(
            uow=UnidadeDeTrabalho(session_maker),
            id=servico.id,
            nova_duracao=-15,
            novo_preco=30,
        )

    # Alterando serviço com preço inválido
    with pytest.raises(PrecoInvalido):
        atualizar_servico(
            uow=UnidadeDeTrabalho(session_maker),
            id=servico.id,
            nova_duracao=15,
            novo_preco=-15,
        )

    # Alterando serviço com sucesso
    atualizar_servico(
        uow=UnidadeDeTrabalho(session_maker),
        id=servico.id,
        novo_nome="Corte de Barba",
        nova_descricao="Corte de barbas curta, bigode e cavanhaque.",
        nova_duracao=30,
        novo_preco=15,
    )

    # Pesquisando e assegurando serviço alterado
    with UnidadeDeTrabalho(session_maker) as uow:
        servico_encontrado = uow.servicos.consultar(servico.id)
        assert servico_encontrado.nome == "Corte de Barba"
        assert servico_encontrado.descricao == "Corte de barbas curta, bigode e cavanhaque."
        assert servico_encontrado.duracao == 30
        assert servico_encontrado.preco == 15        

def test_remover_servico_service(session_maker, mock_servicos_teste):
    # Adicionando serviço
    servico = mock_servicos_teste[0]
    with UnidadeDeTrabalho(session_maker) as uow:
        uow.servicos.adicionar(servico)
        uow.commit()

    # Verificando que existe
    with UnidadeDeTrabalho(session_maker) as uow:
        servico_encontrado = uow.servicos.consultar(servico.id)
        assert servico_encontrado == servico

    # Removendo serviço inexistente
    with pytest.raises(ServicoNaoEncontrado):
        remover_servico(
            uow=UnidadeDeTrabalho(session_maker),
            id='1234567890asdfghjkl'
        )

    # Removendo serviço existente
    remover_servico(
        uow=UnidadeDeTrabalho(session_maker),
        id=servico.id,
    )

    # Verificando remoção
    with UnidadeDeTrabalho(session_maker) as uow:
        servico_encontrado = uow.servicos.consultar(servico.id)
        assert servico_encontrado == None