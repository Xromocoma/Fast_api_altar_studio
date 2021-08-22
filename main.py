import json

from fastapi import FastAPI, status
from app.core.user import get_all_users, get_user, update_user, delete_user, user_login, create_user, user_logout
from starlette import requests, responses
from app.shemas import UserLogin, UserData, UserUpdate, UserLogout

app = FastAPI()


@app.get("/")
async def example():
    return 'OK'


@app.get("/users")
async def get_users():
    return get_all_users()


@app.get("/users/<user_id>")
async def get_user_by_id(user_id: int):
    return get_user(user_id)


@app.put("/users/<user_id>")
async def user_update(user_id: int, user_data: UserUpdate):
    if update_user(user_id, user_data.dict()):
        return responses.Response(status_code=status.HTTP_200_OK)
    return responses.Response(status_code=status.HTTP_404_NOT_FOUND)


@app.delete("/users/<user_id>")
async def user_del(user_id: int):
    return delete_user(user_id)


@app.post("/users/create")
async def user_create(user_data: UserData):
    if user_create(user_data):
        return responses.Response(status_code=status.HTTP_200_OK)
    return responses.Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@app.post("/login")
async def login(user: UserLogin):
    login_ok = user_login(user)
    if login_ok:
        res = responses.Response(status_code=status.HTTP_200_OK)
        res.set_cookie('Access_token', login_ok['access_token'], samesite='strict', max_age=60 * 60 * 3)
        res.set_cookie('role', login_ok['is_admin'], samesite='strict', max_age=60 * 60 * 3)
        return responses
    return responses.Response(status_code=status.HTTP_404_NOT_FOUND)


@app.post("/logout")
async def logout(user: UserLogout):
    logout = user_logout(user)
    if logout:
        res = responses.Response(status_code=status.HTTP_200_OK)
        res.set_cookie('Access_token', "", samesite='strict', max_age=0)
        res.set_cookie('role', "", samesite='strict', max_age=0)
        return responses
    return responses.Response(status_code=status.HTTP_404_NOT_FOUND)
