from typing import List, Optional
from datetime import date
from back.domain.models import Barbeiro

class IBarbeiroRepository:
    def adicionar(self, barbeiro: Barbeiro) -> None:
        """
        Adiciona um novo barbeiro ao repositório.
        Args:
            barbeiro: Instância de Barbeiro a ser adicionada
        """
        raise NotImplementedError

    def obter(self, id: str) -> Optional[Barbeiro]:
        """
        Obtém um barbeiro pelo seu ID (CPF).
        Args:
            id: CPF do barbeiro
        Returns:
            Barbeiro encontrado ou None se não existir
        """
        raise NotImplementedError

    def listar(self) -> List[Barbeiro]:
        """
        Lista todos os barbeiros cadastrados.
        Returns:
            Lista de barbeiros
        """
        raise NotImplementedError

    def remover(self, id: str) -> bool:
        """
        Remove um barbeiro pelo seu ID (CPF).
        Args:
            id: CPF do barbeiro
        Returns:
            True se removido com sucesso, False caso contrário
        """
        raise NotImplementedError

    def buscar_por_email(self, email: str) -> Optional[Barbeiro]:
        """
        Busca um barbeiro pelo email.
        Args:
            email: Email do barbeiro
        Returns:
            Barbeiro encontrado ou None se não existir
        """
        raise NotImplementedError

    def buscar_por_cpf(self, cpf: str) -> Optional[Barbeiro]:
        """
        Busca um barbeiro pelo CPF.
        Args:
            cpf: CPF do barbeiro
        Returns:
            Barbeiro encontrado ou None se não existir
        """
        raise NotImplementedError

    def buscar_disponiveis_por_data(self, data: date) -> List[Barbeiro]:
        """
        Busca barbeiros disponíveis em uma data específica.
        Args:
            data: Data para verificar disponibilidade
        Returns:
            Lista de barbeiros disponíveis na data
        """
        raise NotImplementedError

    def buscar_com_jornadas(self) -> List[Barbeiro]:
        """
        Busca barbeiros com suas jornadas de trabalho carregadas.
        Returns:
            Lista de barbeiros com suas respectivas jornadas
        """
        raise NotImplementedError 