import sqlite3
from db_connector.connection import Connection

class SQLiteConnection(Connection):
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = None

    def connect(self):
        self.connection = sqlite3.connect(self.db_path)
        print("Connected to SQLite")

    def close(self):
        if self.connection:
            self.connection.close()
            print("SQLite connection closed")
