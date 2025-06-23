from src.api.models.entities.base_entity import Base

from sqlmodel import DateTime, ForeignKey, Integer, Text, String
from sqlmodel import Field
from uuid import UUID, uuid4

class MovieModel(Base, table=True):
    __tablename__ = "moviesTable"

    title: str = Field(max_length=100, index=True)
    dataset_id: int | None # tmp solution to export data from the free dataset
