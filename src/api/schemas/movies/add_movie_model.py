from uuid import UUID

from pydantic import BaseModel, Field

class AddMovieModel(BaseModel):
    id: UUID
    title: str = Field(max_length=200)
