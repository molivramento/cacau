class DatabaseManager:
    def __init__(self, model):
        self.model = model

    async def get_all(self, filters=None):
        filters = {key: value for key, value in filters.dict().items() if value}
        return [user async for user in self.model.objects.filter(**filters)]

    async def get(self, uuid):
        return await self.model.objects.aget(uuid=uuid)

    async def create(self, payload):
        return await self.model.objects.acreate(**payload.dict())

    async def update(self, uuid, payload):
        obj = await self.model.objects.aget(uuid=uuid)
        for attr, value in payload.dict().items():
            setattr(obj, attr, value)
        await obj.asave()
        return obj

    async def delete(self, uuid):
        user = await self.model.objects.aget(uuid=uuid)
        return await user.adelete()
