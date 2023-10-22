import pygame
from sys import exit

pygame.init()

game_title = "Runner"
game_framerate = 60

game_window_width, game_window_height = 800, 400
game_window_size = (game_window_width, game_window_height)

screen = pygame.display.set_mode(game_window_size)
pygame.display.set_caption(game_title)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(game_framerate)