from src.api.models.entities.movie_model import MovieModel
from src.api.models.schemas.movies.read_movie_model import ReadMovieModel
from src.api.requests.base_add_request import BaseAddRequest

from sqlmodel import Session


class ReadMovieRequest(BaseAddRequest):
    @classmethod
    def submit(cls, model: ReadMovieModel):
        with Session(cls.engine) as session:
            try:
                return session.get(MovieModel, model.id)
            except Exception as e:
                session.rollback()
                raise