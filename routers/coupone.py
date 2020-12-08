from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn


class Coupon(BaseModel):
    name: str


class User_coupone(BaseModel):
    # user_id: int
    coupone_id: int


tb_coupon = []
tb_usercoupone = []
app = FastAPI()


@app.get("/coupone")
async def get_coupon():
    return tb_coupon


@app.post("/coupone")
async def create_coupon(coupon: Coupon):
    tb_coupon.append(coupon.dict())
    return tb_coupon


@app.post("/user_coupone")
async def create_usercoupone(user_coupone: User_coupone):
    tb_usercoupone.append(user_coupone.dict())
    return tb_usercoupone


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
