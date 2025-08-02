from pydantic import BaseModel
from uuid import UUID

class ReadRecommendationModel(BaseModel):
    user_id: UUID
    limit: int