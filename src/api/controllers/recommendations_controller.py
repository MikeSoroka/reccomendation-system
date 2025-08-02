from fastapi import APIRouter
from src.api.schemas.recommendations.read_recommendation_model import ReadRecommendationModel
from uuid import UUID

router = APIRouter()

@router.get("/recommendation/{user_id}")
async def read_item(user_id: UUID, limit: int = 10):
    model = ReadRecommendationModel(user_id=user_id, limit=limit)
    return "reccomendation"