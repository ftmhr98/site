from redis import Redis

r = Redis(host='localhost', port=6379, db=0, password='')


def token_set(payload):
    token = payload
    z = r.set("token", token)
    print(z)


def token_get():
    token = r.get("token")
    return token
