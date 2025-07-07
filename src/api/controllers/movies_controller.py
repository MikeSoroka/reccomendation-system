from fastapi import APIRouter

from src.api.requests.movies.read_movie_request import ReadMovieRequest
from src.api.requests.movies.add_movies_request import AddMoviesRequest
from src.api.models.schemas.movies.add_movie_model import AddMovieModel
from src.api.models.schemas.movies.read_movie_model import ReadMovieModel
from uuid import UUID

router = APIRouter()

@router.get("/movies/{movie_id}")
async def read_item(movie_id: UUID):
    model = ReadMovieModel(id=movie_id)
    return ReadMovieRequest.submit(model)

@router.post("/movies/movie_id")
async def add_item(movie_id: UUID, title: str):
    model = AddMovieModel(id=movie_id, title=title)
    return AddMoviesRequest.submit([model])