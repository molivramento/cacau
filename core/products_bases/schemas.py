from uuid import UUID
from typing import Optional
from ninja import Schema, ModelSchema
from core.categories.schemas import CategoryOut
from core.products_bases.models import ProductBase


class ProductBaseCreate(ModelSchema):
    class Meta:
        model = ProductBase
        fields = '__all__'
        exclude = ["uuid"]


class ProductBaseOut(ModelSchema):
    category: CategoryOut

    class Meta:
        model = ProductBase
        fields = '__all__'


class ProductBaseUpdate(Schema):
    category_id: Optional[UUID] = None
    name: Optional[str] = None
    cost_base: Optional[float] = None
    price_base: Optional[float] = None


class ProductBaseFilters(Schema):
    category_id: Optional[UUID] = None
    name: Optional[str] = None
    name__icontains: Optional[str] = None
    cost_base: Optional[float] = None
    cost_base__gte: Optional[float] = None
    cost_base_lte: Optional[float] = None
    price_base: Optional[float] = None
    price_base__gte: Optional[float] = None
    price_base_lte: Optional[float] = None