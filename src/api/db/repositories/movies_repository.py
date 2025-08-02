from src.api.db.session import AsyncSession
from src.api.entities.movie_table import MovieTable
from src.api.schemas.movies.add_movie_model import AddMovieModel
from src.api.schemas.movies.read_movie_model import ReadMovieModel


class MoviesRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_movie(self, request: ReadMovieModel) -> MovieTable | None:
        return await self.session.get(MovieTable, request.id)

    async def add_movie  (self, request: AddMovieModel) ->  None:
        movie = MovieTable(
            id = request.id,
            title = request.title
        )
        self.session.add(movie)