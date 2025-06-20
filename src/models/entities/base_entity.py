from uuid import UUID, uuid4
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    id: UUID = uuid4()
    name: str