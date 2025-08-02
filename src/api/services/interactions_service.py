from src.api.db.repositories.interactions_repository import InteractionsRepository
from src.api.entities.interaction_table import InteractionTable
from src.api.schemas.interactions.add_interaction_model import AddInteractionModel
from src.api.schemas.interactions.read_interaction_model import ReadInteractionModel


class InteractionsService:
    def __init__(self, repository: InteractionsRepository):
        self.repository = repository

    async def get_interaction(self, request: ReadInteractionModel) -> InteractionTable | None:
        return await self.repository.get_interaction(request)

    async def add_interaction(self, request: AddInteractionModel) ->  None:
        return await self.repository.add_interaction(request)