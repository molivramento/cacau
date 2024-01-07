from uuid import UUID

from ninja import Router, Query
from core.products_options_values.manager import product_option_value_manager
from core.products_options_values.schemas import ProductOptionValueOut, ProductOptionValueFilter

router = Router()


@router.get("/", response=list[ProductOptionValueOut])
def get_product_option_values(request, filters: Query[ProductOptionValueFilter]):
    return product_option_value_manager.get_all(filters)


@router.get("/{uuid}", response=ProductOptionValueOut)
def get_product_option_value(request, uuid: UUID):
    return product_option_value_manager.get_by_id(uuid)


@router.post("/", response=ProductOptionValueOut)
def create_product_option_value(request, product_option_value: ProductOptionValueOut):
    return product_option_value_manager.create(product_option_value)


@router.put("/{uuid}", response=ProductOptionValueOut)
def update_product_option_value(request, uuid: UUID, product_option_value: ProductOptionValueOut):
    return product_option_value_manager.update(uuid, product_option_value)


@router.delete("/{uuid}", response=bool)
def delete_product_option_value(request, uuid: UUID):
    return product_option_value_manager.delete(uuid)

