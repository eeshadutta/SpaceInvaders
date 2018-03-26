import pygame
import time
import spaceship
import aliens
import missiles
from utils import display_message, font_small

pygame.init()

GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 155)
RED = (255, 0, 0)

display_width = 800
display_height = 800
block_size = 100

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Space Invaders")
pygame.display.set_icon(pygame.image.load("./sprites/alien1.png"))

gameBackground = pygame.image.load("./sprites/background.jpg")
gameDisplay.blit(gameBackground, (0, 0))

clock = pygame.time.Clock()

space_ship = spaceship.SHIP()


def game():
    intro = True
    while intro:
        gameDisplay.fill(BLACK)
        display_message("Space Invaders", BLUE, 180, 150, 70)
        display_message("Press P to Play and Q to Exit", GREEN, 180, 250, 30)
        display_message("Use A and D to move the SpaceShip", GREEN, 180,
                        280, 30)
        display_message("S and Space Bar will launch missiles", GREEN, 180,
                        310, 30)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    intro = False
                    main_loop()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()


def main_loop():
    game_exit = False
    missiles_list1 = []
    missiles_list2 = []
    aliens_list = []
    fps = 30
    start_time = round(time.time())
    x_change = 0
    score = 0
    create = True

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    if space_ship.x <= (display_width - 2*block_size):
                        x_change = block_size
                if event.key == pygame.K_a:
                    if space_ship.x >= block_size:
                        x_change = -block_size

                if event.key == pygame.K_SPACE:
                    missile = missiles.MISSILE1(space_ship.x + 10,
                                                space_ship.y)
                    missiles_list1.append(missile)
                if event.key == pygame.K_s:
                    missile = missiles.MISSILE2(space_ship.x + 10,
                                                space_ship.y)
                    missiles_list2.append(missile)

                if event.key == pygame.K_q:
                    game_exit = True
                    break

        gameDisplay.blit(gameBackground, (0, 0))

        interval = round(time.time()) - start_time

        if interval % 10 is 0 and create is True:
            create = False
            alien = aliens.ALIEN(interval)
            if alien not in aliens_list:
                aliens_list.append(alien)

        if interval % 10 is 9:
            create = True

        for missile in missiles_list1:
            missile.update(5)
            if missile.y <= 0:
                missiles_list1.remove(missile)
        for missile in missiles_list2:
            missile.update(10)
            if missile.y <= 0:
                missiles_list2.remove(missile)

        for alien in aliens_list:
            x = alien.x
            y = alien.y
            gameDisplay.blit(alien.sprite, (alien.x, alien.y))
            for missile in missiles_list1:
                gameDisplay.blit(missile.sprite, (missile.x, missile.y))
                if missile.x in range(x, x + 50) and \
                        missile.y in range(y, y + 60):
                    score += 1
                    aliens_list.remove(alien)
                    missiles_list1.remove(missile)

            for missile in missiles_list2:
                gameDisplay.blit(missile.sprite, (missile.x, missile.y))
                if missile.x in range(x, x + 50) and \
                        missile.y in range(y, y + 80):
                    alien.sprite = pygame.image.load("./sprites/alien2.png")
                    alien.type = 0
                    alien.spawn_time = interval
                    missiles_list2.remove(missile)

        for alien in aliens_list:
            if interval >= alien.spawn_time + 8 and alien.type == 1:
                aliens_list.remove(alien)
            if interval >= alien.spawn_time + 5 and alien.type == 0:
                aliens_list.remove(alien)

        if len(aliens_list) == 0:
            alien = aliens.ALIEN(interval)
            aliens_list.append(alien)

        space_ship.update(x_change)
        x_change = 0
        score_board = font_small.render("Score: " + str(score), True, RED)
        gameDisplay.blit(score_board, (0, 0))
        gameDisplay.blit(space_ship.sprite, (space_ship.x, space_ship.y))
        pygame.display.update()

        clock.tick(fps)

    quit()


game()
