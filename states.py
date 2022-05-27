import pygame.draw
from pygame import KEYDOWN, K_SPACE, K_RETURN, K_UP, K_DOWN, KEYUP, K_ESCAPE
from ranger.config.commands import chain

import constants
from collision import check_collision
from entities.spritegroups import players, whiteblocks, finishblocks, spikes, checkpoints, enemies, movingwhiteblocks
from levelloader import LevelLoader
from constants import (
    SCREEN_WIDTH,
    BLACK,
    WHITE,
    GREEN
)


class State(object):

    def __init__(self):
        pass

    def draw(self, screen):
        pass

    def update(self):
        pass

    def events(self, events, screen):
        pass

    def clear(self, screen):
        pass


class SplashState(State):

    def __init__(self):
        super(SplashState, self).__init__()

    def draw(self, screen):
        self.clear(screen)
        font = pygame.font.SysFont(None, 32)
        title = font.render("Splash Screen", False, WHITE)
        title_rect = title.get_rect(center=(SCREEN_WIDTH / 2, 10))
        screen.blit(title, title_rect)

    def events(self, events):
        for e in events:
            if e.type == KEYDOWN and e.key == K_SPACE:
                self.manager.go_to(MenuState())

    def clear(self, screen):
        screen.fill(BLACK)


class MenuState(State):
    global selected
    selected = 0

    def __init__(self):
        super(MenuState, self).__init__()

    def draw(self, screen):
        self.clear(screen)
        font = pygame.font.SysFont(None, 32)
        title = font.render("Menu Screen", False, WHITE)
        title_rect = title.get_rect(center=(SCREEN_WIDTH / 2, 10))
        screen.blit(title, title_rect)
        play_text = font.render("Play", False, WHITE)
        play_rect = play_text.get_rect(center=(SCREEN_WIDTH / 2, 50))
        screen.blit(play_text, play_rect)
        info_text = font.render("Info", False, WHITE)
        info_rect = info_text.get_rect(center=(SCREEN_WIDTH / 2, 70))
        screen.blit(info_text, info_rect)
        exit_text = font.render("Exit", False, WHITE)
        exit_rect = exit_text.get_rect(center=(SCREEN_WIDTH / 2, 90))
        screen.blit(exit_text, exit_rect)
        if selected == 0:
            play_text = font.render("Play", False, GREEN)
            screen.blit(play_text, play_rect)
        if selected == 1:
            info_text = font.render("Info", False, GREEN)
            screen.blit(info_text, info_rect)
        if selected == 2:
            exit_text = font.render("Exit", False, GREEN)
            screen.blit(exit_text, exit_rect)

    def events(self, events):
        global selected
        for e in events:
            if e.type == KEYDOWN and e.key == K_SPACE:
                self.manager.go_to(GameState())
            if selected == 0 and e.type == KEYDOWN and e.key == K_RETURN:
                self.manager.go_to(GameState())
            if selected == 1 and e.type == KEYDOWN and e.key == K_RETURN:
                self.manager.go_to(InfoState())
            if selected == 2 and e.type == KEYDOWN and e.key == K_RETURN:
                pygame.display.quit()
                pygame.quit()
                exit()
            if selected == 0 and e.type == KEYUP and e.key == K_DOWN:
                selected = 1
            elif selected == 1 and e.type == KEYUP and e.key == K_DOWN:
                selected = 2
            elif selected == 2 and e.type == KEYUP and e.key == K_DOWN:
                selected = 0
            elif selected == 0 and e.type == KEYUP and e.key == K_UP:
                selected = 2
            elif selected == 1 and e.type == KEYUP and e.key == K_UP:
                selected = 0
            elif selected == 2 and e.type == KEYUP and e.key == K_UP:
                selected = 1

    def clear(self, screen):
        screen.fill(BLACK)


class InfoState(State):

    def __init__(self):
        super(InfoState, self).__init__()

    def draw(self, screen):
        self.clear(screen)
        font = pygame.font.SysFont(None, 32)
        title = font.render("Info Screen", False, WHITE)
        title_rect = title.get_rect(center=(SCREEN_WIDTH / 2, 10))
        screen.blit(title, title_rect)
        text = font.render("Info für die Steuerung hier vlt anzeigen", False, WHITE)
        text_rect = title.get_rect(center=(SCREEN_WIDTH / 2, 50))
        screen.blit(text, text_rect)

    def events(self, events):
        for e in events:
            if e.type == KEYDOWN and e.key == K_SPACE:
                self.manager.go_to(MenuState())

    def clear(self, screen):
        screen.fill(BLACK)


class GameState(State):

    def __init__(self):
        super(GameState, self).__init__()
        LevelLoader.gen_level_group(constants.current_level)

    def draw(self, screen):
        self.clear(screen)
        font = pygame.font.SysFont(None, 32)
        title = font.render("Game Screen", False, WHITE)
        title_rect = title.get_rect(center=(SCREEN_WIDTH / 2, 10))
        screen.blit(title, title_rect)
        for finishblock in finishblocks:
            screen.blit(finishblock.surf, finishblock.rect)
        for whiteblock in whiteblocks:
            screen.blit(whiteblock.surf, whiteblock.rect)
        for movingwhiteblock in movingwhiteblocks:
            screen.blit(movingwhiteblock.surf, movingwhiteblock.rect)
        for spike in spikes:
            screen.blit(spike.surf, spike.rect)
        for checkpoint in checkpoints:
            screen.blit(checkpoint.surf, checkpoint.rect)
        for enemy in enemies:
            screen.blit(enemy.surf, enemy.rect)
        for player in players:
            screen.blit(player.surf, player.rect)

    def events(self, events):
        enemies.update()
        movingwhiteblocks.update()
        players.update(events)
        check_collision()
        for e in events:
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                pygame.display.quit()
                pygame.quit()
                exit()
            if e.type == KEYDOWN and e.key == K_SPACE:
                constants.current_level = constants.current_level + 1
                whiteblocks.empty()
                movingwhiteblocks.empty()
                finishblocks.empty()
                spikes.empty()
                players.empty()
                enemies.empty()
                checkpoints.empty()
                LevelLoader.gen_level_group(constants.current_level)

    def clear(self, screen):
        screen.fill(BLACK)
