from ninja import NinjaAPI

from core.users.api import router as users_router
from core.users.api_auth import router as auth_router
from core.categories.api import router as categories_router
from core.products_bases.api import router as products_bases_router
from core.products_stock.api import router as products_stock_router
from core.products_options.api import router as products_options_router
from core.products_options_values.api import router as products_options_values_router
api = NinjaAPI()


api.add_router("/auth", auth_router, tags=["Auth"])
api.add_router("/users", users_router, tags=["Users"])
api.add_router("/categories", categories_router, tags=["Categories"])
api.add_router("/products_options", products_options_router, tags=["Products Options"])
api.add_router("/products_options_values", products_options_values_router, tags=["Products Options Values"])
api.add_router("/products_bases", products_bases_router, tags=["Products Bases"])
api.add_router("/products_stock", products_stock_router, tags=["Products Stock"])
