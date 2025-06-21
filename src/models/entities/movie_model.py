from base_entity import Base

from sqlmodel import DateTime, ForeignKey, Integer, Text, String, UUID
from sqlmodel import Field
import uuid

class MovieModel(Base):
    __tablename__ = "moviesTable"

    id: UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    title: str = Field(max_length=100, index=True)
    dataset_id: int | None # tmp solution to export data from the free dataset
