from pydantic import BaseModel, EmailStr
from typing import Union

class UserLogin(BaseModel):
    email: EmailStr
    passwd: str

class UserLogout(BaseModel):
    id: int
    token: str


class UserFullData(BaseModel):
    id: int
    email: str
    passwd: str
    name: str
    state: bool = True
    is_admin: bool = False


class UserData(BaseModel):

    email: str
    passwd: str
    name: str
    state: bool = True
    is_admin: bool = False


class UserUpdate(BaseModel):
    email: Union[str, None]
    passwd: Union[str, None]
    name: Union[str, None]
    state: Union[bool, None]
    is_admin: Union[bool, None]


