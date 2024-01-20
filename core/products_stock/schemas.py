from uuid import UUID
from typing import Optional
from ninja import ModelSchema, Schema
from core.products_stock.models import ProductStock
from core.products_bases.schemas import ProductBaseOut
from core.products_options_values.schemas import ProductOptionValueOut


class ProductStockCreate(ModelSchema):
    product_option_value_id: UUID
    product_base_id: UUID

    class Meta:
        model = ProductStock
        fields = '__all__'
        exclude = ['uuid', 'product_option_value']


class ProductStockOut(ModelSchema):
    product_base: ProductBaseOut
    product_option_value: list[ProductOptionValueOut]

    class Meta:
        model = ProductStock
        fields = '__all__'
        exclude = ['product_option_value']


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
    product_base_id: Optional[UUID] = None
    product_option_value_id: Optional[UUID] = None
    product_base__name__icontains: Optional[str] = None
    product_option_value__name__icontains: Optional[str] = None
    sku: Optional[str] = None
    barcode: Optional[str] = None
    quantity__lte: Optional[int] = None
    quantity__gte: Optional[int] = None
    price__lte: Optional[float] = None
    price__gte: Optional[float] = None
