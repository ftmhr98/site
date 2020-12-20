from redis import Redis
from datetime import datetime, timedelta
import response

r = Redis(host='localhost', port=6379, db=0, password='')


def token_set(payload):
    token = payload
    z = r.set("token", token)
    print(z)
    return z


def token_get():
    if (r.exists("token")):
        u = r.get("token")
        token = u.decode("utf-8")

        return token
    else:
        raise Exception("YOUR ACCESS DENIED")
