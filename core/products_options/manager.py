from cacau.database_manager import DatabaseManager
from core.products_options.models import ProductOption


class ProductOptionManager(DatabaseManager):
    def __init__(self):
        super().__init__(ProductOption)


product_options_manager = ProductOptionManager()
