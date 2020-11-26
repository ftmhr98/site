from fastapi import FastAPI
import router
def get_hash(str):
    pas_hashed=str(hash(router.pas))
    return pas_hashed