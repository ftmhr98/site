import database
from routers import user, coupone, permission, user_permission
from reposintory import sql, mysql1

q1_user = ("SELECT  id, name , pass FROM users")
q2_user = ("INSERT INTO users (name , pass , email) VALUES (%s , %s , %s)")
q3_user = ("SELECT  id FROM users WHERE name = %S")
user_param = user.log_users
user_log = mysql1.Database.query(database, q2_user)


def save_user():
    mysql1.Database.query(database, q2_user, user.create_user)


def pass_user(id_user):
    id_user = mysql1.Database.execute(database, q3_user)
    return id_user


"""""
def check_user(data):
    if (user_param == user_log):
        pass
"""
