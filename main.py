import pygame

pygame.init()

game_window_width, game_window_height = 800, 400
game_window_size = (game_window_width, game_window_height)

screen = pygame.display.set_mode(game_window_size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break

    pygame.display.update()