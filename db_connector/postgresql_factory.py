from .abstract_factory import ConnectionFactory

from db_connector.postgresql_connection import PostgreSQLConnection

class PostgreSQLConnectionFactory(ConnectionFactory):
    def create_connection(self) -> PostgreSQLConnection:
        return PostgreSQLConnection(
            host='localhost',
            user='postgres',
            password='',
            db='prueba'
        )
