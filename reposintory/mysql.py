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

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def fetchall(self):
        return self.cursor.fetchall()

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()


q1_user = ("SELECT  id, name , pass FROM users")
Database.execute(q1_user)

q1_permission = ("SELECT * FROM Permission")
Database.execute(q1_permission)

q1_user_permission = ("SELECT user_id,permission_id FROM User_permission")
Database.execute(q1_user_permission)

q1_coupones = ("SELECT coupon_name,user_coupon FROM Coupone")
Database.execute(q1_coupones)

q2_user = ("INSERT INTO users (name , pass , email) VALUES (%s , %s , %s)")

Database.execute(q2_user)

q2_permission = ("INSERT INTO Permission (permis )VALUES (%s)")
Database.execute(q2_permission)

q2_coupones = ("INSERT INTO Coupone (coupon_name) VALUSE (%s)")
Database.execute(q2_coupones)

q2_user_permission = ("INSERT INTO User_permission (user_id,permission_id) VALUES  (%s,%s)")
Database.execute(q2_user_permission)

q3_coupones = ("INSERT INTO Coupone (coupon_name,user_coupon) VALUES  (%s,%S)")
Database.execute(q3_coupones)

Database.fetchall()
