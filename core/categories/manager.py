from cacau.database_manager import DatabaseManager
from core.categories.models import Category


class CategoryManager(DatabaseManager):
    def __init__(self):
        super().__init__(Category)

    def create(self, payload):
        if payload.parent:
            payload.parent = self.model.objects.get(pk=payload.parent)
        return self.model.objects.create(**payload.dict())


categories = CategoryManager()
