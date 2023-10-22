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

# plain_color_surface = pygame.Surface((width, height))
plain_color_surface = pygame.Surface((100, 200))
# plain_color_surface.fill(color)
plain_color_surface.fill("Blue")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # screen.blit(surface_to_put_on_display, position)
    screen.blit(plain_color_surface, (0, 0))

    pygame.display.update()
    clock.tick(game_framerate)