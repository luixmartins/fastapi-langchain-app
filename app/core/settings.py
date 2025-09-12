from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    MISTRAL_API_KEY: str
    MODEL_NAME: str

    class Config:
        env_file = "app/.env"

settings = Settings()