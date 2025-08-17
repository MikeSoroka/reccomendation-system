import torch
from torch.nn import Module, Embedding


class Recommender(Module):
    def __init__(self, n_users, n_movies, n_emb=20):
        super().__init__()
        self.users_embedding = Embedding(n_users, n_emb)
        self.movies_embedding = Embedding(n_movies, n_emb)

    def forward(self, users, movies):
        raw_scores = (self.users_embedding(users) * self.movies_embedding(movies)).sum(1)
        return 0.5 + 4.5 * torch.sigmoid(raw_scores)