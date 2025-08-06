from typing import Iterable

from src.api.db.data_utils import DataUtils
from src.api.db.session import AsyncSession
from src.api.entities.interaction_table import InteractionTable
from src.api.schemas.batch.add_batch_model import AddBatchModel
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
            rating=request.rating,
            created_at=request.created_at,
        )
        self.session.add(interaction)

    async def add_interactions(self, request: AddBatchModel) ->  None:
        for chunk in DataUtils.chunks(request.batch):
            interactions = [
                InteractionTable(
                    user_id = item.user_id,
                    movie_id = item.movie_id,
                    rating = item.rating,
                    created_at=item.created_at,
                )
                for item in chunk
            ]
            self.session.add_all(interactions)
            await self.session.commit()