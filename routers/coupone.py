from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from reposintory.sql import coupone
from routers import coupon_model

tb_coupon = {"name": "value"}
tb_usercoupone = {"name": "value",
                  "user_id": 0}
app = FastAPI()


@app.post("/coupone")
async def create_coupon(coupon: coupon_model.Coupon):
    tb_coupon["name"] = (coupon.name)
    print(tb_coupon)
    print(tb_coupon.get("name"))
    coupone.save_coupone(tb_coupon.get("name"))
    return tb_coupon


@app.post("/user_coupone")
async def create_usercoupone(user_coupone: coupon_model.User_coupone):
    tb_usercoupone["name"] = (user_coupone.name)
    tb_usercoupone["user_id"] = (user_coupone.user_id)
    couppon_name = (tb_usercoupone.get("name"))

    user_id = (tb_usercoupone.get("user_id"))

    coupone.save_user(tb_usercoupone.get("user_id"), tb_usercoupone.get("name"))
    return tb_usercoupone


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
