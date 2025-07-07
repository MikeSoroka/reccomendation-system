from src.api.models.entities.interaction_model import InteractionModel
from src.api.models.schemas.interactions.read_interaction_model import ReadInteractionModel
from src.api.requests.base_add_request import BaseAddRequest

from sqlmodel import Session


class ReadInteractionRequest(BaseAddRequest):
    @classmethod
    def submit(cls, model: ReadInteractionModel):
        with Session(cls.engine) as session:
            try:
                return session.get(InteractionModel, (model.user_id, model.movie_id))
            except Exception as e:
                session.rollback()
                raise