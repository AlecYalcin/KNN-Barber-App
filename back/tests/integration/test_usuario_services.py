import pytest
from src.domain.models import Usuario
from src.domain.exceptions import *
from src.service.services.usuario import *
from src.service.unit_of_work import UnidadeDeTrabalho
from tests.mock import *

def test_criar_usuario_service(session_maker):
    usuario = Usuario(
        cpf="12345678900",
        nome="Usuário Teste",
        email="email_invalido",
        senha="senhateste",
    )

    # Criação de usuário com CPF inválido
    with pytest.raises(CPFInvalido):
        criar_usuario(
            uow=UnidadeDeTrabalho(session_maker),
            cpf=usuario.cpf,
            nome=usuario.nome,
            email=usuario.email,
            senha=usuario.senha,
        )

    # Criação de usuário com Email inválido
    usuario.cpf = "54304796089"
    with pytest.raises(EmailInvalido):
        criar_usuario(
            uow=UnidadeDeTrabalho(session_maker),
            cpf=usuario.cpf,
            nome=usuario.nome,
            email=usuario.email,
            senha=usuario.senha,
        )

    # Criação de usuário com sucesso
    usuario.email = "email@teste.com.br"
    criar_usuario(
        uow=UnidadeDeTrabalho(session_maker),
        cpf=usuario.cpf,
        nome=usuario.nome,
        email=usuario.email,
        senha=usuario.senha,
    )

    with UnidadeDeTrabalho(session_maker) as uow:
        usuario_encontrado = uow.usuarios.consultar(usuario.cpf)
        assert usuario_encontrado == usuario

    # Criação de usuário com CPF já existente
    with pytest.raises(CPFEmUso):
        criar_usuario(
            uow=UnidadeDeTrabalho(session_maker),
            cpf=usuario.cpf,
            nome=usuario.nome,
            email=usuario.email,
            senha=usuario.senha,
        )

    # Criação de usuário com Email já existente
    usuario.cpf = "69980389095"
    with pytest.raises(EmailEmUso):
        criar_usuario(
            uow=UnidadeDeTrabalho(session_maker),
            cpf=usuario.cpf,
            nome=usuario.nome,
            email=usuario.email,
            senha=usuario.senha,
        )

def test_consultar_usuario_service(session_maker, mock_usuario_teste):
    usuario = mock_usuario_teste

    # Criando usuário através do repositório
    with UnidadeDeTrabalho(session_maker) as uow:
        uow.usuarios.adicionar(usuario)
        uow.commit()

    # Pesquisando por CPF
    usuario_encontrado = consultar_usuario(uow=UnidadeDeTrabalho(session_maker), cpf=usuario.cpf)
    assert usuario_encontrado == usuario.to_dict()
    
    # Pesquisando por Nome
    usuario_encontrado = consultar_usuario(uow=UnidadeDeTrabalho(session_maker), email=usuario.email)
    assert usuario_encontrado == usuario.to_dict()

    # Pesquisando por um CPF inexistente
    usuario_inexistente = consultar_usuario(uow=UnidadeDeTrabalho(session_maker), cpf="111.222.333.444-55")
    assert usuario_inexistente == {}

    # Pesquisando por um Email inexistente
    usuario_inexistente = consultar_usuario(uow=UnidadeDeTrabalho(session_maker), email="email@inexistente.com")
    assert usuario_inexistente == {}

def test_deletar_usuario_service(session_maker, mock_usuario_teste):
    usuario = mock_usuario_teste

    # Criando usuário através do repositório
    with UnidadeDeTrabalho(session_maker) as uow:
        uow.usuarios.adicionar(usuario)
        uow.commit()

    # Removendo usuario
    remover_usuario(
        uow=UnidadeDeTrabalho(session_maker),
        cpf=usuario.cpf,
    )

    # Procurando por usuario
    with UnidadeDeTrabalho(session_maker) as uow:
        usuario_encontrado = uow.usuarios.consultar(cpf=usuario.cpf)
        assert usuario_encontrado is None
    
    # Tenteando remover novamente
    with pytest.raises(UsuarioNaoEncontrado):
        remover_usuario(
            uow=UnidadeDeTrabalho(session_maker),
            cpf=usuario.cpf,
        )

def test_alterar_usuario_service(session_maker, mock_usuario_teste):
    usuario = mock_usuario_teste

    usuario_teste = Usuario(
        cpf="999.888.777-54",
        nome="Usuário Teste 02",
        email="email@utilizado.com.br",
        senha="senhateste",
    )

    # Criando usuário através do repositório
    with UnidadeDeTrabalho(session_maker) as uow:
        uow.usuarios.adicionar(usuario)
        uow.usuarios.adicionar(usuario_teste)
        uow.commit()

    # Atualizando usuário com e-mail inválido
    with pytest.raises(EmailInvalido):
        atualizar_usuario(
            uow=UnidadeDeTrabalho(session_maker),
            cpf=usuario.cpf,
            novo_email="email-invalido",
            nova_senha="senha1234",
        )

    # Atualizando usuário com CPF inexistente
    with pytest.raises(UsuarioNaoEncontrado):
        atualizar_usuario(
            uow=UnidadeDeTrabalho(session_maker),
            cpf="111.222.333-44",
            novo_email="email@valido.com.br",
            nova_senha="senha1234",
        )

    # Atualizando usuário com e-mail em uso
    with pytest.raises(EmailEmUso):
        atualizar_usuario(
            uow=UnidadeDeTrabalho(session_maker),
            cpf=usuario.cpf,
            novo_email="email@utilizado.com.br",
        )

    # Atualiznado usuário com sucesso
    atualizar_usuario(
        uow=UnidadeDeTrabalho(session_maker),
        cpf=usuario.cpf,
        novo_nome="Novo Usuário",
        novo_email="usuario@gmail.com.br",
        nova_senha="senha_1234",
        novo_telefone="(84) 98888-2222"
    )

    with UnidadeDeTrabalho(session_maker) as uow:
        usuario_alterado = uow.usuarios.consultar(usuario.cpf)
        assert usuario_alterado.nome == "Novo Usuário"
        assert usuario_alterado.email == "usuario@gmail.com.br"
        assert usuario_alterado.senha == "senha_1234"
        assert usuario_alterado.telefone == "(84) 98888-2222"