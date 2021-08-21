from app.database import db
from app.shemas import UserInfo
from app.models import User
from sqlalchemy import update,delete


def get_all_users():
    session = db.session()
    users = session.query(User)
    result = []
    for user in users:
        result.append(user)
    return result


def get_user(user_id: int):
    session = db.session()
    user = session.query(User).where(User.id == user_id).first()
    return user


def update_user(user: UserInfo):
    session = db.session()
    user = session.execute(update(User).where(User.id == user.id).values(user.dict()))
    session.commit()
    return user


def delete_user(user_id: int):
    session = db.session()
    session.execute(delete(User).where(User.id == user_id))
    session.commit()
    return True