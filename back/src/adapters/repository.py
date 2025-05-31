import abc
from typing import Any
from sqlalchemy.orm import Session

class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def adicionar(self, objeto: Any):
        pass

    @abc.abstractmethod
    def consultar(self, id: str) -> Any:
        pass
    
    @abc.abstractmethod
    def remover(self, id: str):
        pass

class AbstractSQLAlchemyRepository(AbstractRepository):
    def __init__(self, session: Session):
        self.session = session

    def adicionar(self, objeto: Any):
        raise NotImplementedError

    def consultar(self, id: str) -> Any:
        raise NotImplementedError

    def remover(self, id: str):
        raise NotImplementedError
