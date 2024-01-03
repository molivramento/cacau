from ninja import NinjaAPI

from core.users.api import router as users_router
from core.categories.api import router as categories_router
from core.products_attributes.api import router as products_attributes_router

api = NinjaAPI()


api.add_router("/users", users_router, tags=["Users"])
api.add_router("/categories", categories_router, tags=["Categories"])
api.add_router("/products_attributes", products_attributes_router, tags=["Products Attributes"])
