import pygame as pg

from agario.config import settings


class Player(pg.sprite.Sprite):
    def __init__(self):
        self.radius = settings.initial_radius

        length = 2 * self.radius
        self.image = pg.surface.Surface((length, length))
        self.image.set_colorkey((0, 0, 0))

        self.rect = self.image.get_rect()
        self.rect.center = settings.screen_width // 2, settings.screen_height // 2

        pg.draw.circle(
            self.image, settings.player_color, (self.radius, self.radius), self.radius
        )
