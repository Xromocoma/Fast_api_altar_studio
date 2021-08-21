import sqlalchemy
from sqlalchemy.orm import scoped_session, sessionmaker
from app.models import User
from sqlalchemy import Table, Column, String, Integer, MetaData, Boolean
from contextlib import contextmanager
import app.config as config


class PostgreDB:
    def __init__(self):
        self.engine = sqlalchemy.create_engine(config.POSTGRES_ENGINE_URL,
                                               echo=True,
                                               pool_size=6,
                                               max_overflow=10,
                                               pool_pre_ping=True
                                               )

        self.engine.connect()
        # scoped_session()
        result = self.engine.execute("Select * FROM users;")
        for item in result:
            print(item)
        ## try exception sql
        meta = MetaData(self.engine)
        users_table = Table('users',
                            meta,
                            Column('id', Integer),
                            Column('email', String),
                            Column('passwd', String),
                            Column('name', String),
                            Column('state', Boolean),
                            Column('is_admin', Boolean)
                            )
        insert_statment = users_table.insert().values(email='Test', passwd='123', name='Totsa')
        self.engine.execute(insert_statment)

        select_statment = users_table.select()
        result = self.engine.execute(select_statment)
        for item in result:
            print(item)

        update_statment = users_table.update().where(users_table.c.email == 'Test').values(email='some@email.ru',
                                                                                           name='Tom')
        self.engine.execute(update_statment)

        delete_statment = users_table.delete().where(users_table.c.email == 'some@email.ru')
        self.engine.execute(delete_statment)

        select_statment = users_table.select()
        result = self.engine.execute(select_statment)
        for item in result:
            print(item)

        ## full ORM support

        from sqlalchemy.ext.declarative import declarative_base

        base = declarative_base()
        print(base)

        class User(base):
            __tablename__ = 'users'

            id = Column(Integer, primary_key=True)
            email = Column(String)
            passwd = Column(String)
            name = Column(String)
            state = Column(Boolean, default=1)
            is_admin = Column(Boolean, default=0)

        Session = sessionmaker(self.engine)
        session = Session()

        base.metadata.create_all(self.engine)

        user_bob = User(email='SOme', passwd='123', name="Bob", is_admin=True)
        session.add(user_bob)
        session.commit()

        users = session.query(User)
        for user in users:
            print(user.email, user.name)

        user_bob.name = 'Piter'
        session.commit()

        session.delete(user_bob)
        session.commit()

        users = session.query(User)
        for user in users:
            print(user.email, user.name)


db = PostgreDB()
