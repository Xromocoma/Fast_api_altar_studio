from pydantic import BaseModel, EmailStr


class Login(BaseModel):
    email: EmailStr
    password: str


class UserInfo(BaseModel):
    id: int
    email: str
    passwd: str
    name: str
    state: bool = True
    is_admin: bool = False

