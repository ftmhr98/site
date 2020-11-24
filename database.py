import mysql.connector
db=mysql.connector.connect(
  host="localhost",
  user="root",
  password="@27061378",
  database= "sitedb"
)
mycursor = db.cursor()
user = [
('ftm','@1234567890','exam@char.com'),
('mhm','@mhm1254','trt@gm.com'),
('zhra','zhr091','utr@ya.com')
]
pers = [
  ("add coupon",),
  ("add user",),
  ("use coupon",)
]
mycursor=db.cursor()
"""CREATE TABLE
mycursor.execute("CREATE TABLE users(id INT AUTO_INCREMENT PRIMARY KEY ,name VARCHAR(255),pass VARCHAR(255),email VARCHAR(255))")
mycursor.execute("CREATE TABLE Permission(id int PRIMARY KEY AUTO_INCREMENT,permis VARCHAR(255))")
mycursor.execute("CREATE TABLE User_permission(id INT AUTO_INCREMENT PRIMARY KEY ,user_id INT NOT NULL, permission_id INT NOT NULL)")
mycursor.execute("CREATE TABLE Coupone(id INT AUTO_INCREMENT PRIMARY KEY,coupon_name VARCHAR(255) NOT NULL,user_coupon int NOT NULL)")
"""
"""
Q1 ="INSERT INTO users (name , pass , email) VALUES (%s , %s , %s) "
Q2 ="INSERT INTO Permission (permis) VALUES (%s)"
"""



