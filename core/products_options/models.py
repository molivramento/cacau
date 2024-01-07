from django.db import models


class ProductOption(models.Model):
    uuid = models.UUIDField(primary_key=True, editable=False)
    name = models.CharField(max_length=255, unique=True)
    tag = models.CharField(max_length=255)
    unity = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = "product_options"
        ordering = ["name"]
