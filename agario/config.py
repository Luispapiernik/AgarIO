from os.path import exists
from typing import Tuple

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    # window settings
    screen_width: int = Field(None, env="SCREEN_WIDTH")
    screen_height: int = Field(None, env="SCREEN_HEIGHT")
    title: str = Field(None, env="TITLE")
    icon_path: str = Field(None, env="ICON_PATH")

    # map settings
    background_color: Tuple[int, int, int] = Field(None, env="BACKGROUND_COLOR")

    # player settings
    initial_radius: float = Field(None, env="INITIAL_RADIUS")
    player_color: Tuple[int, int, int] = Field(None, env="PLAYER_COLOR")

    class Config:
        env_file = (
            "user_settings.env" if exists("user_settings.env") else "settings.env"
        )
        env_file_encoding = "utf-8"


settings = Settings()
