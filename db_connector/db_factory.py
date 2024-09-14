from db_connector.abstract_factory import AbstractDBFactory
from db_connector.mysql_factory import MySQLConnectionFactory
from db_connector.mariadb_factory import MariaDBConnectionFactory
from db_connector.postgresql_factory import PostgreSQLConnectionFactory
from db_connector.sqlite_factory import SQLiteConnectionFactory

class ConcreteDBFactory(AbstractDBFactory):
    def create_mysql_factory(self) -> MySQLConnectionFactory:
        return MySQLConnectionFactory()

    def create_mariadb_factory(self) -> MariaDBConnectionFactory:
        return MariaDBConnectionFactory()

    def create_postgresql_factory(self) -> PostgreSQLConnectionFactory:
        return PostgreSQLConnectionFactory()

    def create_sqlite_factory(self) -> SQLiteConnectionFactory:
        return SQLiteConnectionFactory()
