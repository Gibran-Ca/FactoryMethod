import psycopg2
from db_connector.connection import Connection

class PostgreSQLConnection(Connection):
    def __init__(self, host, user, password, db):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.connection = None

    def connect(self):
        self.connection = psycopg2.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            dbname=self.db
        )
        print("Connected to PostgreSQL")

    def close(self):
        if self.connection:
            self.connection.close()
            print("PostgreSQL connection closed")
