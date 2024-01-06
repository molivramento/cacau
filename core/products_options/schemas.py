from typing import Optional

from ninja import Schema, ModelSchema

from core.products_options.models import ProductOption


class ProductOptionCreate(Schema):
    name: str


class ProductOptionOut(ModelSchema):
    class Meta:
        model = ProductOption
        fields = '__all__'


class ProductOptionUpdate(Schema):
    name: Optional[str] = None


class ProductOptionFilters(Schema):
    name: Optional[str] = None
    name__icontains: Optional[str] = None

