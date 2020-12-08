import database
from routers import user, coupone, permission
from reposintory import sql, mysql1

q1_coupones = ("INSERT INTO Coupone (coupon_name) VALUES  (%s)")
q2_coupones = ("INSERT INTO user_coupone(coupon_id,user_id)VALUES (%s,%s)")
q3_copones = ("SELECT ")
coupone_params = coupone.get_coupon
# coupone_log = mysql1.Database.query(q1_coupones)
user_id = sql.users.pass_user()


def save_coupone():
    mysql1.Database.query(q1_coupones, coupone.create_coupon, )


def save_user():
    mysql1.Database.query(database, q2_coupones, (user_id, coupone.create_usercoupone))
