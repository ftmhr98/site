from fastapi import FastAPI, HTTPException
import uvicorn
from reposintory.sql import coupone, permission
from routers import coupon_model
from reposintory import rediss
from helper.encode_decode import get_id
from pydantic import BaseModel


class Coupon(BaseModel):
    name: str


class User_coupone(BaseModel):
    name: str
    user_id: int


tb_coupon = {"name": "value"}

tb_user_coupon = {"name": "value",
                  "user_id": 0}
app = FastAPI()


@app.post("/coupon")
async def create_coupon(coupon: coupon_model.Coupon, token):
    print(rediss.token_get())
    print(token)
    print(rediss.token_get() is token)

    if rediss.token_get() == token:
        print("hi")
        id_user = get_id(token)
        print(id_user)
        if permission.is_admin(id_user):
            tb_coupon["name"] = coupon.name
            coupone.save_coupone(tb_coupon.get("name"))
            print(tb_coupon)
        else:
            raise HTTPException(status_code=403, detail="Forbidden")
    return tb_coupon


@app.post("/user_coupon")
async def create_user_coupon(user_coupon: User_coupone, token):
    if rediss.token_get() == token:
        id_user = get_id(token)
        print(id_user)
        if permission.is_admin(id_user) is False:
            tb_user_coupon["name"] = user_coupon.name
            tb_user_coupon["user_id"] = user_coupon.user_id
            print(tb_user_coupon)
            coupone.save_user(tb_user_coupon.get("user_id"), tb_user_coupon.get("name"))
            print(tb_user_coupon)

        else:
            raise HTTPException(status_code=403, detail="Forbidden")
        return tb_user_coupon


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
