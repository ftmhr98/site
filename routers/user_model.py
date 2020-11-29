from fastapi import FastAPI
from pydantic import BaseModel, ValidationError, validator


class UserBase(BaseModel):
    name: str
    email: str


class UserIn(UserBase):
    password: str


class UserInDB(UserBase):
    hashed_password: str


class UserOut(UserBase):
    pass


app = FastAPI()
