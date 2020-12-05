import database
from routers import user, coupone, permission
from reposintory import sql, mysql

q1_coupones = ("SELECT coupon_name,user_coupon FROM Coupone")

q2_coupones = ("INSERT INTO Coupone (coupon_name,user_coupon) VALUES  (%s,%S)")

coupone_params = coupone.get_coupon
coupone_log = mysql.Database.query(database, q1_coupones)


def save_coupone():
    mysql.Database.query(database, q1_coupones, coupone.create_coupon)
