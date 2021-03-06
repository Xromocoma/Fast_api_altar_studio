from time import sleep
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from app.config import settings


class PostgreDB:
    def __init__(self):
        sleep(2)  # Несмотря на depent_on в докере, сервис все равно не успевает.
        self.engine = create_engine(settings.POSTGRES_ENGINE_URI,
                                    pool_size=6,
                                    max_overflow=10,
                                    pool_pre_ping=True
                                    )
        self.session = scoped_session(sessionmaker(self.engine))

        self.base = declarative_base()
        self.base.metadata.create_all(self.engine)

    def session(self):
        with self.session() as session:
            try:
                yield session
            except Exception:
                session.rollback()
                raise
            finally:
                session.close()


db = PostgreDB()
