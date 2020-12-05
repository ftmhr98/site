import database
from routers import user, coupone, permission
from reposintory import mysql

user_param = user.log_users
user_log = mysql.Database.query(database, mysql.Database)
permission_params = permission.check_permission
permission_log = mysql.Database.query(database, mysql.q1_permission)


def save_user():
    mysql.Database.query(database, mysql.q2_user, user.create_user)


def check_user(data):
    if (user_param == user_log):
        pass
