from ninja import NinjaAPI

from core.users.api import router as users_router
from core.categories.api import router as categories_router
from core.products_options.api import router as products_options_router
from core.products_options_values.api import router as products_options_values_router

api = NinjaAPI()


api.add_router("/users", users_router, tags=["Users"])
api.add_router("/categories", categories_router, tags=["Categories"])
api.add_router("/products_options", products_options_router, tags=["Products Options"])
api.add_router("/products_options_values", products_options_values_router, tags=["Products Options Values"])
