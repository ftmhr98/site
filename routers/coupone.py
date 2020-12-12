from fastapi import FastAPI, HTTPException

import uvicorn
from reposintory.sql import coupone
from routers import coupon_model
from reposintory import rediss
from helper.encode_decode import get_id

tb_coupon = {"name": "value"}
tb_usercoupone = {"name": "value",
                  "user_id": 0}
app = FastAPI()


@app.post("/coupone")
async def create_coupon(coupon: coupon_model.Coupon, token):
    if rediss.token_get() == token:
        tb_coupon["name"] = (coupon.name)
        coupone.save_coupone(tb_coupon.get("name"))
    else:
        raise HTTPException(status_code=403, detail="Forbidden")
    return tb_coupon


@app.post("/user_coupone")
async def create_usercoupone(user_coupone: coupon_model.User_coupone, token):
    if rediss.token_get() == token:
        tb_usercoupone["name"] = (user_coupone.name)
        tb_usercoupone["user_id"] = (user_coupone.user_id)
        id_user = get_id(token)
        coupone.save_user(id_user, tb_usercoupone.get("name"))
    else:
        raise HTTPException(status_code=403, detail="Forbidden")
    return tb_usercoupone


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
