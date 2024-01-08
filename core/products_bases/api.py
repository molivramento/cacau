from uuid import UUID

from ninja import Router, Query
from core.products_bases.manager import product_base_manager
from core.products_bases.schemas import ProductBaseCreate, ProductBaseOut, ProductBaseUpdate, ProductBaseFilters

router = Router()


@router.get("", response=list[ProductBaseOut])
def get_all(request, filters: Query[ProductBaseFilters]):
    return product_base_manager.get_all(filters)


@router.get("/{uuid}", response=ProductBaseOut)
def get_by_uuid(request, uuid: UUID):
    return product_base_manager.get_by_uuid(uuid)


@router.post("", response=ProductBaseOut)
def create(request, product_base: ProductBaseCreate):
    return product_base_manager.create(product_base)


@router.put("/{uuid}", response=ProductBaseOut)
def update(request, uuid: UUID, product_base: ProductBaseUpdate):
    return product_base_manager.update(uuid, product_base)


@router.delete("/{uuid}")
def delete(request, uuid: UUID):
    return product_base_manager.delete(uuid)
