from fastapi import FastAPI
import uvicorn
from routers.user import create_user
from reposintory.sql.users import save_user
app = FastAPI()
#save_user(create_user)
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
