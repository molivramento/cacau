from uuid import uuid4

from django.db import models


class ProductAttribute(models.Model):
    uuid = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField(max_length=255)
    tag = models.CharField(max_length=255)
    unity = models.CharField(max_length=255)
