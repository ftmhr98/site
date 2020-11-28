from fastapi import FastAPI
from pydantic import BaseModel, ValidationError, validator
import uvicorn


class permission(BaseModel):
    name: str


tb_per = []
app = FastAPI()


@app.get("/permis")
async def check_permission(permis: permission):
    tb_per.append(permis.dict())
    return permis


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
