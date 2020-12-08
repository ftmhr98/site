import database
from routers import user, coupone, permission, user_permission
from reposintory import mysql1
from reposintory.sql import coupone, users

# q1_permission = ("SELECT * FROM Permission")
q1_user_permission = ("SELECT user_id,permission_id FROM User_permission")

q2_user_permission = ("INSERT INTO User_permission (user_id,permission_id) VALUES  (%s,%s)")
q3_user_permission = ("SELECT permission_id FROM User_permission WHERE user_id = %s")
permission_params = user_permission.check_userpermission
# permission_log = mysql.Database.query(database, q2_user_permission)
tb_access = []


def save_permission():
    mysql1.Database.query(database, q2_user_permission, user_permission.creat_user_permission)
    mysql1.Database.close(database)


def check_permission(user_id):
    try:
        permission_id = mysql1.Database.query(database, q3_user_permission, users.pass_user(user_id))
    except PermissionError:
        print("YOU DONT HAVE PERMISSION FOR ANY THING")

        if (permission_id == 1):
            coupone.save_coupone()
        elif (permission_id == 2):
            users.save_user()
            coupone.save_user()
