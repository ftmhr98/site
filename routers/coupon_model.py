from fastapi import FastAPI
from pydantic import BaseModel
class Coupon(BaseModel):
    name: str


class User_coupone(Coupon):
    user_id: int
