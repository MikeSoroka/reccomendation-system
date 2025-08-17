from datetime import datetime, timezone
from os import times

from dependency_injector.wiring import inject, Provide

from config import PROJECT_ROOT
import os
import pandas as pd

from src.api.core.container import Container
from src.api.redis.redis_db import RedisDB
from src.api.schemas.batch.add_batch_model import AddBatchModel
from src.api.schemas.interactions.add_interaction_model import AddInteractionModel
from src.api.schemas.users.add_user_model import AddUserModel
from src.api.schemas.movies.add_movie_model import AddMovieModel
from uuid import uuid4

from src.api.services.interactions_service import InteractionsService
from src.api.services.movies_service import MoviesService
from src.api.services.users_service import UsersService

EXPORT_DATASET = True
EXPORT_EMBEDDING_IDS = True

class MovielensHelper:
    @staticmethod
    @inject
    async def export(
        location = os.path.join(PROJECT_ROOT, 'datasets', 'movielens_dataset'),
        interactions_service: InteractionsService = Provide[Container.interactions_service],
        movies_service: MoviesService = Provide[Container.movies_service],
        users_service: UsersService = Provide[Container.users_service],
        user_mappings_redis_session = Provide[Container.user_mappings_redis_session],
        movie_mappings_redis_session = Provide[Container.movie_mappings_redis_session],
    ):
        print("Reading movielens dataset...")
        ratings_df = pd.read_csv(os.path.join(location, "rating.csv"))
        movies_df = pd.read_csv(os.path.join(location, "movie.csv"))

        users = ratings_df['userId'].unique()
        movies = movies_df['movieId'].unique()

        print("Generating requests")
        user_id_to_uuid = dict(zip(users, [uuid4() for _ in users], ))

        movie_id_to_title = dict(zip(movies, movies_df['title'], ))
        movie_id_to_uuid = dict(zip(movies, [uuid4() for _ in movies], ))

        interaction_key_to_title = {}
        for _, row in ratings_df.iterrows():
            key = (row['userId'], row['movieId'])
            interaction_key_to_title[key] = (row['rating'], row['timestamp'])

        if EXPORT_DATASET:
            print("Generating requests...")
            users_request = AddBatchModel(
                batch=[AddUserModel(id=user_id_to_uuid[user_id]) for user_id in users]
            )
            movies_request = AddBatchModel(
                batch=[
                    AddMovieModel(id=movie_id_to_uuid[movie_id],
                                  title=movie_id_to_title[movie_id])
                    for movie_id in movies
                ]
            )
            interactions_request = AddBatchModel(
                batch=[
                    AddInteractionModel(
                        user_id=user_id_to_uuid[dict_row[0][0]],
                        movie_id=movie_id_to_uuid[dict_row[0][1]],
                        rating=int(dict_row[1][0] * 2),
                        created_at=datetime.strptime(dict_row[1][1], "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
                    )
                    for dict_row in interaction_key_to_title.items()
                ]
            )

            print("Writing to the database")
            try:
                await users_service.add_users(users_request)
                await movies_service.add_movies(movies_request)
                await interactions_service.add_interactions(interactions_request)
            except Exception as e:
                raise e
            
        if EXPORT_EMBEDDING_IDS:
            print("WRITING TO REDIS...")
            for index, value in enumerate(user_id_to_uuid.values()):
                await user_mappings_redis_session.set(str(value), str(index))
            for index, value in enumerate(movie_id_to_uuid.values()):
                await movie_mappings_redis_session.set(str(value), str(index))