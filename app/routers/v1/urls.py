from app.core.user import get_all_users, get_user, update_user, delete_user, user_login, create_user, user_logout
from app.core.data_source import collect_data
from app.shemas import UserLogin, UserCreate, UserUpdate, UserInfo
from typing import List
from app.core.dependencies import is_authentication, security, is_admin
from fastapi import status, Response, Depends, Security, APIRouter
from fastapi.security import HTTPAuthorizationCredentials


router = APIRouter()

# Получение списка всех юзеров по UID
@router.get("/users",
            response_model=List[UserInfo],
            dependencies=[Depends(is_authentication), Security(security)])
def get_users():
    return get_all_users()


# Получение юзера по UID
@router.get("/users/{user_id}",
            response_model=UserInfo,
            dependencies=[Depends(is_authentication), Security(security)])
def get_user_by_id(user_id: int):

    return get_user(user_id)

# Обновление юзера по UID, поля динамические
@router.put("/users/{user_id}",
            dependencies=[Depends(is_authentication), Depends(is_admin), Security(security)])
def user_update(user_id: int, user_data: UserUpdate):
    if update_user(user_id, user_data.dict()):
        return Response(status_code=status.HTTP_200_OK)
    return Response(status_code=status.HTTP_404_NOT_FOUND)

# Удаление юзера по UID
@router.delete("/users/{user_id}",
               dependencies=[Depends(is_authentication), Depends(is_admin), Security(security)])
def user_del(user_id: int):
    if delete_user(user_id):
        return Response(status_code=status.HTTP_200_OK)

# Добавление юзера
@router.post("/users/create",
             dependencies=[Depends(is_authentication), Depends(is_admin), Security(security)])
async def user_create(user_data: UserCreate):
    if create_user(user_data):
        return Response(status_code=status.HTTP_200_OK)

# Вход и получение токена авторизации
@router.post("/login",)
def login(user: UserLogin):
    login_ok = user_login(user)
    if not login_ok:
        return Response(status_code=status.HTTP_401_UNAUTHORIZED)
    return Response(login_ok, status_code=status.HTTP_200_OK)

# Выход и отчистка токена
@router.post("/logout",
             dependencies=[Depends(is_authentication)])
def logout(credentials: HTTPAuthorizationCredentials = Security(security)):
    user_logout(credentials.credentials)
    return Response(status_code=status.HTTP_200_OK)

# Асинхронный запрос к 3 источникам (Задание 2)
@router.get("/data_source",
            dependencies=[Depends(is_authentication)])
async def get_data_source():
    return await collect_data()
