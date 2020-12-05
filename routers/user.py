from fastapi import FastAPI
from pydantic import BaseModel, ValidationError, validator
from routers import user_model
from helper import hash_tools as hash
import uvicorn
import database
import requests

tb_user = []

app = FastAPI()


def save_user(user_in: user_model.UserIn):
    hashed_password = hash.get_hash(user_in.password)
    user_in_db = user_model.UserInDB(**user_in.dict(), hashed_password=hashed_password)
    return user_in_db
@app.get("/users")
async def log_users():
    return tb_user

@app.post("/users")
async def create_user(user_in: user_model.UserIn):
    hashed_password = hash.get_hash(user_in.password)
    tb_user = save_user(user_in)
    return tb_user





if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)