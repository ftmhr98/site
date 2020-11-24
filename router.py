from fastapi import FastAPI
from pydantic import BaseModel
import databases
import sqlalchemy


app=FastAPI()
db=[]
class User (BaseModel):
    name=str
    pass=str


@app.get("/users")
def get_users:
    return db;
@app.post("/users"):
def create_user(user:User):
    return user;

