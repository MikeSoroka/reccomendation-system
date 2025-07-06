from src.api.models.entities.movie_model import MovieModel
from src.api.models.schemas.movies.add_movie_model import AddMovieModel
from src.api.models.schemas.recommendations.read_recommendation_model import ReadRecommendationModel
from src.model.recommendation_model_client import MovieReccomender


from sqlmodel import create_engine, Session
from dotenv import load_dotenv
import os

class ReadRecommendationRequest():
    @classmethod
    def submit(cls, model: ReadRecommendationModel):
        recommender = MovieReccomender("tmp_dummy_weights")
        return recommender.user_reccomendation(model.user_id, model.limit)
