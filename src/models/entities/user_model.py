from src.models.entities.base_entity import Base

from sqlmodel import DateTime, ForeignKey, Integer, Text, String
from sqlmodel import Field
from uuid import UUID, uuid4

class UserModel(Base, table=True):
    __tablename__ = "usersTable"

    dataset_id: int | None # tmp solution to export data from the free dataset
    #TODO: username, password and other stuff to be added later