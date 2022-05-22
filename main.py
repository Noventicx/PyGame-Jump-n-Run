import pygame
from pygame import QUIT
from statemanager import StateMananger
from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT
)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True

manager = StateMananger()

while running:

    if pygame.event.get(QUIT):
        running = False

    manager.state.draw(screen)
    manager.state.events(pygame.event.get())
    pygame.display.flip()