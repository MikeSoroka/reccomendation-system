from typing import Sequence

import pandas as pd
import torch
from dependency_injector.wiring import Provide, inject
from redis import Redis
from torch.utils.data import Dataset

from src.api.core.container import Container
from src.api.entities.interaction_table import InteractionTable
from src.api.services.interactions_service import InteractionsService


class MoviesDataset(Dataset):
    def __init__(
            self,
            redis_user_mappings_session: Redis,
            redis_movie_mappings_session: Redis,
            interactions: Sequence[InteractionTable] | None = None
    ):
        super().__init__()
        print("Creatin interactions...")
        self.interactions = interactions
        print("Creating redis connections...")
        self.redis_user_mappings = redis_user_mappings_session
        self.redis_movie_mappings = redis_movie_mappings_session

    @classmethod
    @inject
    async def create(
            cls,
            interactions_service = Provide[Container.interactions_service],
            redis_user_mappings = Provide[Container.users_mappings_redis_session],
            redis_movie_mappings = Provide[Container.movies_mappings_redis_session]
    ):

        return cls(redis_user_mappings, redis_movie_mappings, interactions)

    def __getitem__(self, index):
        return (
            self.redis_user_mappings.get(str(self.interactions[index].user_id)),
            self.redis_movie_mappings.get(str(self.interactions[index].movie_id)),
            self.interactions[index].rating,
        )

    def __len__(self):
        return len(self.interactions)
