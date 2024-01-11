from cacau.database_manager import DatabaseManager
from core.categories.models import Category
from core.categories.schemas import CategoryOut


class CategoryManager(DatabaseManager):
    def __init__(self):
        super().__init__(Category)

    async def create(self, payload):
        return await self.model.objects.acreate(**payload.dict())


categories_manager = CategoryManager()
