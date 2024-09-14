from .abstract_factory import ConnectionFactory

from db_connector.mariadb_connection import MariaDBConnection

class MariaDBConnectionFactory(ConnectionFactory):
    def create_connection(self) -> MariaDBConnection:
        return MariaDBConnection(
            host='localhost',
            user='root',
            password='',
            db='prueba'
        )
