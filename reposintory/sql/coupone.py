import database
from routers import user, coupone, permission
from reposintory import sql, mysql

q1_coupones = ("SELECT coupon_name,user_coupon FROM Coupone")

q2_coupones = ("INSERT INTO Coupone (coupon_name) VALUES  (%s)")
q3_coupones =("UPDATE  Coupone SET user_coupone = %S WHERE coupon_name = %S")

coupone_params = coupone.get_coupon
coupone_log = mysql.Database.query(database, q1_coupones)


def save_coupone():
    mysql.Database.query(database, q2_coupones, coupone.create_coupon)
def save_user():
    mysql.Database.query(database,q3_coupones,)