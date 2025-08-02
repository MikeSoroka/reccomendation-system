from src.api.db.session import AsyncSession
from src.api.entities.interaction_table import InteractionTable
from src.api.schemas.interactions.add_interaction_model import AddInteractionModel
from src.api.schemas.interactions.read_interaction_model import ReadInteractionModel


class InteractionsRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_interaction(self, request: ReadInteractionModel) -> InteractionTable | None:
        return await self.session.get(InteractionTable, request.id)

    async def add_interaction(self, request: AddInteractionModel) ->  None:
        interaction = InteractionTable(
            user_id = request.user_id,
            movie_id = request.movie_id,
        )
        self.session.add(interaction)