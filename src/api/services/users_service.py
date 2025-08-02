from src.api.db.repositories.users_repository import UsersRepository
from src.api.entities.user_table import UserTable
from src.api.schemas.users.add_user_model import AddUserModel
from src.api.schemas.users.read_user_model import ReadUserModel


class UsersService:
    def __init__(self, repository: UsersRepository):
        self.repository = repository

    async def get_user(self, request: ReadUserModel) -> UserTable | None:
        return await self.repository.get_user(request)

    async def add_user(self, request: AddUserModel) ->  None:
        return await self.repository.add_user(request)