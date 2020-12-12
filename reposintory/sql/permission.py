import database
from routers import user, coupone, permission, user_permission
from reposintory import mysql1
from reposintory.sql.users import save_user, pass_user
from reposintory.sql import coupone

q1_user_permission = "SELECT user_id,permission_id FROM User_permission"

q2_user_permission = "INSERT INTO User_permission (user_id,permission_id) VALUES  (%s,%s)"
q3_user_permission = "SELECT permission_id FROM User_permission WHERE user_id = %s"
permission_params = user_permission.check_user_permission

tb_access = []
database_objct = mysql1.Database


def save_permission(id_user, id_permission):
    database_objct.query_2(q2_user_permission, (id_user, id_permission))


def check_permission(user_id):
    try:
        permission_id = database_objct.execute(q3_user_permission, user_id)
    except PermissionError:
        print("YOU DONT HAVE PERMISSION FOR ANY THING")
        if (permission_id == 1):
            coupone.save_coupone()
        elif (permission_id == 2):
            save_user()
            coupone.save_user(user_id)
