from typing import Generic, TypeVar
from pydantic import BaseModel

T = TypeVar("T")


class PageOfModel(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int
    size: int
