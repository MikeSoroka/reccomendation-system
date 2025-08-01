from sqlmodel import Field, SQLModel
from uuid import UUID, uuid4

class MovieTable(SQLModel, table=True):
    __tablename__ = "moviesTable"

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    title: str = Field(max_length=200, index=True)
