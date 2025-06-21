from sqlalchemy import UUID
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    id: UUID