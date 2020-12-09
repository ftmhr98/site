from reposintory import mysql1
import mysql.connector

q1_user = "SELECT  id, name , pass FROM users"
q2_user = "INSERT INTO users (name , pass) VALUES (%s,%s)"
q3_user = "SELECT  id FROM users WHERE name = %s and pass = %s"

database_object = mysql1.Database()


def save_user(name_user,user_password):
    database_object.query(q2_user, (name_user,user_password))


def pass_user(user_in, pass_in):
    resault = database_object.execute(q3_user, (user_in, pass_in))
    return resault

