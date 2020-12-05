import json
import jwt
import requests
from fastapi import FastAPI, requests

SECRET_KEY = "hkBxrbZ9Td4QEwgRewV6gZSVH4q78vBia4GBYuqd09SsiMsIjH"
app = FastAPI()


def token_required(function):
    def wrap():
        try:
            token_passed = requests.headers['TOKEN']
            if requests.headers['TOKEN'] != '' and requests.headers['TOKEN'] != None:
                try:
                    data = jwt.decode(token_passed, SECRET_KEY, algorithms=['HS256'])
                    return function()
                except jwt.exceptions.ExpiredSignatureError:
                    return_data = {
                        "error": "1",
                        "message": "Token has expired"
                    }
                    return app.response_class(response=json.dumps(return_data), mimetype='application/json')
                except:
                    return_data = {
                        "error": "1",
                        "message": "Invalid Token"
                    }
                    return app.response_class(response=json.dumps(return_data), mimetype='application/json')
            else:
                return_data = {
                    "error": "2",
                    "message": "Token required",
                }
                return app.response_class(response=json.dumps(return_data), mimetype='application/json')
        except Exception as e:
            return_data = {
                "error": "3",
                "message": "An error occured"
            }
            return app.response_class(response=json.dumps(return_data), mimetype='application/json')

    return wrap
