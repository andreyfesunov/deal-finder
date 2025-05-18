from dishka import FromDishka, Provider, Scope, provide

from src.application.usecases.get_products_usecase import GetProductsUsecase
from src.application.usecases.get_categories_usecase import GetCategoriesUsecase
from src.domain.repositories.datastore_repository import DatastoreRepository


class UsecaseContainer(Provider):
    @provide(scope=Scope.APP)
    def provide_get_products_usecase(
        self, datastore_repository: FromDishka[DatastoreRepository]
    ) -> GetProductsUsecase:
        return GetProductsUsecase(datastore_repository)

    @provide(scope=Scope.APP)
    def provide_get_categories_usecase(
        self, datastore_repository: FromDishka[DatastoreRepository]
    ) -> GetCategoriesUsecase:
        return GetCategoriesUsecase(datastore_repository)
