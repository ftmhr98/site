import mysql.connector


class Database:
    def __init__(self):
        self._conn = mysql.connector.connect(user='root', password='@27061378',
                                             host='localhost',
                                             database='sitedb')

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

        # def execute(self, query, *params):
        #     self.cursor.execute(query, params)

    def fetchall(self):
        return self.cursor.fetchall()

    @staticmethod
    def query(query, params):
        conn = mysql.connector.connect(user='root', password='@27061378',
                                       host='localhost',
                                       database='sitedb')

        cursors = conn.cursor()
        cursors.execute(query, params)
        conn.commit()

    @staticmethod
    def query_2(query, *params):
        conn = mysql.connector.connect(user='root', password='@27061378',
                                       host='localhost',
                                       database='sitedb')

        cursors = conn.cursor()
        cursors.execute(query, params)
        conn.commit()

    @staticmethod
    def execute(query, params):
        conn = mysql.connector.connect(user='root', password='@27061378',
                                       host='localhost',
                                       database='sitedb')
        cursors = conn.cursor()
        cursors.execute(query, params)
        resualt = cursors.fetchall()
        return resualt

    @staticmethod
    def execute_1(query):
        conn = mysql.connector.connect(user='root', password='@27061378',
                                       host='localhost',
                                       database='sitedb')
        cursors = conn.cursor()
        cursors.execute(query)
        resualt = cursors.fetchall()
        return resualt
