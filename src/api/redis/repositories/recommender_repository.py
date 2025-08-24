import ast
import asyncio
from typing import Sequence
from uuid import UUID

import anyio
import numpy as np
import pandas as pd
import torch
from dependency_injector.wiring import Provide, inject
from redis import Redis
from torch.utils.data import Dataset

from src.api.core.container import Container
from src.api.entities.interaction_table import InteractionTable
from src.api.redis.redis_utils import RedisUtils, ConversionType
from src.api.schemas.interactions.read_interaction_model import ReadInteractionModel
from src.api.services.interactions_service import InteractionsService


class MoviesDataset(Dataset):
    def __init__(self):
        super().__init__()

    @inject
    def __getitem__(
            self,
            index: int,
            interactions_service=Provide[Container.interactions_service],
            redis_users_mappings=Provide[Container.users_mappings_redis_sync_session],
            redis_movies_mappings=Provide[Container.movies_mappings_redis_sync_session],
            redis_interactions_mappings=Provide[Container.interactions_mappings_redis_sync_session]
    ):
        user_id_str, movie_id_str, interaction_str = RedisUtils.parse_record(redis_interactions_mappings.get(str(index)), ConversionType.MIXED_TUPLE)
        user_id = user_id_str[6:-2]
        movie_id = movie_id_str[7:-2]

        interaction = np.float32(interaction_str)
        user_mapping = int(redis_users_mappings.get(str(user_id)))
        movie_mapping = int(redis_movies_mappings.get(str(movie_id)))

        return (user_mapping, movie_mapping), interaction

    @inject
    def __len__(
        self,
        redis_interactions_mappings=Provide[Container.interactions_mappings_redis_sync_session]
    ):
        return redis_interactions_mappings.dbsize()

    @inject
    def get_dimensions(
        self,
        redis_users_mappings=Provide[Container.users_mappings_redis_sync_session],
        redis_movies_mappings=Provide[Container.movies_mappings_redis_sync_session],
    ):
        print("AAAAAAAAAAAAAAAAAAA", redis_users_mappings.dbsize())
        print("BBBBBBBBBBBBBBBBBBBBB", redis_movies_mappings.dbsize())
        return redis_users_mappings.dbsize(), redis_movies_mappings.dbsize()
