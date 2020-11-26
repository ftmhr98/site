from fastapi import FastAPI
import router
import database
import hash_tools
import requests
def check_user():
    if router.Use is  database.user:
        return response.ok
    else:
        return response.status_code(200)

