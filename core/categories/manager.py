from cacau.database_manager import DatabaseManager
from core.categories.models import Category


class CategoryManager(DatabaseManager):
    def __init__(self):
        super().__init__(Category)


categories_manager = CategoryManager()
