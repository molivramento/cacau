from uuid import uuid4

from django.db import models


class Category(models.Model):
    uuid = models.UUIDField(primary_key=True, editable=False, default=uuid4, db_index=True)
    name = models.CharField(max_length=255, db_index=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, default=None, null=True, db_index=True)
