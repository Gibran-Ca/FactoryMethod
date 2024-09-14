import MySQLdb
from db_connector.connection import Connection

class MariaDBConnection(Connection):
    def __init__(self, host, user, password, db):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.connection = None

    def connect(self):
        self.connection = MySQLdb.connect(
            host=self.host,
            user=self.user,
            passwd=self.password,
            db=self.db
        )
        print("Connected to MariaDB")

    def close(self):
        if self.connection:
            self.connection.close()
            print("MariaDB connection closed")
