
import MySQLdb
from db_connector.connection import Connection

class MySQLConnection(Connection):
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
        print("Connected to MySQL")

    def close(self):
        if self.connection:
            self.connection.close()
            print("MySQL connection closed")
