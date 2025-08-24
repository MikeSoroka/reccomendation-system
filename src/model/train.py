import asyncio

import torch
from dependency_injector.wiring import Provide, inject
from redis import Redis
from torch.nn import MSELoss
from torch.optim import AdamW
from torch.utils.data import DataLoader
import numpy as np
from tqdm import tqdm

from src.api.core.container import Container
from src.api.redis.repositories.recommender_repository import MoviesDataset
from src.model.recommender import Recommender

class RecommenderTrainer:
    def __init__(
        self,
        dataset: MoviesDataset,
        n_users: int,
        n_movies: int,
        batch_size: int,
        learning_rate: float
    ):
        print("Initializing RecommenderTrainer")
        self.recommender = Recommender(n_users=n_users, n_movies=n_movies)

        self.optimiser = AdamW(self.recommender.parameters(), lr=learning_rate)
        self.loss_fn = MSELoss()

        self.epoch_train_losses = []
        self.train_rmse_list = []

        print("DataLoader")
        self.TrainLoader = DataLoader(dataset=dataset, batch_size=batch_size, num_workers=1, shuffle=True)
        self.epoch_train_losses = []

    def train(self, epochs):
        print("Training...")
        for i in range(epochs):
            self.recommender.train()
            train_losses = np.array([])
            for X, y in tqdm(self.TrainLoader):
                # X_user, X_movie = X[0].to(device=DEVICE, dtype=torch.long), X[1].to(device=DEVICE, dtype=torch.long)
                loss = self.loss_fn(self.recommender(X), y)
                train_losses = np.append(train_losses, loss.item())
                self.optimiser.zero_grad()
                loss.backward()
                self.optimiser.step()

            print("Epoch {}/{}, Loss: {:.4f}".format(i+1, epochs, train_losses[-1]))

            print("Avg epoch losses", np.average(train_losses))
            print("Min epoch loss", np.min(train_losses))

            torch.save(self.recommender.state_dict(), "/kaggle/working/last_model.pt")
            self.epoch_train_losses.append(np.average(train_losses))

            with torch.no_grad():
                if loss < BEST_ACC:
                    print("NEW BEST LOSS:", loss)
                    BEST_ACC = loss
                    torch.save(self.recommender.state_dict(), "working/best_model.pt")

    # def get_stats(self):
    #     model = MatrixFactorization(len(dataset.users) + 1, len(dataset.movies) + 1)
    #     model.load_state_dict(torch.load("/kaggle/working/last_model.pt", weights_only=True))
    #     model.eval()


if __name__ == "__main__":
    print("Creating container...")
    container = Container()
    container.wire()

    dataset = MoviesDataset()
    n_users, n_movies = dataset.get_dimensions()


    def train():
        print("Creating a trainer...")

        trainer =  RecommenderTrainer(
            dataset=dataset,
            n_users=n_users,
            n_movies=n_movies,
            batch_size=256,
            learning_rate=0.1
        )

        print("Training...")
        trainer.train(epochs=100)
    train()