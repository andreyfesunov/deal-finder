from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    CATEGORIES_CSV_FILE_PATH: str
    PRODUCTS_CSV_FILE_PATH: str

    model_config = SettingsConfigDict(env_file=".env")


config = Config()
