import database
from routers import user, coupone, permission, user_permission
from reposintory import sql, mysql

# q1_permission = ("SELECT * FROM Permission")
q1_user_permission = ("SELECT user_id,permission_id FROM User_permission")
q2_user_permission = ("INSERT INTO User_permission (user_id,permission_id) VALUES  (%s,%s)")
permission_params = user_permission.check_userpermission
permission_log = sql.Database.query(database, q2_user_permission)


def save_permission():
    mysql.Database.query(database, sql.permission.q2_user_permission, user_permission.creat_userpermission)
