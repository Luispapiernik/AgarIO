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
    width: int = Field(None, env="WIDTH")
    height: int = Field(None, env="HEIGHT")
    grid_length: int = Field(None, env="GRID_LENGTH")
    grid_line_width: int = Field(None, env="GRID_LINE_WIDTH")
    background_color: Tuple[int, int, int] = Field(None, env="BACKGROUND_COLOR")
    grid_color: Tuple[int, int, int] = Field(None, env="GRID_COLOR")

    # player settings
    player_initial_radius: float = Field(None, env="PLAYER_INITIAL_RADIUS")
    player_color: Tuple[int, int, int] = Field(None, env="PLAYER_COLOR")

    # food settings
    food_initial_radius: float = Field(None, env="FOOD_INITIAL_RADIUS")
    food_amount: int = Field(None, env="FOOD_AMOUNT")

    class Config:
        env_file = (
            "user_settings.env" if exists("user_settings.env") else "settings.env"
        )
        env_file_encoding = "utf-8"


settings = Settings()
