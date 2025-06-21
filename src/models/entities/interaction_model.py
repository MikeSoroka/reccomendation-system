from base_entity import Base

from datetime import datetime, timezone
from sqlmodel import Field, SQLModel
from sqlmodel import UUID, DateTime, Integer, String, Text


class UserMovieAssociationModel(Base, table=True):
    __tablename__ = "interactionsTable"

    user_id: UUID = Field(foreign_key="usersTable.id", primary_key=True)
    movie_id: UUID = Field(foreign_key="moviesTable.id", primary_key=True)
    rating: int = Field(ge=1, le=10)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    dataset_id: int | None = Field(default=None)  # tmp solution to export data from the free dataset