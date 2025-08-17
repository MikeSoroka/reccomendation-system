import pandas as pd
import torch
from redis import Redis
from torch.utils.data import Dataset

from src.api.services.interactions_service import InteractionsService


class MoviesDataset(Dataset):
    def __init__(
            self,
            interactions_service: InteractionsService,
            redis_user_mappings_session: Redis,
            redis_movie_mappings_session: Redis):
        super().__init__()
        self.interactions = interactions_service.get_page() # TODO: maybe, update it so interactions are not stored in RAM(when too much)
        self.redis_user_mappings = redis_user_mappings_session
        self.redis_movie_mappings = redis_movie_mappings_session

    def __getitem__(self, index):
        return (
            self.redis_user_mappings.get(self.interactions[index].user_id),
            self.redis_movie_mappings.get(self.interactions[index].movie_id),
            self.interactions[index].rating,
        )

    def __len__(self):
        return len(self.interactions)
