import pygame
from colors import *
from directions import *


class Racket(pygame.sprite.Sprite):

    def __init__(self, screen, width, height, racket_width, racket_height, side):
        super().__init__()

        self.width = width
        self.height = height
        self.racket_height = racket_height
        self.racket_width = racket_width
        # self.racket_height = 500
        self.movement_speed = 5
        offset = 20
        self.screen = screen
        self.image = pygame.Surface([10, self.racket_height])
        self.image.fill(WHITE)
        pygame.draw.rect(self.image, WHITE, [0, 0, 10, self.racket_height])
        self.rect = self.image.get_rect()
        print(side)
        if side is Directions.LEFT:
            self.position = (offset, self.height / 2)
        else:
            self.position = (self.width - offset - 10, self.height / 2)
        print(self.position)
    @property
    def position(self):
        return (self.rect.x, self.rect.y)

    @position.setter
    def position(self, pos):
        try:
            pos_x, pos_y = pos
        except ValueError:
            raise ValueError("Pass an iterable with two items")
        else:
            self.rect.x, self.rect.y = pos_x, pos_y

    def move_up(self):
        if self.position[1] > 0:
            self.position = (self.position[0], self.position[1] - self.movement_speed)

    def move_down(self):
        if self.position[1] - 350 < 640:
            self.position = (self.position[0], self.position[1] + self.movement_speed)
        # elif self.position[1] + self.racket_height == WIN_HEIGHT:
        #     self.position
