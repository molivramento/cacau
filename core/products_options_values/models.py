from uuid import uuid4
from django.db import models
from core.products_options.models import ProductOption


class ProductOptionValue(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    product_option = models.ForeignKey(ProductOption, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)
