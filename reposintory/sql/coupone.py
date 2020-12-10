from reposintory import sql, mysql1

q1_coupone = "INSERT INTO Coupone (coupon_name) VALUE (%s)"
q2_coupone = "INSERT INTO user_coupone(user_id , coupon_name) VALUES (%s,%s)"

database_obj = mysql1.Database


def save_coupone(name_coupone):
    database_obj.query_2(q1_coupone, name_coupone)


def save_user(id_user, name_coupon):
    database_obj.query(q2_coupone, (id_user, name_coupon))


date = {"name": "snap45", "user_id": 1}
id = date.get("user_id")
print(id)
name = date.get("name")
print(name)
save_user(id,name)
