from src.domain.models.page_of_model import PageOfModel
from src.domain.models.product_model import ProductModel
from src.domain.repositories.datastore_repository import DatastoreRepository


class GetProductsUsecase:
    def __init__(self, datastore_repository: DatastoreRepository):
        self.__datastore_repository = datastore_repository

    async def execute(self, page: int, size: int) -> PageOfModel[ProductModel]:
        return await self.__datastore_repository.get_products(page, size)
