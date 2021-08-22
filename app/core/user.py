import hashlib
from fastapi import HTTPException
from app.database import db
from app.shemas import UserData, UserUpdate, UserLogin, UserLogout
from app.models import User
from sqlalchemy import update, delete
from app.core.authorization import auth


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


def update_user(user_id: int, user: dict):
    """
    :param user_id:
    :param user:
    :return:
    """
    # создаем новый dict с не пустыми значениями
    update_values = {}
    for item in user:
        if user[item]:
            update_values.update({item: user[item]})

    if update_values.get('passwd'):
        update_values['passwd'] = passwd_to_hash(update_values['passwd'])

    session = db.session()
    user_in_base = session.query(User).where(User.id == user_id).first()
    if not user_in_base:
        HTTPException(status_code=400, detail='User not found')
    user = session.execute(update(User).where(User.id == user_id).values(**update_values))
    print(user)
    session.commit()

    return user


def delete_user(user_id: int):
    session = db.session()
    session.execute(delete(User).where(User.id == user_id))
    session.commit()
    return True


def create_user(user: UserData):
    session = db.session()
    new_user = User(email=user.email,
                    passwd=passwd_to_hash(user.passwd),
                    name=user.name,
                    state=user.state,
                    is_admin=user.is_admin)
    session.add(new_user)
    session.commit()


def passwd_to_hash(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


def user_login(user: UserLogin):
    session = db.session()
    user.passwd = passwd_to_hash(user.passwd)
    user_in_base = session.query(User).where(User.email == user.email).first()
    if not user_in_base:
        HTTPException(status_code=400, detail='User not found')
    if user_in_base.password != user.passwd:
        HTTPException(status_code=400, detail='email or password invalid')
    access_token = auth.create_jwt_token(user_in_base)
    return {"access_token": access_token, "admin": True}


def user_logout(user: UserLogout) -> bool or Exception:
    session = db.session()
    user.passwd = passwd_to_hash(user.passwd)
    user_in_base = session.query(User).where(User.id == user.id).first()
    if not user_in_base:
        HTTPException(status_code=400, detail='User not found')

    auth.remove_jwt_token(user.id)
    return True
