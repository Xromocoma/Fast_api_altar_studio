import jwt
from app.config import settings
from app.core.redis import Redis
from app.shemas import UserFullData


class Auth(Redis):
    def set_jwt_token(self, user_id: int, payload: dict) -> None:
        self.set(name=f'Access_{user_id}',
                 value=payload,
                 keepttl=settings.REDIS_TTL)

    def get_jwt_token(self, user_id: int):
        return self.get(f'Access_{user_id}')

    def remove_jwt_token(self, user_id: int) -> None:
        self.remove(f'Access_{user_id}')

    def check_jwt_token(self, user_id: int, token: str) -> bool:
        token_from_redis = self.get_jwt_token(user_id)
        if token_from_redis:
            if token == token_from_redis:
                return True
        return False

    def create_jwt_token(self, user: UserFullData) -> None:
            user_payload = {
            "id": user.id,
            "email": user.email,
            "state": user.state,
            "is_admin": user.is_admin
            }
            payload = jwt.encode(user_payload, settings.JWT_KEY, algorithm='HS256').decode('utf-8')
            self.set_jwt_token(user_id=user.id,
                               payload=payload)



auth = Auth()

