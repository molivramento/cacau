from uuid import uuid4
from django.db import models
from core.products_bases.models import ProductBase
from core.products_options_values.models import ProductOptionValue


class ProductStock(models.Model):
    uuid = models.UUIDField(primary_key=True, editable=False, default=uuid4, db_index=True)
    product_base = models.ForeignKey('products_bases.ProductBase', on_delete=models.CASCADE)
    product_option_value = models.ManyToManyField(ProductOptionValue)
    sku = models.CharField(max_length=255, null=True, default=None, db_index=True)
    barcode = models.CharField(max_length=255, null=True, default=None, db_index=True)
    quantity = models.IntegerField(default=0, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, db_index=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    weight = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
