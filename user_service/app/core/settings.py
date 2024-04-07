from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()


class DBSetting(BaseSettings):
    DB_POSTGRES_HOST: str = os.environ.get("POSTGRES_HOST")
    DB_POSTGRES_PORT: int = os.environ.get("POSTGRES_PORT")
    DB_POSTGRES_USERNAME: str = os.environ.get("POSTGRES_USERNAME")
    DB_POSTGRES_PASSWORD: str = os.environ.get("POSTGRES_PASSWORD")
    DB_POSTGRESQL_DATABASE: str = os.environ.get("POSTGRESQL_DATABASE")


class DBTestSettings(BaseSettings):
    DB_TEST_POSTGRES_HOST: str = os.environ.get("TEST_POSTGRES_HOST")
    DB_TEST_POSTGRES_PORT: int = os.environ.get("TEST_POSTGRES_PORT")
    DB_TEST_POSTGRES_USERNAME: str = os.environ.get("TEST_POSTGRES_USERNAME")
    DB_TEST_POSTGRES_PASSWORD: str = os.environ.get("TEST_POSTGRES_PASSWORD")
    DB_TEST_POSTGRESQL_DATABASE: str = os.environ.get("TEST_POSTGRESQL_DATABASE")


db_settings = DBSetting()
db_test_settings = DBTestSettings()


class DBURI(BaseSettings):
    DB_URI: str = f"postgresql+asyncpg://{db_settings.DB_POSTGRES_USERNAME}:{db_settings.DB_POSTGRES_PASSWORD}@{db_settings.DB_POSTGRES_HOST}:{db_settings.DB_POSTGRES_PORT}/{db_settings.DB_POSTGRESQL_DATABASE}"
    DB_TEST_URI: str = f"postgresql+asyncpg://{db_test_settings.DB_TEST_POSTGRES_USERNAME}:{db_test_settings.DB_TEST_POSTGRES_PASSWORD}@{db_test_settings.DB_TEST_POSTGRES_HOST}:{db_test_settings.DB_TEST_POSTGRES_PORT}/{db_test_settings.DB_TEST_POSTGRESQL_DATABASE}"


db_uri = DBURI()
