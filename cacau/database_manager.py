from asgiref.sync import sync_to_async

from core.categories.schemas import CategoryOut


class DatabaseManager:
    def __init__(self, model):
        self.model = model

    def get_all(self, filters=None):
        filters = {key: value for key, value in filters.dict().items() if value}
        users = self.model.objects.prefetch_related('parent').filter(**filters)
        return users

    def get(self, uuid):
        return self.model.objects.get(uuid=uuid)

    def create(self, payload):
        return self.model.objects.create(**payload.dict())

    async def update(self, uuid, payload):
        obj = await self.model.objects.aget(uuid=uuid)
        for attr, value in payload.dict().items():
            setattr(obj, attr, value)
        await obj.asave()
        return obj

    async def delete(self, uuid):
        user = await self.model.objects.aget(uuid=uuid)
        return await user.adelete()
