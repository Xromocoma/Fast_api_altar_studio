from pydantic import BaseModel,EmailStr


class Login(BaseModel):
    email: EmailStr
    password: str


class User(BaseModel):
    id: int
    email: str
    password: str
    name: str
    state: bool = True
    is_admin: bool = False


