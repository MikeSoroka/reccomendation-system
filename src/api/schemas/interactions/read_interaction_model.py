from pydantic import BaseModel
from uuid import UUID

class ReadInteractionModel(BaseModel):
    user_id: UUID
    movie_id: UUID