import database
import mysql.connector

cnx = mysql.connector.connect(user='root', password='@27061378',
                              host='localhost',
                              database='sitedb')
cursor = cnx.cursor()

"""""
def execute(query):
    result = query.fetchall()
    return result
"""


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

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()

    def get_connection(self):
        if self.connection == None:
            self._conn = mysql.connect(cnx)
        else:
            mysql.connector.connect().close()


q1_user = ("SELECT  id, name , pass FROM users")

q1_permission = ("SELECT * FROM Permission")

q1_user_permission = ("SELECT user_id,permission_id FROM User_permission")

q1_coupones = ("SELECT coupon_name,user_coupon FROM Coupone")

q2_user = ("INSERT INTO users (name , pass , email) VALUES (%s , %s , %s)")

q2_coupones = ("INSERT INTO Coupone (coupon_name) VALUSE (%s)")

q2_user_permission = ("INSERT INTO User_permission (user_id,permission_id) VALUES  (%s,%s)")

q3_coupones = ("INSERT INTO Coupone (coupon_name,user_coupon) VALUES  (%s,%S)")

Database.fetchall()
Database.close()
