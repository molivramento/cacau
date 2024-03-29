from ninja import Router, Query
from core.products_options.schemas import ProductOptionCreate, ProductOptionOut, ProductOptionFilters
from core.products_options.manager import product_options_manager

router = Router(tags=["Product Options"])


@router.get("/", response=list[ProductOptionOut])
def get_all(request, filters: Query[ProductOptionFilters]):
    return product_options_manager.get_all(filters)


@router.get("/{uuid}", response=ProductOptionOut)
def get_one(request, uuid: str):
    return product_options_manager.get_one(uuid)


@router.post("/", response=ProductOptionOut)
def create(request, payload: ProductOptionCreate):
    return product_options_manager.create(payload)


@router.put("/{uuid}", response=ProductOptionOut)
def update(request, uuid: str, payload: ProductOptionCreate):
    return product_options_manager.update(uuid, payload)


@router.delete("/{uuid}")
def delete(request, uuid: str):
    return product_options_manager.delete(uuid)

