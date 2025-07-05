from src.api.models.entities.base_entity import Base

from sqlmodel import DateTime, ForeignKey, Integer, Text, String
from sqlmodel import Field
from uuid import UUID, uuid4

class UserModel(Base, table=True):
    __tablename__ = "usersTable"

    #TODO: username, password and other stuff to be added later
