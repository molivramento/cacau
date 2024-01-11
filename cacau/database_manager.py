class DatabaseManager:
    def __init__(self, model):
        self.model = model

    async def get_all(self, filters=None):
        filters = {key: value for key, value in filters.dict().items() if value is not None}
        users = [user async for user in self.model.objects.filter(**filters)]
        return users

    async def get(self, uuid):
        return await self.model.objects.aget(uuid=uuid)

    async def create(self, payload):
        return await self.model.objects.acreate(**payload.dict())

    async def update(self, uuid, payload):
        obj = await self.get(uuid=uuid)
        payload = [(attr, value) for attr, value in payload.dict().items() if value is not None]
        for attr, value in payload:
            setattr(obj, attr, value)
        await obj.asave()
        return obj

    async def delete(self, uuid):
        try:
            user = await self.get(uuid=uuid)
            await user.adelete()
            return True
        except self.model.DoesNotExist:
            return False
