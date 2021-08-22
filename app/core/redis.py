import jwt
import redis
from app.config import settings


class Redis:
    def __init__(self):
        self.instance = redis.Redis(host=settings.REDIS_HOST,
                                     port=settings.REDIS_PORT)

    def set(self, name, value):
        self.instance.set(name=name,
                       value=value,
                       keepttl=settings.REDIS_TTL)

    def get(self, name):
        return self.instance.get(name)

    def remove(self, name):
        self.instance.delete(name)


