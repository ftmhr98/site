from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from reposintory.sql import permission


class Permissions(BaseModel):
    user_id: int
    permission_id: int


tb_per = {"user_id": 0,
          "id_permission": 0}
app = FastAPI()


@app.get("/permiss")
async def check_permission():
    return tb_per


@app.post("/permiss")
async def creat_permission(permiss: Permissions):
    tb_per["user_id"] = (permiss.user_id)
    tb_per["id_permission"] = (permiss.permission_id)
    print(tb_per.get("user_id"))
    print(tb_per.get("id_permission"))
    permission.save_permission(tb_per.get("user_id"), tb_per.get("id_permission"))
    return tb_per


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
