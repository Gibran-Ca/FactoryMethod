from abc import ABC, abstractmethod
from db_connector.connection_factory import ConnectionFactory

class AbstractDBFactory(ABC):
    @abstractmethod
    def create_mysql_factory(self) -> ConnectionFactory:
        pass

    @abstractmethod
    def create_mariadb_factory(self) -> ConnectionFactory:
        pass

    @abstractmethod
    def create_postgresql_factory(self) -> ConnectionFactory:
        pass

    @abstractmethod
    def create_sqlite_factory(self) -> ConnectionFactory:
        pass
