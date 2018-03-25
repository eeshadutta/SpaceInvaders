import pygame


pygame.init()

GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 155)
RED = (255, 0, 0)

display_width = 800
display_height = 800
block_size = 100

font = pygame.font.SysFont("comicsansms", 70)
font_small = pygame.font.SysFont("comicsansms", 30)

gameDisplay = pygame.display.set_mode((display_width, display_height))


def display_message(string, color, x, y, size):
    if size == 30:
        msg_board = font_small.render(string, True, color)
    else:
        msg_board = font.render(string, True, color)
    gameDisplay.blit(msg_board, (x, y))
