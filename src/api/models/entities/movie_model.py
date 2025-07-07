from src.api.models.entities.base_entity import Base

from sqlmodel import DateTime, ForeignKey, Integer, Text, String
from sqlmodel import Field
from uuid import UUID, uuid4

class MovieModel(Base, table=True):
    __tablename__ = "moviesTable"

    title: str = Field(max_length=200, index=True)
