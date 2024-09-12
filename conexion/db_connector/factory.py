
from abc import ABC, abstractmethod
from db_connector.connection import Connection

class ConnectionFactory(ABC):
    @abstractmethod
    def create_connection(self) -> Connection:
        pass
