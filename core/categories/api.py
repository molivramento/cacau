from uuid import UUID
from ninja import Router, Query
from core.categories.manager import categories
from core.categories.schemas import CategoryFilters, CategoryOut, CategoryCreate, CategoryUpdate

router = Router()


@router.get("/", response=list[CategoryOut])
async def categories_list(request, filters: Query[CategoryFilters]):
    return await categories.get_all(filters)


@router.get("/{uuid}", response=CategoryOut)
async def categories_detail(request, uuid: UUID):
    return await categories.get(uuid)


@router.post("/", response=CategoryOut)
async def categories_create(request, payload: CategoryCreate):
    return await categories.create(payload)


@router.put("/{uuid}", response=CategoryOut)
async def categories_update(request, uuid: UUID, payload: CategoryUpdate):
    return categories.update(uuid, payload)


@router.delete("/{uuid}")
async def categories_delete(request, uuid: UUID):
    return await categories.delete(uuid)