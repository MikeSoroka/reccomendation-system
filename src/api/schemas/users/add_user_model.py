from pydantic import BaseModel
from uuid import UUID

class AddUserModel(BaseModel):
    id: UUID