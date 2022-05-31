import pygame
from pygame import QUIT

import constants
from statemanager import StateMananger
from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT
)
from states import EndState

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True

manager = StateMananger()

while running:

    # limit fps to 60
    # clock.tick(60)
    #print(clock.get_fps())

    if pygame.event.get(QUIT):
        running = False

    if constants.end_state is True:
        constants.end_state = False
        manager.go_to(EndState())

    manager.state.draw(screen)
    manager.state.events(pygame.event.get())
    pygame.display.flip()