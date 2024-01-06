from uuid import UUID
from ninja import Router, Query
from core.categories.manager import categories
from core.categories.schemas import CategoryFilters, CategoryOut, CategoryCreate, CategoryUpdate, \
    CategoryOutWithoutParent

router = Router()


@router.get("/", response=list[CategoryOut])
def categories_list(request, filters: Query[CategoryFilters]):
    return categories.get_all(filters)


@router.get("/{uuid}", response=CategoryOut)
def categories_detail(request, uuid: UUID):
    return categories.get(uuid)


@router.post("/", response=CategoryOut)
def categories_create(request, payload: CategoryCreate):
    return categories.create(payload)


@router.put("/{uuid}", response=CategoryOut)
def categories_update(request, uuid: UUID, payload: CategoryUpdate):
    print(uuid)
    return categories.update(uuid, payload)


@router.delete("/{uuid}", response=bool)
async def categories_delete(request, uuid: UUID):
    return await categories.delete(uuid)
