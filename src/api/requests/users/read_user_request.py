from src.api.models.entities.user_model import UserModel
from src.api.models.schemas.users.read_user_model import ReadUserModel
from src.api.requests.base_add_request import BaseAddRequest

from sqlmodel import Session


class ReadUserRequest(BaseAddRequest):
    @classmethod
    def submit(cls, model: ReadUserModel):
        with Session(cls.engine) as session:
            try:
                return session.get(UserModel, model.id)
            except Exception as e:
                session.rollback()
                raise