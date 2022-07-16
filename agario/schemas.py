from enum import IntEnum
from typing import Tuple

RGB = Tuple[int, int, int]


class SCENES(IntEnum):
    TITLE = 0
    SETTINGS = 1
    GAME = 2
    IN_GAME_SETTINGS = 3
    PAUSE = 4
    CREDITS = 5
