from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_HOSTNAME: str
    DATABASE_PASSWORD: str
    DATABASE_PORT: str
    DATABASE_NAME: str
    DATABASE_USERNAME: str
    
    class Config:
        env_file = ".env"


settings = Settings()