from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn


class Coupon(BaseModel):
    name: str


tb_coupon = []

app = FastAPI()


@app.get("/coupone")
async def get_coupon():
    return tb_coupon


@app.post("/coupone")
async def create_coupon(coupon: Coupon):
    tb_coupon.append(coupon.dict())
    return tb_coupon


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
