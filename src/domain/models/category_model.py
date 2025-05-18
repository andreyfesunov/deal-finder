class CategoryModel:
    def __init__(self, main_category: str, sub_category: str):
        self.__main_category = main_category
        self.__sub_category = sub_category

    @property
    def main_category(self) -> str:
        return self.__main_category

    @property
    def sub_category(self) -> str:
        return self.__sub_category
