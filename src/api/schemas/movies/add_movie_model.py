from pydantic import BaseModel, Field

class AddMovieModel(BaseModel):
    title: str = Field(max_length=200)
