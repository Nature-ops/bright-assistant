from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Bright Assistant"
    VERSION: str = "0.2.0"
    

    class Config:
        env_file = ".env"


settings = Settings()