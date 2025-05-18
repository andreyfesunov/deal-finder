from dishka import FromDishka, Provider

from src.application.usecases.get_products_usecase import GetProductsUsecase
from src.application.usecases.get_categories_usecase import GetCategoriesUsecase
from src.domain.repositories.datastore_repository import DatastoreRepository


class UsecaseContainer(Provider):
    def provide_get_products_usecase(
        self, datastore_repository: FromDishka[DatastoreRepository]
    ) -> GetProductsUsecase:
        return GetProductsUsecase(datastore_repository)

    def provide_get_categories_usecase(
        self, datastore_repository: FromDishka[DatastoreRepository]
    ) -> GetCategoriesUsecase:
        return GetCategoriesUsecase(datastore_repository)
