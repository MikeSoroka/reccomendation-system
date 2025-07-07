from src.api.models.entities.interaction_model import InteractionModel
from src.api.models.schemas.interactions.add_interaction_model import AddInteractionModel
from src.api.requests.base_add_request import BaseAddRequest


from sqlmodel import create_engine, Session
from dotenv import load_dotenv
import os

class AddInteractionsRequest(BaseAddRequest):
    @classmethod
    def submit(cls, models: list[AddInteractionModel]):
        with Session(cls.engine) as session:
            try:
                for model in models:
                    session.add(
                        InteractionModel(
                            user_id=model.user_id,
                            movie_id=model.movie_id,
                             rating=model.rating,
                            **({} if model.created_at is None else {"created_at": model.created_at}),
                        )
                    )
                session.commit()
            except Exception as e:
                session.rollback()
                raise