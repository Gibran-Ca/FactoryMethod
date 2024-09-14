
from .abstract_factory import ConnectionFactory


from db_connector.mysql_connection import MySQLConnection

class MySQLConnectionFactory(ConnectionFactory):
    def create_connection(self) -> MySQLConnection:
        return MySQLConnection(
            host='localhost',
            user='root',
            password='',
            db='prueba'
        )
