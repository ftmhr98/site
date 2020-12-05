import database
import mysql.connector

cnx = mysql.connector.connect(user='root', password='@27061378',
                              host='localhost',
                              database='sitedb')
cursor = cnx.cursor()


class Database:
    def __init__(self, name):
        self._conn = mysql.connect(cnx)
        self._cursor = self._conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self.connection.commit()

    def close(self, commit=True):
        if commit:
            self.commit()
        self.connection.close()

    def execute(self, query, params=None):
        self.cursor.execute(query, params or ())

    def fetchall(self):
        return self.cursor.fetchall()

    def query(self, query, params=None):
        self.cursor.execute(query, params or ())
        return self.fetchall()

    def get_connection(self):
        if self.connection is None:
            self._conn = mysql.connect(cnx)
        else:
            mysql.connector.connect().close()
