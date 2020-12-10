import redis
from routers import user
redis_host = "localhost"
redis_port = 6379
redis_password = ""
redis_connect = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password)
def token_set(payload):
    pass

