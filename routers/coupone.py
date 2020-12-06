from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn


class Coupon(BaseModel):
    name: str


class user_coupone(Coupon):
    user_id: int


tb_coupon = []

app = FastAPI()


@app.get("/coupone")
async def get_coupon():
    return tb_coupon


@app.post("/coupone")
async def create_coupon(coupon: Coupon):
    tb_coupon.append(coupon.dict())
    return tb_coupon


@app.put("/coupone")
async def add_user(user: user_coupone):
    pass


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
