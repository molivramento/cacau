from cacau.database_manager import DatabaseManager
from core.categories.models import Category


class CategoryManager(DatabaseManager):
    def __init__(self):
        super().__init__(Category)

    async def create(self, payload):
        payload.parent = await self.model.objects.aget(pk=payload.parent)
        return await self.model.objects.acreate(**payload.dict())


categories = CategoryManager()
