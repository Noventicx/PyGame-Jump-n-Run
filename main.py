import pygame
from pygame import QUIT
from statemanager import StateMananger
from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT
)

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True

manager = StateMananger()

while running:

    # limit fps to 60
    #clock.tick(60)
    #print(clock.get_fps())

    if pygame.event.get(QUIT):
        running = False

    manager.state.draw(screen)
    manager.state.events(pygame.event.get())
    pygame.display.flip()