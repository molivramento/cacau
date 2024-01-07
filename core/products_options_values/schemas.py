from typing import Optional
from uuid import UUID

from ninja import Schema, ModelSchema

from core.products_options.schemas import ProductOptionOut
from core.products_options_values.models import ProductOptionValue


class ProductOptionValueCreate(Schema):
    option_value_id: UUID
    value: str


class ProductOptionValueOut(ModelSchema):
    product_option: ProductOptionOut

    class Meta:
        model = ProductOptionValue
        fields = '__all__'


class ProductOptionValueUpdate(Schema):
    value: Optional[str] = None
    product_option_id: Optional[UUID] = None


class ProductOptionValueFilter(Schema):
    value: Optional[str] = None
    value__contains: Optional[str] = None
    product_option_id: Optional[UUID] = None
