from fastapi import FastAPI
from pydantic import BaseModel
import databases
import sqlalchemy
import uvicorn
from tortois import field

from tortois.models import Model
import requests


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

app=FastAPI()
@app.get("/users")
async def get_users():
    return tb_user
@app.post("/users")
async def create_user(user:User):
    tb_user.append(user.dict())
    return user
@app.get("/Permission")
async def get_permis():
    return tb_per

@app.post("/Permission")
async def create_permis(permis:Pers):

    return permis
    
@app.get("/Coupone")
async def get_coupon():
    return tb_coupon
app.post("/Coupone")
async def create_coupon(coupon:Coupon):
    return coupon

"""if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)"""