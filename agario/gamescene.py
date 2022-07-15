import pygame as pg

from agario.foodmanager import FoodManager
from agario.player import Player
from agario.scene import Scene


class GameScene(Scene):
    def __init__(self) -> None:
        self.initialize_parameters()
        self.initialize_sprites()

    def initialize_parameters(self):
        self.pause = True

    def initialize_sprites(self):
        self.player = Player()
        self.food_manager = FoodManager()

        self.player.update()
        self.food_manager.update(self.player)

    def update(self, events):
        for event in events:
            if event.type == pg.KEYDOWN and event.key == pg.K_p:
                self.pause = not self.pause

        if not self.pause:
            self.player.update()
            self.food_manager.update(self.player)

    def draw(self, screen):
        self.player.draw(screen)
        self.food_manager.draw(screen)
