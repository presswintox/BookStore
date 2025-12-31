import os

from pydantic_settings import BaseSettings

# from src.core.logger import LOGGING


class Settings(BaseSettings):
    # Применяем настройки логирования
    # logging_config.dictConfig(LOGGING)

    # Название проекта. Используется в Swagger-документации
    PROJECT_NAME: str = "BookStore"

    # Корень проекта
    BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    class Config:
        env_file = ".env"


settings = Settings()
