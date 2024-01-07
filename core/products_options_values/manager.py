from cacau.database_manager import DatabaseManager
from core.products_options_values.models import ProductOptionValue


class ProductOptionValueManager(DatabaseManager):
    def __init__(self):
        super().__init__(ProductOptionValue)


product_option_value_manager = ProductOptionValueManager()
