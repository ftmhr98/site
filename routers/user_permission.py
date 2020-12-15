from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn


class user_permission(BaseModel):
    user_id: int
    permission_id: int


tb_userpermission = []
app = FastAPI()


@app.get("/user_permiss")
async def check_user_permission():
    return tb_userpermission


@app.post("/user_permiss")
async def creat_user_permission(user_permission: user_permission):
    tb_userpermission.append(user_permission.dict())
    return tb_userpermission


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
