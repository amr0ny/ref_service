from pydantic_settings import BaseSettings, SettingsConfigDict
from logger import Logger


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix='')
    postgres_db: str
    postgres_user: str
    postgres_host: str
    postgres_port: int
    postgres_password: str
    log_path: str
    log_level: str

settings = Settings(_env_file='.env', _env_file_encoding='utf-8')
logger = Logger(settings.log_path, settings.log_level)