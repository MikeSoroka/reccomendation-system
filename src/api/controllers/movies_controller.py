from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from src.api.core.container import Container
from src.api.schemas.movies.add_movie_model import AddMovieModel
from src.api.schemas.movies.read_movie_model import ReadMovieModel
from uuid import UUID

from src.api.services.movies_service import MoviesService

router = APIRouter()

@router.get("/movies/{movie_id}")
@inject
async def read_movie(
    movie_id: UUID,
    movies_service: MoviesService = Depends(Provide[Container.movies_service]),
):
    model = ReadMovieModel(id=movie_id)
    return await movies_service.get_movie(model)

@router.post("/movies/movie_id")
@inject
async def add_item(
     movie_id: UUID,
    title: str,
    movies_service: MoviesService = Depends(Provide[Container.movies_service]),
):
    model = AddMovieModel(id=movie_id, title=title)
    return await movies_service.add_movie(model)