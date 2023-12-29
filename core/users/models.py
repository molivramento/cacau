from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models

from core.users.managers import UserManager


class User(AbstractUser):
    uuid = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    email = models.EmailField(unique=True)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
