import pygame.image

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
current_level = 1
current_coins = 0
current_deaths = 0
end_state = False
background = pygame.transform.scale(pygame.image.load("sprites/bg.jpg"), (1920, 1080))
