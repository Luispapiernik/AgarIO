import random

import pygame as pg

from agario.config import settings
from agario.constants import COLORS
from agario.food import Food


class FoodManager(pg.sprite.Group):
    def __init__(self) -> None:
        super().__init__()

        self.generate_food()

        # list of the sprite to show
        self.to_show: Food = []

    def generate_food(self):
        for _ in range(settings.food_amount):
            left = random.randint(
                settings.screen_width, settings.width - settings.screen_width
            )
            top = random.randint(
                settings.screen_height, settings.height - settings.screen_height
            )

            self.add(Food(x=left, y=top, color=random.choice(list(COLORS.values()))))

    def update(self, player) -> None:
        for food in self.to_show:
            food.rect.center = -500, -500

        self.to_show = []
        for food in self.sprites():
            if player.camera.colliderect(food.real_rect):
                food.rect.x = food.real_rect.x - player.camera.x
                food.rect.y = food.real_rect.y - player.camera.y
                self.to_show.append(food)

                if player.rect.colliderect(food.rect):
                    food.kill()
