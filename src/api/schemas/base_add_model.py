from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4

class BaseAddModel(SQLModel, table=False):
    id: UUID
