import csv
from io import StringIO
from typing import Awaitable, Callable
from src.domain.models.category_model import CategoryModel
from src.domain.models.page_of_model import PageOfModel
from src.domain.models.product_model import ProductModel
from src.domain.repositories.datastore_repository import DatastoreRepository


class DatastoreRepositoryImpl(DatastoreRepository):
    def __init__(
        self,
        categories_csv_file_path: str,
        products_csv_file_path: str,
        get_file_from_storage: Callable[[str], Awaitable[bytes]],
    ):
        self.__categories_csv_file_path = categories_csv_file_path
        self.__products_csv_file_path = products_csv_file_path
        self.__get_file_from_storage = get_file_from_storage

    async def get_products(self, page: int, size: int) -> PageOfModel[ProductModel]:
        file = await self.__get_file_from_storage(self.__products_csv_file_path)

        csv_str = file.decode("utf-8")
        csv_file = StringIO(csv_str)
        reader = csv.DictReader(csv_file)

        all_rows = list(reader)
        total = len(all_rows)

        start_idx = (page - 1) * size
        end_idx = start_idx + size

        paginated_rows = all_rows[start_idx:end_idx]
        products = [
            ProductModel(
                name=row["Название товара"],
                sub_category=row["Подкатегория 2"],
                m_video_link=row["М-видео"],
                m_video_price=float(row["Цена М-видео"]),
                eldorado_link=row["Эльдорадо"],
                eldorado_price=float(row["Цена Эльдорадо"]),
                dns_link=row["ДНС"],
                dns_price=float(row["Цена ДНС"]),
                citylink_link=row["Ситилинк"],
                citylink_price=float(row["Цена Ситилинк"]),
                yandex_link=row["Яндекс Маркет"],
                yandex_price=float(row["Цена Яндекс Маркет"]),
            )
            for row in paginated_rows
        ]

        return PageOfModel(items=products, page=page, size=size, total=total)

    async def get_categories(self, page: int, size: int) -> PageOfModel[CategoryModel]:
        file = await self.__get_file_from_storage(self.__categories_csv_file_path)

        csv_str = file.decode("utf-8")
        csv_file = StringIO(csv_str)
        reader = csv.DictReader(csv_file)

        all_rows = list(reader)
        total = len(all_rows)

        start_idx = (page - 1) * size
        end_idx = start_idx + size

        paginated_rows = all_rows[start_idx:end_idx]
        categories = [
            CategoryModel(
                main_category=row["Категория"],
                sub_category=row["Подкатегория"],
            )
            for row in paginated_rows
        ]

        return PageOfModel(items=categories, page=page, size=size, total=total)
