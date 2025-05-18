from dishka import Provider, Scope, provide
from config import config

from src.domain.repositories.datastore_repository import DatastoreRepository
from src.infrastructure.repositories.datastore_repository_impl import (
    DatastoreRepositoryImpl,
)


class RepositoryContainer(Provider):
    @provide(scope=Scope.APP)
    def provide_datastore_repository(self) -> DatastoreRepository:
        async def get_file_from_storage(path: str) -> bytes:
            with open(path, "rb") as file:
                return file.read()

        return DatastoreRepositoryImpl(
            categories_csv_file_path=config.CATEGORIES_CSV_FILE_PATH,
            products_csv_file_path=config.PRODUCTS_CSV_FILE_PATH,
            get_file_from_storage=get_file_from_storage,
        )
