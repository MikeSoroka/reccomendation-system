from sqlmodel import Field
from uuid import UUID, uuid4

class UserTable(table=True):
    __tablename__ = "usersTable"
    id: UUID = Field(default_factory=uuid4, primary_key=True)

    #TODO: username, password and other stuff to be added later
