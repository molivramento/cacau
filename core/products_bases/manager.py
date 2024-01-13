from cacau.database_manager import DatabaseManager
from core.products_bases.models import ProductBase


class ProductBaseManager(DatabaseManager):
    def __init__(self):
        super().__init__(ProductBase)


product_base_manager = ProductBaseManager()
