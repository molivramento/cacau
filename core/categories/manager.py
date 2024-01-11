from cacau.database_manager import DatabaseManager
from core.categories.models import Category


class CategoryManager(DatabaseManager):
    def __init__(self):
        super().__init__(Category)

    async def create(self, payload):
        if payload.parent:
            payload.parent = await self.get(pk=payload.parent)
        return await self.model.objects.create(**payload.dict())


categories_manager = CategoryManager()
