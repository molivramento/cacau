from cacau.database_manager import DatabaseManager
from core.products_attributes.models import ProductAttribute


class ProductAttributeManager(DatabaseManager):
    def __init__(self):
        super().__init__(ProductAttribute)


products_attributes = ProductAttributeManager()
