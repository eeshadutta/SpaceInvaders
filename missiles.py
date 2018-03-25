import pygame


class MISSILE:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, change):
        self.y -= change


class MISSILE1(MISSILE):
    def __init__(self, x, y):
        self.sprite = pygame.image.load("./sprites/missile1.png")
        MISSILE.__init__(self, x, y)


class MISSILE2(MISSILE):
    def __init__(self, x, y):
        self.sprite = pygame.image.load("./sprites/missile2.png")
        MISSILE.__init__(self, x, y)
