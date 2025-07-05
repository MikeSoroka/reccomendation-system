from src.api.models.entities.movie_model import MovieModel
from src.api.models.schemas.movies.add_movie_model import AddMovieModel
from src.api.requests.base_add_request import BaseAddRequest


from sqlmodel import create_engine, Session
from dotenv import load_dotenv
import os

class AddMoviesRequest(BaseAddRequest):
    @classmethod
    def submit(cls, models: list[AddMovieModel]):
        with Session(cls.engine) as session:
            try:
                for model in models:
                    session.add(
                        MovieModel(
                            id=model.id,
                            title=model.title,
                        )
                    )
                session.commit()
            except Exception as e:
                session.rollback()
                raise