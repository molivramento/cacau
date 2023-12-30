from ninja import Router, Query
from core.products_attributes.manager import products_attributes
from core.products_attributes.schemas import ProductAttributeOut, ProductAttributeCreate, ProductAttributeUpdate, \
    ProductAttributeFilters

router = Router()


@router.get("/", response=list[ProductAttributeOut])
async def products_attributes_list(request, filters: Query[ProductAttributeFilters]):
    return await products_attributes.get_all()


@router.get("/{uuid}", response=ProductAttributeOut)
async def products_attributes_detail(request, uuid):
    return await products_attributes.get(uuid)


@router.post("/", response=ProductAttributeOut)
async def products_attributes_create(request, payload: ProductAttributeCreate):
    return await products_attributes.create(payload)


@router.put("/{uuid}", response=ProductAttributeOut)
async def products_attributes_update(request, uuid, payload: ProductAttributeUpdate):
    return await products_attributes.update(uuid, payload)


@router.delete("/{uuid}")
async def products_attributes_delete(request, uuid):
    return await products_attributes.delete(uuid)
