import database
from routers import user, coupone, permission
from reposintory import sql, mysql1
from reposintory.sql.users import pass_user

q1_coupones = ("INSERT INTO Coupone (coupon_name) VALUES  (%s)")
q2_coupones = ("INSERT INTO user_coupone(coupon_id,user_id)VALUES (%s,%s)")

coupone_params = coupone.tb_coupon


# = pass_user()


def save_coupone():
    mysql1.Database.query(q1_coupones, coupone.create_coupon, coupone_params)


def save_user(user_id):
    mysql1.Database.query(database, q2_coupones, (user_id, coupone.create_usercoupone))
