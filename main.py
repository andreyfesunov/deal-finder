from dishka import make_async_container
from fastapi import FastAPI, Query
from dishka.integrations.fastapi import (
    FromDishka,
    FastapiProvider,
    setup_dishka,
)
from fastapi.concurrency import asynccontextmanager

from src.application.usecases.get_categories_usecase import GetCategoriesUsecase
from src.application.usecases.get_products_usecase import GetProductsUsecase
from src.di.repository_container import RepositoryContainer
from src.di.usecase_container import UsecaseContainer
from src.domain.models.category_model import CategoryModel
from src.domain.models.page_of_model import PageOfModel
from src.domain.models.product_model import ProductModel


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await app.state.dishka_container.close()


app = FastAPI(lifespan=lifespan)
container = make_async_container(
    RepositoryContainer(), UsecaseContainer(), FastapiProvider()
)
setup_dishka(app, container)


@app.get("/products")
async def get_products(
    get_products_usecase: FromDishka[GetProductsUsecase],
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100),
) -> PageOfModel[ProductModel]:
    return await get_products_usecase.execute(page, size)


@app.get("/categories")
async def get_categories(
    get_categories_usecase: FromDishka[GetCategoriesUsecase],
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100),
) -> PageOfModel[CategoryModel]:
    return await get_categories_usecase.execute(page, size)


@app.get("/ping")
def ping():
    return {"message": "pong"}
