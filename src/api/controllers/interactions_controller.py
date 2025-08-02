from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

from src.api.core.container import Container
from src.api.schemas.interactions.read_interaction_model import ReadInteractionModel
from src.api.schemas.interactions.add_interaction_model import AddInteractionModel
from uuid import UUID

from src.api.services.interactions_service import InteractionsService

router = APIRouter()

@router.get("/interactions")
@inject
async def read_interaction(
    user_id: UUID,
    movie_id: UUID,
    interactions_service: InteractionsService = Depends(Provide[Container.interactions_service]),
):
    model = ReadInteractionModel(user_id=user_id, movie_id=movie_id)
    return await interactions_service.get_interaction(model)

@router.post("/interactions")
@inject
async def add_interaction(
    user_id: UUID,
    movie_id: UUID,
    rating: int,
    interactions_service: InteractionsService = Depends(Provide[Container.interactions_service]),
):
    model = AddInteractionModel(user_id=user_id, movie_id=movie_id, rating=rating)
    await interactions_service.add_interaction(model)