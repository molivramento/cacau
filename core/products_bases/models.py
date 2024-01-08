from uuid import uuid4
from django.db import models
from core.categories.models import Category


class ProductBase(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    cost_base = models.DecimalField(max_digits=10, decimal_places=2)
    price_base = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=None)
