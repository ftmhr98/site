from fastapi import FastAPI
import router

salt = "dsfdsfsdfvdsvdsv"


def get_hash(text):
    return str(hash(text + salt))
