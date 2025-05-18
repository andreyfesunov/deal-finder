from src.domain.models.category_model import CategoryModel
from src.domain.models.page_of_model import PageOfModel
from src.domain.repositories.datastore_repository import DatastoreRepository


class GetCategoriesUsecase:
    def __init__(self, datastore_repository: DatastoreRepository):
        self.__datastore_repository = datastore_repository

    async def execute(self, page: int, size: int) -> PageOfModel[CategoryModel]:
        return await self.__datastore_repository.get_categories(page, size)
