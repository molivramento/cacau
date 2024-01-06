from django.db import models


class ProductOption(models.Model):
    uuid = models.UUIDField(primary_key=True, editable=False)
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = "product_options"
        ordering = ["name"]

    def __str__(self):
        return self.name
