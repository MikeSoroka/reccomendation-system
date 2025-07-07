from fastapi import APIRouter

from src.api.models.schemas.interactions.read_interaction_model import ReadInteractionModel
from src.api.requests.interactions.add_interactions_request import AddInteractionsRequest
from src.api.requests.interactions.read_interaction_request import ReadInteractionRequest
from src.api.models.schemas.interactions.add_interaction_model import AddInteractionModel
from uuid import UUID

router = APIRouter()

@router.get("/interactions")
async def read_item(user_id: UUID, movie_id: UUID):
    model = ReadInteractionModel(user_id=user_id, movie_id=movie_id)
    return ReadInteractionRequest.submit(model)

@router.post("/interactions")
async def add_item(user_id: UUID, movie_id: UUID, rating: int):
    model = AddInteractionModel(user_id=user_id, movie_id=movie_id, rating=rating)
    return AddInteractionsRequest.submit([model])