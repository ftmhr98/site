from fastapi import FastAPI
from routers import user_model
from helper import hash_tools as hash
import uvicorn

from helper.encode_decode import get_encode, get_decode, creat_token

from reposintory.rediss import token_set

from reposintory.sql import users

tb_user = []

app = FastAPI()
access_token_minutes = 30


def save(user_in: user_model.UserIn):
    hashed_password = hash.get_hash(user_in.password)
    user_in_db = user_model.UserInDB(**user_in.dict(), hashed_password=hashed_password)
    return user_in_db


@app.post("/users")
async def create_user(user_in: user_model.UserIn):
    hashed_password = hash.get_hash(user_in.password)
    tb_user = save(user_in)
    print(users.save_user(user_in.name, hashed_password))
    return tb_user


@app.post("/users_login")
async def log_in(user: user_model.UserIn):
    user_name = user.name
    password = user.password
    hashed_password = hash.get_hash(password)
    id_user = users.pass_user(user_name, hashed_password)
    token = creat_token(id_user)

    decode_token = token.decode("utf-8")

    token_set(decode_token)

    return decode_token


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
