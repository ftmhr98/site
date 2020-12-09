from fastapi import FastAPI
from routers import user_model
from helper import hash_tools as hash
import uvicorn
from typing import Optional
from helper.encode_decode import get_encode, get_decode

from datetime import datetime, timedelta
import jwt
from reposintory.sql import users

tb_user = []

app = FastAPI()
access_token_minutes = 30


def save(user_in: user_model.UserIn):
    hashed_password = hash.get_hash(user_in.password)
    user_in_db = user_model.UserInDB(**user_in.dict(), hashed_password=hashed_password)
    return user_in_db


def creat_token(user_id, expires_delta: Optional[timedelta] = None):
    to_encode = {"user_id": user_id}

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encode_id = get_encode(to_encode)
    return encode_id


@app.post("/users")
async def create_user(user_in: user_model.UserIn):
    hashed_password = hash.get_hash(user_in.password)
    tb_user = save(user_in)
    print((user_in.name, hashed_password))
    users.save_user(user_in.name, hashed_password)
    return tb_user


@app.post("/users_login")
async def log_in(user: user_model.UserIn):
    user_name = user.name
    password = user.password
    hasshed_password = hash.get_hash(password)
    # creat_token(users.pass_user())
    return user_name, hasshed_password


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
