from uuid import UUID
from typing import Optional
from ninja import Schema, ModelSchema, FilterSchema
from core.categories.schemas import CategoryOut
from core.products_bases.models import ProductBase


class ProductBaseCreate(Schema):
    category_id: UUID
    name: str
    cost_base: float
    price_base: float


class ProductBaseOut(ModelSchema):
    # category: CategoryOut

    class Meta:
        model = ProductBase
        fields = '__all__'


class ProductBaseUpdate(Schema):
    category_id: Optional[UUID] = None
    name: Optional[str] = None
    cost_base: Optional[float] = None
    price_base: Optional[float] = None


class ProductBaseFilters(FilterSchema):
    category_id: Optional[UUID] = None
    name: Optional[str] = None
    name__icontains: Optional[str] = None
    cost_base: Optional[float] = None
    cost_base__gte: Optional[float] = None
    cost_base_lte: Optional[float] = None
    price_base: Optional[float] = None
    price_base__gte: Optional[float] = None
    price_base_lte: Optional[float] = None
