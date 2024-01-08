from uuid import uuid4
from django.db import models

from core.products_bases.models import ProductBase
from core.products_options_values.models import ProductOptionValue


class ProductStock(models.Model):
    uuid = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    product = models.ForeignKey(ProductBase, on_delete=models.CASCADE)
    product_option_value = models.ManyToManyField(ProductOptionValue, on_delete=models.CASCADE)
    sku = models.CharField(max_length=255, null=True, default=None)
    barcode = models.CharField(max_length=255, null=True, default=None)
    quantity = models.IntegerField(default=0)
    add_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    add_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    add_weight = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)