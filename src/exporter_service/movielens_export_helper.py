from config import PROJECT_ROOT
import os
import pandas as pd
from src.api.models.schemas.interactions.add_interaction_model import AddInteractionModel
from src.api.models.schemas.users.add_user_model import AddUserModel
from src.api.models.schemas.movies.add_movie_model import AddMovieModel
from src.api.requests.interactions.add_interactions_request import AddInteractionsRequest
from src.api.requests.movies.add_movies_request import AddMoviesRequest
from src.api.requests.users.add_users_request import AddUsersRequest
from uuid import uuid4

class MovielensHelper:
    @classmethod
    def export(cls, location = os.path.join(PROJECT_ROOT, 'datasets', 'movielens_dataset')):
        print("Reading movielens dataset...")
        ratings_df = pd.read_csv(os.path.join(location, "rating.csv"))
        movies_df = pd.read_csv(os.path.join(location, "movie.csv"))

        users = ratings_df['userId'].unique()
        movies = ratings_df['movieId'].unique()

        print("Generating requests")
        user_id_to_uuid = dict(zip(users, [uuid4() for user in users], ))
        users_request = [AddUserModel(id = user_id_to_uuid[user_id]) for user_id in users]

        movie_id_to_title = dict(zip(movies, movies_df['title'], ))
        movie_id_to_uuid = dict(zip(movies, [uuid4() for movie in movies], ))
        movies_request = [
            AddMovieModel(id=movie_id_to_uuid[movie_id],
                        title=movie_id_to_title[movie_id])
            for movie_id in movies
        ]

        interaction_key_to_title = {}
        for _, row in ratings_df.iterrows():
            key = (row['userId'], row['movieId'])
            interaction_key_to_title[key] = row['rating']

        interactions_request = [
            AddInteractionModel(user_id=user_id_to_uuid[dict_row[0][0]],
                                movie_id=movie_id_to_uuid[dict_row[0][1]],
                                rating=int(dict_row[1] * 2))
            for dict_row in interaction_key_to_title.items()]

        print("Writing to the database")
        try:
            AddUsersRequest.submit(users_request)
            AddMoviesRequest.submit(movies_request)
            AddInteractionsRequest.submit(interactions_request)
        except Exception as e:
            raise e