from abc import ABC, abstractmethod
from typing import List

import pygame as pg

from agario.schemas import SCENES


class Scene(ABC):
    @abstractmethod
    def update(self, events) -> SCENES:
        pass

    @abstractmethod
    def draw(self, screen) -> List[pg.Rect]:
        pass
