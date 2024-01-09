from cacau.database_manager import DatabaseManager
from core.products_stock.models import ProductStock


class ProductStockManager(DatabaseManager):
    def __init__(self):
        super().__init__(ProductStock)


product_stock_manager = ProductStockManager()
