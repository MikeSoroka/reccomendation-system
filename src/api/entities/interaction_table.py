from datetime import datetime, timezone

from sqlalchemy import Column, DateTime
from sqlmodel import Field, SQLModel
from uuid import UUID


class InteractionTable(SQLModel, table=True):
    __tablename__ = "interactionsTable"

    user_id: UUID = Field(foreign_key="usersTable.id", primary_key=True)
    movie_id: UUID = Field(foreign_key="moviesTable.id", primary_key=True)
    rating: int = Field(ge=1, le=10)
    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), nullable=False),
        default_factory=lambda: datetime.now(timezone.utc),
    )
