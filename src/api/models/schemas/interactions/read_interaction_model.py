from sqlmodel import SQLModel
from uuid import UUID, uuid4

class ReadInteractionModel(SQLModel, table=False):
    user_id: UUID
    movie_id: UUID