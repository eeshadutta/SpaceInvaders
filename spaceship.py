import pygame


class SHIP:
    def __init__(self):
        self.sprite = pygame.image.load("./sprites/spaceship.png")
        self.x = 400
        self.y = 700

    def update(self, change):
        self.x += change
