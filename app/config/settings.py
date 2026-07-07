from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Bright Assistant"
    VERSION: str = "0.2.0"
    DEBUG: bool = True

    OLLAMA_MODEL: str = "llama3.1:8b"

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()