from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
import uvicorn
from helper.encode_decode import get_id
from reposintory import rediss
from reposintory.sql import permission
from helper.convert import convert_list, convert_int
from starlette.requests import Request


class Permissions(BaseModel):
    user_id: int
    permission_id: int


tb_per = {"user_id": 0,
          "id_permission": 0}
app = FastAPI()


@app.post("/permiss")
async def check_permissions(request: Request):
    token: str = request.headers.get('Authorization')
    token = token.replace("Bearer", "")
    token = token[1:]
    if rediss.token_get() == token:

        id_user = get_id(token)
        print(id_user)
        x = convert_list(id_user)
        print(x)
        user_id = convert_int(x)
        if permission.is_admin(user_id):
            return "ADMIN"
        else:
            return "NORMAL"

    else:
        raise HTTPException(status_code=408, detail="Request Timeout")


@app.post("/permissions")
async def creat_permission(permissions: Permissions, request: Request):
    token: str = request.headers.get('Authorization')
    token = token.replace("Bearer", "")
    token = token[1:]
    try:
        if rediss.token_get() == token:
            id_user = get_id(token)
            x = convert_list(id_user)
            user_id = convert_int(x)
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
