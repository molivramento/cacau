from uuid import UUID
from ninja import Router, Query
from core.users.models import User
from core.users.schemas import UserFilters, UserOut, UserIn, UserUpdate

router = Router(tags=["users"])


@router.get("/", response=list[UserOut])
async def users_list(request, filters: Query[UserFilters]):
    filters = {key: value for key, value in filters.dict().items() if value}
    users = [user async for user in User.objects.filter(**filters)]
    return users


@router.get("/{uuid}", response=UserOut)
async def users_detail(request, uuid: UUID):
    return await User.objects.aget(uuid=uuid)


@router.post("/", response=UserOut)
async def users_create(request, payload: UserIn):
    return await User.objects.acreate(**payload.dict())


@router.put("/{uuid}", response=UserOut)
async def users_update(request, uuid: UUID, payload: UserUpdate):
    user = await User.objects.aget(uuid=uuid)
    for attr, value in payload.dict().items():
        setattr(user, attr, value)
    await user.asave()
    return user


@router.delete("/{uuid}")
async def users_delete(request, uuid: UUID):
    user = await User.objects.aget(uuid=uuid)
    await user.adelete()
    return {"success": True}
