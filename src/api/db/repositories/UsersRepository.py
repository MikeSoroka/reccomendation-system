from src.api.db.session import AsyncSession
from src.api.entities.user_table import UserTable
from src.api.schemas.users.add_user_model import AddUserModel
from src.api.schemas.users.read_user_model import ReadUserModel


class UsersRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_user(self, request: ReadUserModel) -> UserTable | None:
        return await self.session.get(UserTable, request.id)

    async def create_user(self, request: AddUserModel) ->  None:
        user = UserTable(
            id = request.id
        )
        self.session.add(user)