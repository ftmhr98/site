import database
from routers import user, coupone, permission, user_permission
from reposintory import sql, mysql

q1_user = ("SELECT  id, name , pass FROM users")
q2_user = ("INSERT INTO users (name , pass , email) VALUES (%s , %s , %s)")
user_param = user.log_users
user_log = sql.Database.query(database, q2_user)


def save_user():
    mysql.Database.query(database, q2_user, user.create_user)


def check_user(data):
    if (user_param == user_log):
        pass
