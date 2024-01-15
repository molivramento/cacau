from cacau.database_manager import DatabaseManager
from core.products_options_values.manager import product_option_value_manager
from core.products_stock.models import ProductStock


class ProductStockManager(DatabaseManager):
    def __init__(self):
        super().__init__(ProductStock)

    def create(self, product_stock):
        product_option_value = [
            product_option_value_manager.get(uuid=uuid) for uuid in product_stock.product_option_value
        ]
        product_stock = product_stock.dict()
        product_stock.pop('product_option_value')
        product_stock = self.model.objects.create(**product_stock)
        for pov in product_option_value:
            pov.add(product_stock).save()
        return self.get(uuid=product_stock.uuid)


product_stock_manager = ProductStockManager()
