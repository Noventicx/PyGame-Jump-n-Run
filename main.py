import pygame
from pygame import QUIT

import constants
from statemanager import StateMananger
from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT
)
from states import EndState

# initialisieren von pygame
pygame.init()
clock = pygame.time.Clock()
# setzen der Fenstergröße
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True

manager = StateMananger()

# starten des Gameloops in diesem Loop läuft das ganze spiel
while running:

    # limitieren auf 60 fps
    clock.tick(60)
    # print(clock.get_fps())

    if pygame.event.get(QUIT):
        running = False

    if constants.end_state:
        constants.end_state = False
        manager.go_to(EndState())

    manager.state.draw(screen)
    manager.state.events(pygame.event.get())
    manager.state.update()
    pygame.display.flip()
