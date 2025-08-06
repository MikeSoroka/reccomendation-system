from src.api.db.repositories.movies_repository import MoviesRepository
from src.api.entities.movie_table import MovieTable
from src.api.schemas.batch.add_batch_model import AddBatchModel
from src.api.schemas.movies.add_movie_model import AddMovieModel
from src.api.schemas.movies.read_movie_model import ReadMovieModel


class MoviesService:
    def __init__(self, repository: MoviesRepository):
        self.repository = repository

    async def get_movie(self, request: ReadMovieModel) -> MovieTable | None:
        return await self.repository.get_movie(request)

    async def add_movie(self, request: AddMovieModel) ->  None:
        return await self.repository.add_movie(request)

    async def add_movies(self, request: AddBatchModel) ->  None:
        return await self.repository.add_movies(request)