from src.api.models.entities.user_model import UserModel
from src.api.models.schemas.users.add_user_model import AddUserModel
from src.api.requests.base_add_request import BaseAddRequest


from sqlmodel import create_engine, Session
from dotenv import load_dotenv
import os

class AddUsersRequest(BaseAddRequest):
    @classmethod
    def submit(cls, models: list[AddUserModel]):
        with Session(cls.engine) as session:
            try:
                for model in models:
                    session.add(
                        UserModel(
                            id=model.id,
                        )
                    )
                session.commit()
            except Exception as e:
                session.rollback()
                raise