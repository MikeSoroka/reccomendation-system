from pydantic import BaseModel
from uuid import UUID

class ReadMovieModel(BaseModel):
    id: UUID