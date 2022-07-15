import random

import pygame as pg

from agario.config import settings


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.radius = settings.player_initial_radius
        self.minimum_x = settings.screen_width // 2
        self.minimum_y = settings.screen_height // 2

        length = 2 * self.radius
        self.image = pg.surface.Surface((length, length))
        self.image.set_colorkey((0, 0, 0))

        self.rect = self.image.get_rect()
        self.rect.center = self.minimum_x, self.minimum_y

        pg.draw.circle(
            self.image, settings.player_color, (self.radius, self.radius), self.radius
        )

        # This limits are here because the player will be always on the center
        # of the screen
        left = random.randint(0, settings.width - settings.screen_width)
        top = random.randint(0, settings.height - settings.screen_height)

        self.camera = pg.Rect(left, top, settings.screen_width, settings.screen_height)

    # TODO: This should be improved such that the movement looks more elastic
    def update(self):
        mouse_x, mouse_y = pg.mouse.get_pos()
        x, y = self.rect.center

        dx = mouse_x - x
        dy = mouse_y - y

        elasticity = 0.1

        new_x = self.camera.x + elasticity * dx
        if self.minimum_x < new_x < settings.width - self.minimum_x:
            self.camera.x = new_x

        new_y = self.camera.y + elasticity * dy
        if self.minimum_y < new_y < settings.height - self.minimum_y:
            self.camera.y = new_y

    def draw(self, screen):
        top = self.camera.top
        left = self.camera.left

        x_offset = settings.grid_length - left % settings.grid_length
        y_offset = settings.grid_length - top % settings.grid_length

        # vertical lines
        for i in range(0, self.camera.width, settings.grid_length):
            start_pos = i + x_offset, 0
            end_pos = i + x_offset, self.camera.height
            pg.draw.line(
                screen,
                settings.grid_color,
                start_pos,
                end_pos,
                width=settings.grid_line_width,
            )

        # horizontal lines
        for i in range(0, self.camera.height, settings.grid_length):
            start_pos = 0, i + y_offset
            end_pos = self.camera.width, i + y_offset
            pg.draw.line(
                screen,
                settings.grid_color,
                start_pos,
                end_pos,
                width=settings.grid_line_width,
            )

        screen.blit(self.image, self.rect)
