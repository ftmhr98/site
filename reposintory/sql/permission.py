import database
from routers import user, coupone, permission, user_permission
from reposintory import sql, mysql
from reposintory.sql import coupone,users
# q1_permission = ("SELECT * FROM Permission")
q1_user_permission = ("SELECT user_id,permission_id FROM User_permission")

q2_user_permission = ("INSERT INTO User_permission (user_id,permission_id) VALUES  (%s,%s)")
q3_user_permission = ("SELECT user_id,permission_id FROM User_permission WHERE user_id = %s")
permission_params = user_permission.check_userpermission
# permission_log = mysql.Database.query(database, q2_user_permission)
tb_access = []


def save_permission():
    mysql.Database.query(database, q2_user_permission, user_permission.creat_user_permission)
    mysql.Database.close(database)


def check_permission(user_id, permission_id):
    try:
        mysql.Database.query(database, q3_user_permission, user_permission.check_user_permission)
    except PermissionError:
        print("YOU DONT HAVE PERMISSION FOR ANY THING")
        if(permission_id == 1):
            sql.coupone.save_coupone()
        elif (permission_id == 2):
            sql.users.save_user()
        elif(permission_id == 3):

            pass


