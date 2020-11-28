from fastapi import FastAPI
from pydantic import BaseModel, ValidationError, validator

import uvicorn
import requests

tb_user = []




class User(BaseModel):
    name: str
    pas: str



app = FastAPI()


@app.get("/users")
async def log_users():
    return tb_user


@app.post("/users")
async def create_user(user: User):
    tb_user.append(user.dict())
    return user







if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
