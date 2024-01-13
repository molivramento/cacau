from typing import Optional
from ninja import Schema, ModelSchema
from core.products_options.models import ProductOption


# class ProductOptionCreate(Schema):
#     name: str
#     tag: str
#     unity: Optional[str] = None

class ProductOptionCreate(ModelSchema):
    class Meta:
        model = ProductOption
        fields = '__all__'
        exclude = ['uuid']


class ProductOptionOut(ModelSchema):
    class Meta:
        model = ProductOption
        fields = '__all__'


class ProductOptionUpdate(Schema):
    name: Optional[str] = None
    tag: Optional[str] = None
    unity: Optional[str] = None


class ProductOptionFilters(Schema):
    name: Optional[str] = None
    name__icontains: Optional[str] = None
    tag: Optional[str] = None
    tag__icontains: Optional[str] = None
    unity: Optional[str] = None
    unity__icontains: Optional[str] = None

