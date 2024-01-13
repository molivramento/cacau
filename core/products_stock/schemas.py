from typing import Optional
from uuid import UUID

from ninja import ModelSchema, Schema

from core.products_bases.schemas import ProductBaseOut
from core.products_options_values.schemas import ProductOptionValueOut
from core.products_stock.models import ProductStock


class ProductStockCreate(ModelSchema):
    product_option_value: list[UUID]
    # product_base_id: UUID

    class Meta:
        model = ProductStock
        fields = '__all__'
        exclude = ['uuid']


class ProductStockOut(ModelSchema):
    product: ProductBaseOut
    product_option_value: ProductOptionValueOut

    class Meta:
        model = ProductStock
        fields = '__all__'


class ProductStockUpdate(Schema):
    product: Optional[UUID] = None
    product_option_value: Optional[UUID] = None
    sku: Optional[str] = None
    barcode: Optional[str] = None
    quantity: Optional[int] = None
    price: Optional[float] = None
    cost: Optional[float] = None
    weight: Optional[float] = None


class ProductStockFilter(Schema):
    product_id: Optional[UUID] = None
    product_option_value_id: Optional[UUID] = None
    sku: Optional[str] = None
    barcode: Optional[str] = None
    quantity__lte: Optional[int] = None
    quantity__gte: Optional[int] = None
    price__lte: Optional[float] = None
    price__gte: Optional[float] = None
