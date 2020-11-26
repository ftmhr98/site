from fastapi import FastAPI
from pydantic import BaseModel, ValidationError, validator

import uvicorn
import requests

tb_user = []
tb_coupon = []
tb_per = []


class User(BaseModel):
    name: str
    pas: str


class Coupon(BaseModel):
    name: str


class Pers(BaseModel):
    permis: str


app = FastAPI()


@app.get("/users")
async def log_users():
    return tb_user


@app.post("/users")
async def create_user(user: User):
    tb_user.append(user.dict())
    return user




@app.get("/coupone")
async def get_coupon():
    return tb_coupon


@app.post("/coupone")
async def create_coupon(coupon: Coupon):
    tb_coupon.append(coupon.dict())
    return coupon


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
