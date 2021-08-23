from app.database import db
from sqlalchemy import Column, String, Integer, Boolean


class User(db.base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String)
    passwd = Column(String)
    name = Column(String)
    state = Column(Boolean, default=1)
    is_admin = Column(Boolean, default=0)
