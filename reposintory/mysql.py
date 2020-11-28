import database
import mysql.connector

cnx = mysql.connector.connect(user='root', password='@27061378',
                              host='localhost',
                              database='sitedb')
cursor = cnx.cursor()


def execute(query):
    result = query.fetchall()
    return result


q1_user = ("SELECT  id, name , pass FROM users")
execute(q1_user)

q1_permis = ("SELECT * FROM Permission")
execute(q1_permis)

q1_usper = ("SELECT user_id,permission_id FROM User_permission")
execute(q1_usper)

q1_coupone = ("SELECT coupon_name,user_coupon FROM Coupone")
execute(q1_coupone)

q2_user = ("INSERT INTO users (name , pass , email) VALUES (%s , %s , %s)")

execute(q2_user)

q2_permis = ("INSERT INTO Permission (permis )VALUES (%s)")
execute(q2_permis)

q2_coupone = ("INSERT INTO Coupone (coupon_name) VALUSE (%s)")
execute(q2_coupone)

q2_usper = ("INSERT INTO User_permission (user_id,permission_id) VALUES  (%s,%s)")
execute(q2_usper)

q3_coupone = ("INSERT INTO Coupone (coupon_name,user_coupon) VALUES  (%s,%S)")
execute(q3_coupone)
