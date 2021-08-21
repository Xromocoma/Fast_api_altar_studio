from fastapi import FastAPI, status
from app.core.user import get_all_users, user_login
from starlette import requests, responses
from app.models import Login, User

my_app = FastAPI()


@my_app.get("/")
async def example():
    return get_all_users()

@my_app.get("/test")
async def example():
    return responses.JSONResponse(status_code=200, content={"is": "ok"})



@my_app.post("/login")
async def login(login_data: Login):
    res = await user_login(login_data)
    if res:
        return responses.JSONResponse(status_code=status.HTTP_200_OK)
    return responses.Response(status_code=status.HTTP_401_UNAUTHORIZED)
