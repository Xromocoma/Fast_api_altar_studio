import json

from fastapi import FastAPI, status
from app.core.user import get_all_users, get_user,update_user, delete_user
from starlette import requests, responses
from app.shemas import Login, UserInfo

app = FastAPI()


@app.get("/")
async def example():
    return 'OK'


@app.get("/users")
async def get_users():

    return get_all_users()

@app.get("/user/<user_id>")
async def get_user_by_id(user_id: int):
    return get_user(user_id)

@app.post("/user/update")
async def update_user_data(user_data: UserInfo):
    return update_user(user_data)

@app.delete("/user/<user_id>")
async def user_del(user_id: int):
    return delete_user(user_id)
