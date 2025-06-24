from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4
from src.api.models.schemas.base_add_model import BaseAddModel
from datetime import datetime, timezone
from sqlmodel import Field, SQLModel
from uuid import UUID, uuid4


class AddInteractionModel(BaseAddModel, table=False):
    user_id: UUID
    movie_id: UUID
    rating: int = Field(ge=1, le=10)
    created_at: datetime | None