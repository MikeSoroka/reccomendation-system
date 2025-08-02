from uuid import UUID

from pydantic import BaseModel

class ReadUserModel(BaseModel):
    id: UUID