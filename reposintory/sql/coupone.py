import database
from routers import user, coupone, permission
from reposintory import sql, mysql1
from reposintory.sql.users import pass_user

q1_coupones = "INSERT INTO Coupone (coupon_name) VALUES  (%s)"
q2_coupones = "INSERT INTO user_coupone(coupon_id,user_id)VALUES (%s,%s)"

coupone_params = coupone.tb_coupon

database_obj=mysql1.Database




def save_coupone(name_coupone):
    database_obj.query(q1_coupones, name_coupone)


def save_user(user_id,coupone_id):
    database_obj.query(q2_coupones, (user_id,coupone_id))
