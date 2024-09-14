from .abstract_factory import ConnectionFactory
from db_connector.sql_connection import SQLiteConnection

class SQLiteConnectionFactory(ConnectionFactory):
    def create_connection(self) -> SQLiteConnection:
        return SQLiteConnection(
            db_path='prueba.db'
        )
