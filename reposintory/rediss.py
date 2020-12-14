from redis import Redis
from datetime import datetime, timedelta
import response

r = Redis(host='localhost', port=6379, db=0, password='')


def token_set(payload):
    token = payload
    z = r.set("token", token)
    print(z)


def token_get():
    if (r.exists("token")):
        token = r.get("token")
        print(token)
        return token
    else:
        raise Exception("YOUR ACCESS DENIED")
