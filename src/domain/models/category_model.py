from pydantic import BaseModel


class CategoryModel(BaseModel):
    main_category: str
    sub_category: str
