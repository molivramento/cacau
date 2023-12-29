from uuid import UUID
from ninja import Router, Query
from core.users.manager import users
from core.users.schemas import UserFilters, UserOut, UserIn, UserUpdate

router = Router(tags=["users"])


@router.get("/", response=list[UserOut])
async def users_list(request, filters: Query[UserFilters]):
    return await users.get_all(filters)


@router.get("/{uuid}", response=UserOut)
async def users_detail(request, uuid: UUID):
    return await users.get(uuid)


@router.post("/", response=UserOut)
async def users_create(request, payload: UserIn):
    return await users.create(payload)


@router.put("/{uuid}", response=UserOut)
async def users_update(request, uuid: UUID, payload: UserUpdate):
    return await users.update(uuid, payload)


@router.delete("/{uuid}")
async def users_delete(request, uuid: UUID):
    return await users.delete(uuid)
