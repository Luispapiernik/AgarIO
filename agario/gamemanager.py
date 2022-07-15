import pygame as pg

from agario.config import settings
from agario.foodmanager import FoodManager
from agario.player import Player

pg.display.init()


class GameManager:
    def __init__(self) -> None:
        self.initialize_parameters()
        self.initialize_window()
        self.initialize_sprites()

    def initialize_parameters(self):
        self.screen_width = settings.screen_width
        self.screen_height = settings.screen_height

        self.clock = pg.time.Clock()
        self.pause = True
        self.quit = False

    def initialize_window(self):
        self.set_icon()
        pg.display.set_caption(settings.title)
        self.screen = pg.display.set_mode((self.screen_width, self.screen_height))

    def initialize_sprites(self):
        self.player = Player()
        self.food_manager = FoodManager()

    def set_icon(self):
        icon = pg.image.load(settings.icon_path)
        pg.display.set_icon(icon)

    def run(self):
        self.player.update()
        self.food_manager.update(self.player)
        while not self.quit:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit = True
                if event.type == pg.KEYDOWN and event.key == pg.K_q:
                    self.quit = True
                if event.type == pg.KEYDOWN and event.key == pg.K_p:
                    self.pause = not self.pause

            if not self.pause:
                self.player.update()
                self.food_manager.update(self.player)

            self.screen.fill(settings.background_color)
            self.player.draw(self.screen)
            self.food_manager.draw(self.screen)
            pg.display.flip()

            self.clock.tick(30)

        pg.display.quit()
