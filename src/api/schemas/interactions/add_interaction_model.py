from datetime import datetime, timezone
from pydantic import BaseModel, Field
from uuid import UUID


class AddInteractionModel(BaseModel):
    user_id: UUID
    movie_id: UUID
    rating: int = Field(ge=1, le=10)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))