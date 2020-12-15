from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from helper.encode_decode import get_id
from reposintory import rediss
from reposintory.sql import permission


class Permissions(BaseModel):
    user_id: int
    permission_id: int


tb_per = {"user_id": 0,
          "id_permission": 0}
app = FastAPI()


@app.post("/permiss")
async def check_permissions(token):
    if rediss.token_get() == token:

        id_user = get_id(token)
        x = permission.convert_list(id_user)
        user_id = permission.convert_int(x)
        if permission.is_admin(user_id):
            return "ADMIN"
        else:
            return "NORMAL"

    else:
        raise HTTPException(status_code=408, detail="Request Timeout")


@app.post("/permissions")
async def creat_permission(permissions: Permissions, token):
    try:
        if rediss.token_get() == token:
            id_user = get_id(token)
            x = permission.convert_list(id_user)
            user_id = permission.convert_int(x)
            if permission.is_admin(user_id):
                tb_per["user_id"] = permissions.user_id
                tb_per["id_permission"] = permissions.permission_id
                permission.save_permission(tb_per.get("user_id"), tb_per.get("id_permission"))
                return tb_per
            else:
                raise HTTPException(status_code=403, detail="Forbidden")
    except:
        raise HTTPException(status_code=401, detail="Unauthorized")


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
