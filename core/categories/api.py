from uuid import UUID

from ninja import Router, Query
from core.categories.models import Category
from core.categories.schemas import CategoryFilters, CategoryOut, CategoryCreate, CategoryUpdate

router = Router()


@router.get("/", response=list[CategoryOut])
async def categories_list(request, filters: Query[CategoryFilters]):
    filters = {key: value for key, value in filters.dict().items() if value}
    categories = [category async for category in Category.objects.filter(**filters)]
    return categories


@router.get("/{uuid}", response=CategoryOut)
async def categories_detail(request, uuid: UUID):
    return await Category.objects.aget(uuid=uuid)


@router.post("/", response=CategoryOut)
async def categories_create(request, payload: CategoryCreate):
    return await Category.objects.acreate(**payload.dict())


@router.put("/{uuid}", response=CategoryOut)
async def categories_update(request, uuid: UUID, payload: CategoryUpdate):
    category = await Category.objects.aget(uuid=uuid)
    for attr, value in payload.dict().items():
        setattr(category, attr, value)
    await category.asave()
    return category


@router.delete("/{uuid}")
async def categories_delete(request, uuid: UUID):
    category = await Category.objects.aget(uuid=uuid)
    await category.adelete()
    return {"success": True}