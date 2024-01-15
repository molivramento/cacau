from cacau.database_manager import DatabaseManager
from core.products_options_values.manager import product_option_value_manager
from core.products_stock.models import ProductStock


class ProductStockManager(DatabaseManager):
    def __init__(self):
        super().__init__(ProductStock)

    def create(self, product_stock):
        product_option_value = product_option_value_manager.get(uuid=product_stock.product_option_value_id)
        params = product_stock.dict()
        params.pop('product_option_value_id')
        product_stock = self.model.objects.create(**params)
        product_stock.product_option_value.add(product_option_value)
        product_stock.save()
        return product_stock

    def get_all(self, filters=None):
        filters = {key: value for key, value in filters.dict().items() if value is not None}
        # users = [user async for user in self.model.objects.filter(**filters)]
        return self.model.objects.filter(**filters)


product_stock_manager = ProductStockManager()
