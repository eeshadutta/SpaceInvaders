import pygame
import random


class ALIEN:
    def __init__(self, spawn):
        self.sprite = pygame.image.load("./sprites/alien1.png")
        self.x = random.randint(0, 7) * 100
        self.y = random.randint(0, 1) * 100
        self.type = 1
        self.spawn_time = spawn
