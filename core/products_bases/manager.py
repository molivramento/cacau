from cacau.database_manager import DatabaseManager
from core.categories.models import Category
from core.products_bases.models import ProductBase
from core.categories.manager import categories_manager


class ProductBaseManager(DatabaseManager):
    def __init__(self):
        super().__init__(ProductBase)


product_base_manager = ProductBaseManager()
