from reposintory import  mysql1

q1_coupone = "INSERT INTO Coupone (coupon_name) VALUE (%s)"
q2_coupone = "INSERT INTO user_coupone(user_id, coupon_name) VALUES (%s,%s)"
q3_user_coupone = "SELECT * FROM user_coupone "
q4_coupone="SELECT * FROM Coupone"
database_obj = mysql1.Database


def save_coupone(name_coupone):
    database_obj.query_2(q1_coupone, name_coupone)


def save_user(id_user, name_coupon):
    database_obj.query(q2_coupone, (id_user, name_coupon))


