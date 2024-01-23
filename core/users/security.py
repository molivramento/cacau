import jwt
from ninja.security import HttpBearer


class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        try:
            return jwt.decode(token, "secret", algorithms=["HS256"])
        except jwt.DecodeError:
            return None
