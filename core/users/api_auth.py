from ninja import Router
from jwt import PyJWTError, encode
from core.users.models import User

from core.users.security import AuthBearer

router = Router()


@router.post("/token")
def get_token(request, username: str, password: str):
    user = User.objects.get(email=username)
    if not user.check_password(password):
        return {"error": "Invalid credentials"}
    if user is None:
        return {"error": "Invalid credentials"}
    try:
        token = encode({"username": user.email}, "secret", algorithm="HS256")
    except PyJWTError:
        return {"error": "Internal error"}
    return {"token": token}


@router.get("/me", auth=AuthBearer())
def me(request):
    return request.auth
