from uuid import uuid4

from django.db import models


class ProductAttribute(models.Model):
    uuid = models.UUIDField(primary_key=True, editable=False, default=uuid4, db_index=True)
    name = models.CharField(max_length=255, db_index=True)
    tag = models.CharField(max_length=255)
    unity = models.CharField(max_length=255)
