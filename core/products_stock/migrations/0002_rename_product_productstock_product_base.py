# Generated by Django 5.0 on 2024-01-13 02:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products_stock', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productstock',
            old_name='product',
            new_name='product_base',
        ),
    ]
