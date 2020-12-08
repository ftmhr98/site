import json
import jwt
import datetime
from fastapi import FastAPI, requests
import uvicorn
import datetime

secret_key = "hkBxrbZ9Td4QEwgRewV6gZSVH4q78vBia4GBYuqd09SsiMsIjH"
app = FastAPI()


def get_encode(payload):
    # timeLimit = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    # token = jwt.encode(payload, secret_key)
    encode_params = jwt.encode(payload, secret_key, algorithms='HS256')
    return encode_params


def get_decode(payload):
    decode_params = jwt.decode(get_encode(payload), secret_key, algorithms='HS256')
    return decode_params
