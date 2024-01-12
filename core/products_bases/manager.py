from cacau.database_manager import DatabaseManager
from core.categories.models import Category
from core.products_bases.models import ProductBase
from core.categories.manager import categories_manager


class ProductBaseManager(DatabaseManager):
    def __init__(self):
        super().__init__(ProductBase)

    # def create(self, product_base):
    #     product_base.category = categories_manager.get(uuid=product_base.category)
    #     return self.model.objects.create(**product_base.dict())


product_base_manager = ProductBaseManager()
