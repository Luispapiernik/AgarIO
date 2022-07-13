from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    width: int = Field(None, env="WIDTH")
    height: int = Field(None, env="HEIGHT")
    title: str = Field(None, env="TITLE")

    class Config:
        env_file = "settings.env"
        env_file_encoding = "utf-8"


settings = Settings()
