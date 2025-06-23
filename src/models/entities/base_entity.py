from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4


class Base(SQLModel, table=False):
    id: UUID = Field(default_factory=uuid4, primary_key=True)