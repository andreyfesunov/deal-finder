from abc import ABC, abstractmethod

from src.domain.models.category_model import CategoryModel
from src.domain.models.page_of_model import PageOfModel
from src.domain.models.product_model import ProductModel


class DatastoreRepository(ABC):
    @abstractmethod
    async def get_products(self, page: int, size: int) -> PageOfModel[ProductModel]:
        pass

    @abstractmethod
    async def get_categories(self, page: int, size: int) -> PageOfModel[CategoryModel]:
        pass
