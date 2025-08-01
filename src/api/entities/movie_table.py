from sqlmodel import Field
from uuid import UUID, uuid4

class MovieTable(table=True):
    __tablename__ = "moviesTable"

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    title: str = Field(max_length=200, index=True)
