from cacau.database_manager import DatabaseManager
from core.users.models import User


class UserManager(DatabaseManager):
    def __init__(self):
        super().__init__(User)


users_manager = UserManager()
