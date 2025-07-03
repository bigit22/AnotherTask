from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MODERATION_API_KEY: str
    MODERATION_API_URL: str
    MAX_IMAGE_SIZE_MB: int = 5

    class Config:
        env_file = '.env'


settings = Settings()
