from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4

class BaseReadModel(SQLModel, table=False):
    id: UUID