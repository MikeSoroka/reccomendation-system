from config import PROJECT_ROOT
import os
import pandas as pd
from src.api.models

class Helper:
    def __init__(self, location = os.path.join(PROJECT_ROOT, 'datasets', 'movielens_dataset')):
        ratings_df = pd.read_csv("ratings.csv")
        self.users = ratings_df["userId"].unique()
        self.movies = ratings_df["movieId"].unique()

        self.user2id = {y: x for x, y in enumerate(self.users)}
        self.movie2id = {y: x for x, y in enumerate(self.movies)}

        self.id2user = {x: y for x, y in enumerate(self.users)}
        self.id2movie = {x: y for x, y in enumerate(self.movies)}
