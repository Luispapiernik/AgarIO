import pygame as pg

from agario.config import settings
from agario.constants import COLORS
from agario.schemas import RGB


class Food(pg.sprite.Sprite):
    def __init__(self, x: int, y: int, color: RGB):
        super().__init__()

        self.radius = settings.food_initial_radius

        length = 2 * self.radius
        self.image = pg.surface.Surface((length, length))
        self.image.set_colorkey(COLORS["BLACK"])

        # position used to paint in the screen
        self.rect = self.image.get_rect()
        self.rect.center = -100, -100

        pg.draw.circle(self.image, color, (self.radius, self.radius), self.radius)

        # position used for the collisions
        self.real_rect = pg.Rect(x, y, length, length)
