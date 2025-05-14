from typing import List, Optional
from abc import ABC, abstractmethod
from back.domain.models import Pessoa

class AbstractPessoaRepository(ABC):
    @abstractmethod
    def criar_pessoa(self, cpf: str, nome: str, email: str, telefone: str, senha: str) -> Pessoa:
        """
        Cria uma nova pessoa.
        Args:
            cpf: CPF da pessoa
            nome: Nome da pessoa
            email: Email da pessoa
            telefone: Telefone da pessoa
            senha: Senha da pessoa
        Returns:
            Pessoa criada
        """
        raise NotImplementedError

    @abstractmethod
    def buscar_pessoa_por_cpf(self, cpf: str) -> Optional[Pessoa]:
        """
        Busca uma pessoa pelo CPF.
        Args:
            cpf: CPF da pessoa
        Returns:
            Pessoa encontrada ou None se não existir
        """
        raise NotImplementedError

    @abstractmethod
    def buscar_pessoa_por_email(self, email: str) -> Optional[Pessoa]:
        """
        Busca uma pessoa pelo email.
        Args:
            email: Email da pessoa
        Returns:
            Pessoa encontrada ou None se não existir
        """
        raise NotImplementedError

    @abstractmethod
    def listar_pessoas(self) -> List[Pessoa]:
        """
        Lista todas as pessoas cadastradas.
        Returns:
            Lista de pessoas
        """
        raise NotImplementedError

    @abstractmethod
    def atualizar_dados(self, cpf: str, nome: str = None, email: str = None, 
                       telefone: str = None, senha: str = None) -> Optional[Pessoa]:
        """
        Atualiza os dados de uma pessoa.
        Args:
            cpf: CPF da pessoa
            nome: Novo nome da pessoa
            email: Novo email da pessoa
            telefone: Novo telefone da pessoa
            senha: Nova senha da pessoa
        Returns:
            Pessoa atualizada ou None se não existir
        """
        raise NotImplementedError

    @abstractmethod
    def remover_pessoa(self, cpf: str) -> bool:
        """
        Remove uma pessoa pelo CPF.
        Args:
            cpf: CPF da pessoa
        Returns:
            True se removida com sucesso, False caso contrário
        """
        raise NotImplementedError 