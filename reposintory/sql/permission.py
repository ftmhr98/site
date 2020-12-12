import database
from routers import user, coupone, permission, user_permission
from reposintory import mysql1
from reposintory.sql.users import save_user, pass_user
from reposintory.sql import coupone

q1_user_permission = "SELECT * FROM User_permission"

q2_user_permission = "INSERT INTO User_permission (user_id,permission_id) VALUES  (%s,%s)"
q3_user_permission = "SELECT permission_id FROM User_permission WHERE user_id = %s"
permission_params = user_permission.check_user_permission

tb_access = []
database_objct = mysql1.Database


def save_permission(id_user, id_permission):
    database_objct.query_2(q2_user_permission, (id_user, id_permission))


def is_admin(user_id):
    permission_id = database_objct.execute(q3_user_permission, user_id)
    if permission_id == 1:
        return True
    else:
        return False
