from routers import user, coupone, permission
from reposintory import mysql1
from helper.convert import convert_int
q1_user_permission = "SELECT * FROM User_permission"

q2_user_permission = "INSERT INTO User_permission (user_id,permission_id) VALUES  (%s,%s)"
q3_user_permission = "SELECT permission_id FROM User_permission WHERE user_id = %s"

tb_access = []
database_objct = mysql1.Database


def save_permission(id_user, id_permission):
    database_objct.query(q2_user_permission, (id_user, id_permission))


def is_admin(user_id):
    permission_id = database_objct.execute(q3_user_permission, user_id)
    print(permission_id)
    id_user = convert_int(permission_id[0])
    if id_user == 1:
        print(id_user)
        return True
    else:
        print(id_user)
        return False



