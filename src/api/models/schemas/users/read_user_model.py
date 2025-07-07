from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4
from src.api.models.schemas.base_read_model import BaseReadModel

class ReadUserModel(BaseReadModel, table=False):
    pass