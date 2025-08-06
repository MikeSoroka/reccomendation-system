from src.api.db.data_utils import DataUtils
from src.api.db.session import AsyncSession
from src.api.entities.user_table import UserTable
from src.api.schemas.batch.add_batch_model import AddBatchModel
from src.api.schemas.users.add_user_model import AddUserModel
from src.api.schemas.users.read_user_model import ReadUserModel


class UsersRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_user(self, request: ReadUserModel) -> UserTable | None:
        return await self.session.get(UserTable, request.id)

    async def add_user(self, request: AddUserModel) ->  None:
        user = UserTable(
            id = request.id
        )
        self.session.add(user)

    async def add_users(self, request: AddBatchModel) ->  None:
        for chunk in DataUtils.chunks(request.batch):
            users = [
                UserTable(
                    id = item.id
                )
                for item in chunk
            ]
            self.session.add_all(users)
        await self.session.commit()