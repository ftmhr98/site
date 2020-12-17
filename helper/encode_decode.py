import json
import jwt
from datetime import datetime, timedelta
from fastapi import FastAPI, requests
from typing import Optional

secret_key = "hkBxrbZ9Td4QEwgRewV6gZSVH4q78vBia4GBYuqd09SsiMsIjH"
app = FastAPI()


def get_encode(payload):
    encode_params = jwt.encode(payload, secret_key, algorithm='HS256')
    return encode_params


def get_decode(payload):
    decode_params = jwt.decode(payload, secret_key, algorithm='HS256')

    return str(decode_params)


def get_id(payload):
    decode_params = jwt.decode(payload, secret_key, algorithm='HS256')

    user_id = decode_params.get("user_id")
    print(user_id)
    return user_id


def creat_token(user_id, expires_delta: Optional[timedelta] = None):
    to_encode = {"user_id": user_id}

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=20)
    to_encode.update({"exp": expire})
    encode_id = get_encode(to_encode)
    return encode_id
