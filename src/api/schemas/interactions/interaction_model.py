from datetime import datetime, timezone
from uuid import UUID
from pydantic import BaseModel


class InteractionModel(BaseModel):
    user_id: UUID
    movie_id: UUID
    rating: int
    created_at: datetime
