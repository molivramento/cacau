# Generated by Django 5.0 on 2024-01-15 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_options_values', '0001_initial'),
        ('products_stock', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productstock',
            name='product_option_value',
            field=models.ManyToManyField(to='products_options_values.productoptionvalue'),
        ),
    ]
