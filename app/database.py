from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from contextlib import contextmanager
import app.config as config
from sqlalchemy.ext.declarative import declarative_base


class PostgreDB:
    def __init__(self):
        self.engine = create_engine(config.POSTGRES_ENGINE_URL,
                                               echo=True,
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
