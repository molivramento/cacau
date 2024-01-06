from ninja import NinjaAPI

from core.users.api import router as users_router
from core.categories.api import router as categories_router

api = NinjaAPI()


api.add_router("/users", users_router, tags=["Users"])
api.add_router("/categories", categories_router, tags=["Categories"])
