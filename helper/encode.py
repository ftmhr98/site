import json
import jwt
import datetime
from helper import decode
from fastapi import FastAPI, requests
import uvicorn

SECRET_KEY = "hkBxrbZ9Td4QEwgRewV6gZSVH4q78vBia4GBYuqd09SsiMsIjH"

app = FastAPI()


@app.post('/loginEndpoint')
def loginFunction():
    username = requests.form.get('name')
    password = requests.form.get('password')

    timeLimit = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)  # set limit for user
    payload = {"user_id": username, "exp": timeLimit}
    token = jwt.encode(payload, decode.SECRET_KEY)
    return_data = {
        "error": "0",
        "message": "Successful",
        "token": token.decode("UTF-8"),
        "Elapse_time": f"{timeLimit}"
    }
    return app.response_class(response=json.dumps(return_data), mimetype='application/json')


@app.post('/anEndpoint')
@decode.token_required  # Verify token decorator
def aWebService():
    return_data = {
        "error": "0",
        "message": "You Are verified"
    }
    return app.response_class(response=json.dumps(return_data), mimetype='application/json')


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
