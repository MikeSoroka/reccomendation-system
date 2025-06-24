from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4
from src.api.models.schemas.base_add_model import BaseAddModel

class AddMovieModel(BaseAddModel, table=False):
    title: str = Field(max_length=100, default="", index=True)
