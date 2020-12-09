import mysql.connector


class Database:
    def __init__(self):
        self._conn = mysql.connector.connect(user='root', password='@27061378',
                                             host='localhost',
                                             database='sitedb')

        print(self._conn)

        self._cursor = self._conn.cursor()
        print(self._cursor)

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

        # fe = self.cursor.fetchall()
        #
        # print(params)
        # print(fe)
    @staticmethod
    def execute(query,params):
        conn = mysql.connector.connect(user='root', password='@27061378',
                                       host='localhost',
                                       database='sitedb')
        cursors = conn.cursor()
        cursors.execute(query, params)
        resualt=cursors.fetchall()
        return resualt


"""""
    def get_connection(self):
        if self.connection is None:
            self._conn = mysql.connect()
        else:
            mysql.connector.connect().close()
"""
