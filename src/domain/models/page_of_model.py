from typing import Generic, TypeVar

T = TypeVar("T")


class PageOfModel(Generic[T]):
    def __init__(self, items: list[T], total: int, page: int, size: int):
        self.__items = items
        self.__total = total
        self.__page = page
        self.__size = size

    @property
    def items(self) -> list[T]:
        return self.__items

    @property
    def total(self) -> int:
        return self.__total

    @property
    def page(self) -> int:
        return self.__page

    @property
    def size(self) -> int:
        return self.__size
