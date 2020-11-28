from fastapi import FastAPI
import database


def get_user(users):
    if users == database.user:
        return users
    else:
        return "faild"


def check_per(userper):
    if userper == database.User_permission:
        return userper
    else:
        return "faild"
