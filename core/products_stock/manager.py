from cacau.database_manager import DatabaseManager
from core.products_stock.models import ProductStock


class ProductStockManager(DatabaseManager):
    def __init__(self):
        super().__init__(ProductStock)

    def create(self, product_stock):
        product_stock = product_stock.dict()
        product_stock.pop('product_option_value')
        print(product_stock)
        return self.model.objects.create(product_stock)


product_stock_manager = ProductStockManager()
