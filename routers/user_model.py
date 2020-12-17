from fastapi import FastAPI
from pydantic import BaseModel


class UserBase(BaseModel):
    name: str


class UserIn(UserBase):
    password: str


class UserInDB(UserBase):
    hashed_password: str


app = FastAPI()
