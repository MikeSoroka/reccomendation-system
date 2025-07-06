from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4

class ReadRecommendationModel(SQLModel, table=False):
    user_id: UUID
    limit: int