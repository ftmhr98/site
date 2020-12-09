import database
from routers import user, coupone, permission
from reposintory import sql, mysql1
from reposintory.sql.users import pass_user

q1_coupone = "INSERT INTO Coupone (coupon_name) VALUES (%s)"
q2_coupone = "INSERT INTO user_coupone(user_id , coupon_name) VALUES (%s,%s)"

database_obj = mysql1.Database


def save_coupone(name_coupone):
    database_obj.query(q1_coupone, name_coupone)


def save_user(coupone_in):
    database_obj.query(q2_coupone, coupone_in)


