from fastapi import FastAPI
from pydantic import BaseModel
import databases
import sqlalchemy


app=FastAPI()
tb_user=[]
tb_coupon=[]
tb_per=[]

class User(BaseModel):
    name=str
    pas=str
class Coupon(BaseModel):
    name=str
class Pers(BaseModel):
    permis=str

@app.get("/users")
def get_users():
    return tb_user
@app.post("/users")
def create_user(user:User):
    return user
@app.get("/Permission")
def get_permis():
    return tb_per

@app.post("/Permission")
def create_permis(permis:Pers):
    return permis
    
@app.get("/Coupone")
def get_coupon():
    return tb_coupon
app.post("/Coupone")
def create_coupon(coupon:Coupon):
    return coupon
