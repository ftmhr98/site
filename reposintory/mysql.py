import database
import mysql.connector

cnx = mysql.connector.connect(user='root', password='@27061378',
                              host='localhost',
                              database='sitedb')
cursor = cnx.cursor()


def isfetch(query):
    result = query.fetchall()
    return result


q1_user = ("SELECT  id, name , pass FROM users")
isfetch(q1_user)
q1_permis = ("SELECT * FROM permis")
isfetch(q1_permis)
q1_usper = ("SELECT user_id,permission_id FROM User_permission")
isfetch(q1_usper)
q1_coupone = ("SELECT coupon_name,user_coupon FROM Coupone")
isfetch(q1_coupone)
q2_user = ("INSERT INTO users (name , pass , email) VALUES (%s , %s , %s)")
isfetch(q2_user)
q2_permis = ("INSERT INTO permis (permis VALUES (%s))")
isfetch(q2_permis)
q2_coupone = ("INSERT INTO Coupone (coupon_name) VALUSE (%s)")
isfetch(q2_coupone)
q2_usper = ("SELECT users.name AS user_id , permis.id AS permission_id FROM User_permission INNER JOIN  users,permis  ")
isfetch(q2_usper)
q3_coupone = ("SELECT users.id AS user_coupon FROM users INNER JOIN users")
isfetch(q3_coupone)
