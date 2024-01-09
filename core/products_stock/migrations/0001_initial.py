# Generated by Django 5.0 on 2024-01-09 16:43

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products_bases', '0001_initial'),
        ('products_options_values', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductStock',
            fields=[
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('sku', models.CharField(db_index=True, default=None, max_length=255, null=True)),
                ('barcode', models.CharField(db_index=True, default=None, max_length=255, null=True)),
                ('quantity', models.IntegerField(db_index=True, default=0)),
                ('price', models.DecimalField(db_index=True, decimal_places=2, default=0.0, max_digits=10)),
                ('cost', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('weight', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products_bases.productbase')),
                ('product_option_value', models.ManyToManyField(db_index=True, to='products_options_values.productoptionvalue')),
            ],
        ),
    ]