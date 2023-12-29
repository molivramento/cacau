from uuid import UUID
from ninja import Schema
from typing import Optional
from datetime import datetime
from pydantic import EmailStr


class UserIn(Schema):
    email: EmailStr
    password: str


class UserOut(Schema):
    uuid: UUID
    email: str
    is_active: bool
    is_superuser: bool
    last_login: Optional[datetime]
    date_joined: Optional[datetime]


class UserUpdate(Schema):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = None
    is_superuser: Optional[bool] = None


class UserPasswordUpdate(Schema):
    password: str
    new_password: str


class UserFilters(Schema):
    email: Optional[EmailStr] = None
    email__icontains: Optional[str] = None
    is_active: Optional[bool] = None
    is_superuser: Optional[bool] = None
    date_joined__lte: Optional[datetime] = None
    date_joined__gte: Optional[datetime] = None
    last_login__lte: Optional[datetime] = None
    last_login__gte: Optional[datetime] = None
