import json
import jwt

from fastapi import FastAPI, requests

secret_key = "hkBxrbZ9Td4QEwgRewV6gZSVH4q78vBia4GBYuqd09SsiMsIjH"
app = FastAPI()


def get_encode(payload):
    encode_params = jwt.encode(payload, secret_key, algorithm='HS256')
    return encode_params


def get_decode(payload):
    decode_params = jwt.decode(payload, secret_key, algorithm='HS256')
    return decode_params


def get_id(payload):
    decode_params = jwt.decode(payload, secret_key, algorithm='HS256')

    user_id = decode_params.get("user_id")
    print(user_id)
    return user_id
