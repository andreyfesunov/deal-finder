from dishka import make_async_container
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from dishka.integrations.fastapi import (
    FromDishka,
    FastapiProvider,
    setup_dishka,
    inject,
)

from src.application.usecases.get_categories_usecase import GetCategoriesUsecase
from src.application.usecases.get_products_usecase import GetProductsUsecase
from src.di.repository_container import RepositoryContainer
from src.di.usecase_container import UsecaseContainer
from src.domain.models.category_model import CategoryModel
from src.domain.models.page_of_model import PageOfModel
from src.domain.models.product_model import ProductModel


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

container = make_async_container(
    RepositoryContainer(), UsecaseContainer(), FastapiProvider()
)
setup_dishka(container, app)


@app.get("/products")
@inject
async def get_products(
    get_products_usecase: FromDishka[GetProductsUsecase],
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100),
) -> PageOfModel[ProductModel]:
    return await get_products_usecase.execute(page, size)


@app.get("/categories")
@inject
async def get_categories(
    get_categories_usecase: FromDishka[GetCategoriesUsecase],
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100),
) -> PageOfModel[CategoryModel]:
    return await get_categories_usecase.execute(page, size)


@app.get("/ping")
def ping():
    return {"message": "pong"}
