from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn


class permission(BaseModel):
    permis: str


tb_per = []
app = FastAPI()


@app.get("/permiss/")
async def check_permission():
    return tb_per


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
