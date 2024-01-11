from uuid import UUID
from ninja import Router, Query
from core.categories.manager import categories_manager
from core.categories.schemas import CategoryFilters, CategoryOut, CategoryCreate, CategoryUpdate

router = Router()


@router.get("/", response=list[CategoryOut])
async def categories_list(request, filters: Query[CategoryFilters]):
    return await categories_manager.get_all(filters)


@router.get("/{uuid}", response=CategoryOut)
def categories_detail(request, uuid: UUID):
    return categories_manager.get(uuid)


@router.post("/", response=CategoryOut)
async def categories_create(request, payload: CategoryCreate):
    return await categories_manager.create(payload)


@router.put("/{uuid}", response=CategoryCreate)
def categories_update(request, uuid: UUID, payload: CategoryUpdate):
    return categories_manager.update(uuid, payload)


@router.delete("/{uuid}", response=bool)
async def categories_delete(request, uuid: UUID):
    return await categories_manager.delete(uuid)
