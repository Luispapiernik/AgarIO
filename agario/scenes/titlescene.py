from os import path

import pygame as pg

from agario.config import settings
from agario.constants import COLORS
from agario.scenes.scene import Scene
from agario.schemas import SCENES


class TitleScene(Scene):
    def __init__(self):
        self.first_update = True

        self.font = pg.font.Font(
            path.join("assets/fonts/Press_Start_2P/PressStart2P-Regular.ttf"),
            120,
        )
        self.main_image = self.font.render(
            "Agar.io", True, COLORS["BLACK"], settings.background_color
        )
        self.main_image.set_colorkey(settings.background_color)

        self.main_image_rect = self.main_image.get_rect()
        self.main_image_rect.x = (
            settings.screen_width - self.main_image_rect.width
        ) // 2
        self.main_image_rect.y = settings.screen_height // 4

        self.font = pg.font.Font(
            path.join("assets/fonts/Press_Start_2P/PressStart2P-Regular.ttf"),
            20,
        )
        self.second_image = self.font.render(
            "Press the space key to start",
            True,
            COLORS["BLACK"],
            settings.background_color,
        )
        self.second_image.set_colorkey(settings.background_color)

        self.second_image_rect = self.second_image.get_rect()
        self.second_image_rect.x = (
            settings.screen_width - self.second_image_rect.width
        ) // 2
        self.second_image_rect.y = (
            self.main_image_rect.y + self.main_image_rect.height + 10
        )

    def update(self, events):
        for event in events:
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                return SCENES.GAME

        return SCENES.TITLE

    def draw(self, screen):
        if self.first_update:
            screen.fill(settings.background_color)
            screen.blit(self.main_image, self.main_image_rect)
            screen.blit(self.second_image, self.second_image_rect)

        to_update = []

        if self.first_update:
            to_update = screen.get_rect()
            self.first_update = False

        return to_update
