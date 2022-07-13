import pygame as pg

from agario.config import settings

pg.display.init()


class GameManager:
    def __init__(self) -> None:
        self.width = settings.width
        self.height = settings.height

        pg.display.set_caption(settings.title)
        self.screen = pg.display.set_mode((self.width, self.height))

        self.quit = False

    def run(self):
        while not self.quit:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit = True
                if event.type == pg.KEYDOWN and event.key == pg.K_q:
                    self.quit = True

        pg.display.quit()
