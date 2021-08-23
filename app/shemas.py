from pydantic import BaseModel, EmailStr
from typing import Union


class UserLogin(BaseModel):
    email: EmailStr
    passwd: str


class UserData(BaseModel):
    email: EmailStr
    name: str
    state: bool = True
    is_admin: bool = False

    class Config:
        orm_mode = True


class UserCreate(UserData):
    passwd: str


class UserInfo(UserData):
    id: int


class UserFullData(UserInfo):
    passwd: str


class UserUpdate(BaseModel):
    email: Union[EmailStr, None]
    passwd: Union[str, None]
    name: Union[str, None]
    state: Union[bool, None]
    is_admin: Union[bool, None]

    class Config:
        orm_mode = True