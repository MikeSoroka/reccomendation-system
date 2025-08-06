from typing import Iterable, TypeVar

from pydantic import BaseModel

T = TypeVar("T")
class AddBatchModel(BaseModel):
    batch: list[T]