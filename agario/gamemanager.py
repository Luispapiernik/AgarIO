import pygame as pg

from agario.config import settings
from agario.gamescene import GameScene

pg.display.init()


class GameManager:
    def __init__(self) -> None:
        self.initialize_parameters()
        self.initialize_window()
        self.initialize_scenes()

    def initialize_parameters(self):
        self.screen_width = settings.screen_width
        self.screen_height = settings.screen_height

        self.clock = pg.time.Clock()
        self.quit = False

    def initialize_window(self):
        self.set_icon()
        pg.display.set_caption(settings.title)
        self.screen = pg.display.set_mode((self.screen_width, self.screen_height))

    def set_icon(self):
        icon = pg.image.load(settings.icon_path)
        pg.display.set_icon(icon)

    def initialize_scenes(self):
        self.game_scene = GameScene()

    def run(self):
        while not self.quit:
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    self.quit = True
                if event.type == pg.KEYDOWN and event.key == pg.K_q:
                    self.quit = True

            self.game_scene.update(events)

            self.screen.fill(settings.background_color)
            self.game_scene.draw(self.screen)

            pg.display.flip()

            self.clock.tick(30)

        pg.display.quit()
