from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4
from src.api.models.schemas.base_add_model import BaseAddModel

class AddUserModel(BaseAddModel, table=False):
    pass