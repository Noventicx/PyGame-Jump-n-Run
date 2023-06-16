import pygame.draw
from pygame import KEYDOWN, K_RETURN, K_UP, K_DOWN, KEYUP, K_ESCAPE, mixer

import constants
import sqlite
from collision import check_collision
from entities.spritegroups import players, whiteblocks, finishblocks, spikes, checkpoints, enemies, movingwhiteblocks, \
    coins
from levelloader import LevelLoader
from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    BLACK,
    WHITE,
    GREEN,
    YELLOW
)


# Grundklasse für die States, auf dieser bauen alle States auf
class State(object):

    def __init__(self):
        pass

    # ist für das Zeichnen von z.B Spielern, Blocken und Enemies
    def draw(self, screen):
        pass

    # updaten der Position von Spielern und Enemies
    def update(self):
        pass

    # verarbeitet alle Tasteneingaben
    def events(self, events):
        pass

    # wenn die Szene gewchselt werden soll wird diese Funktion aufgeurfen
    def clear(self, screen):
        pass


class SplashState(State):

    def __init__(self):
        super(SplashState, self).__init__()

    def draw(self, screen):
        self.clear(screen)
        screen.blit(constants.background, (0, 0))
        font = pygame.font.SysFont(None, 32)
        title = font.render("Splash Screen", False, WHITE)
        title_rect = title.get_rect(center=(SCREEN_WIDTH / 2, 10))
        info = font.render("Enter drücken zum fortfahren", False, WHITE)
        info_rect = info.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        screen.blit(info, info_rect)
        screen.blit(title, title_rect)

    def events(self, events):
        for e in events:
            if e.type == KEYDOWN and e.key == K_RETURN:
                self.manager.go_to(MenuState())

    def clear(self, screen):
        screen.fill(BLACK)


class MenuState(State):
    global selected
    # der aktuell ausgewählte Text
    selected = 0

    def __init__(self):
        super(MenuState, self).__init__()

    # Zeichnen des Menüs
    def draw(self, screen):
        self.clear(screen)
        screen.blit(constants.background, (0, 0))
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
        score_text = font.render("Score", False, WHITE)
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH / 2, 90))
        screen.blit(score_text, score_rect)
        exit_text = font.render("Exit", False, WHITE)
        exit_rect = exit_text.get_rect(center=(SCREEN_WIDTH / 2, 110))
        screen.blit(exit_text, exit_rect)
        howto_text = font.render("* auswählen mit den Pfeiltasten, bestätigen mit Enter", False, WHITE)
        howto_rect = howto_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 15))
        screen.blit(howto_text, howto_rect)
        # der ausgewählte Text wird grün überzeichnet
        if selected == 0:
            play_text = font.render("Play", False, GREEN)
            screen.blit(play_text, play_rect)
        if selected == 1:
            info_text = font.render("Info", False, GREEN)
            screen.blit(info_text, info_rect)
        if selected == 2:
            score_text = font.render("Score", False, GREEN)
            screen.blit(score_text, score_rect)
        if selected == 3:
            exit_text = font.render("Exit", False, GREEN)
            screen.blit(exit_text, exit_rect)

    def events(self, events):
        global selected
        for e in events:
            if selected == 0 and e.type == KEYDOWN and e.key == K_RETURN:
                self.manager.go_to(GameState())
                mixer.init()
                mixer.music.load("music/background.mp3")
                mixer.music.set_volume(0.02)
                mixer.music.play(-1)
            # wechseln der State über das aktuell ausgewählte Element
            if selected == 1 and e.type == KEYDOWN and e.key == K_RETURN:
                self.manager.go_to(InfoState())
            if selected == 2 and e.type == KEYDOWN and e.key == K_RETURN:
                self.manager.go_to(ScoreState())
            if selected == 3 and e.type == KEYDOWN and e.key == K_RETURN:
                pygame.display.quit()
                pygame.quit()
                exit()
            # logik für das Wechseln der Textelemente mit Hilfe der Pfeiltasten
            if selected == 0 and e.type == KEYUP and e.key == K_DOWN:
                selected = 1
            elif selected == 1 and e.type == KEYUP and e.key == K_DOWN:
                selected = 2
            elif selected == 2 and e.type == KEYUP and e.key == K_DOWN:
                selected = 3
            elif selected == 3 and e.type == KEYUP and e.key == K_DOWN:
                selected = 0
            elif selected == 0 and e.type == KEYUP and e.key == K_UP:
                selected = 3
            elif selected == 1 and e.type == KEYUP and e.key == K_UP:
                selected = 0
            elif selected == 2 and e.type == KEYUP and e.key == K_UP:
                selected = 1
            elif selected == 3 and e.type == KEYUP and e.key == K_UP:
                selected = 2

    def clear(self, screen):
        screen.fill(BLACK)


class InfoState(State):

    def __init__(self):
        super(InfoState, self).__init__()

    def draw(self, screen):
        self.clear(screen)
        screen.blit(constants.background, (0, 0))
        font = pygame.font.SysFont(None, 32)
        title = font.render("Info Screen", False, WHITE)
        title_rect = title.get_rect(center=(SCREEN_WIDTH / 2, 10))
        screen.blit(title, title_rect)
        steuerungs_text = font.render("Steuerung: Bewegen mit den Pfeiltasten, springen mit Pfeiltaste nach oben",
                                      False, WHITE)
        gegner_text = font.render("Gegner: Alle roten Blöcke töten, bewegende Gegner können durch eine Sprung von "
                                  "oben getötet werden",
                                  False, WHITE)
        checkpoint_text = font.render("Checkpoint: speichert die Position des Spieler, so dass das Level nicht von "
                                      "vorne begonnen werden muss",
                                      False, WHITE)
        steuerungs_text_rect = steuerungs_text.get_rect(center=(SCREEN_WIDTH / 2, 50))
        gegner_text_rect = gegner_text.get_rect(center=(SCREEN_WIDTH / 2, 70))
        checkpoint_text_rect = checkpoint_text.get_rect(center=(SCREEN_WIDTH / 2, 90))
        screen.blit(steuerungs_text, steuerungs_text_rect)
        screen.blit(gegner_text, gegner_text_rect)
        screen.blit(checkpoint_text, checkpoint_text_rect)

    def events(self, events):
        for e in events:
            if e.type == KEYDOWN and e.key == K_RETURN:
                self.manager.go_to(MenuState())

    def clear(self, screen):
        screen.fill(BLACK)


class ScoreState(State):

    def __init__(self):
        super(ScoreState, self).__init__()

    # zeichnen der besten 3 Scores
    def draw(self, screen):
        self.clear(screen)
        screen.blit(constants.background, (0, 0))
        font = pygame.font.SysFont(None, 32)
        title = font.render("Highscores", False, WHITE)
        title_rect = title.get_rect(center=(SCREEN_WIDTH / 2, 10))
        screen.blit(title, title_rect)
        sqlite.get_scores(font, screen)

    def events(self, events):
        for e in events:
            if e.type == KEYDOWN and e.key == K_RETURN:
                self.manager.go_to(MenuState())

    def clear(self, screen):
        screen.fill(BLACK)


class GameState(State):
    # in dieser State läuft das eigentliche Spiel ab
    def __init__(self):
        super(GameState, self).__init__()
        LevelLoader.gen_level_group(constants.current_level)

    def draw(self, screen):
        self.clear(screen)
        screen.blit(constants.background, (0, 0))
        font = pygame.font.SysFont(None, 32)
        title = font.render("Game Screen", False, WHITE)
        title_rect = title.get_rect(center=(SCREEN_WIDTH / 2, 10))
        screen.blit(title, title_rect)
        # iterieren durch die Spritegroups und zeichnen der Blöcke, der Enemies und des Spielers
        for finishblock in finishblocks:
            screen.blit(finishblock.surf, finishblock.rect)
        for whiteblock in whiteblocks:
            screen.blit(whiteblock.surf, whiteblock.rect)
        for movingwhiteblock in movingwhiteblocks:
            screen.blit(movingwhiteblock.surf, movingwhiteblock.rect)
        for spike in spikes:
            screen.blit(spike.surf, spike.rect)
        for coin in coins:
            screen.blit(coin.surf, coin.rect)
        for checkpoint in checkpoints:
            screen.blit(checkpoint.surf, checkpoint.rect)
        for enemy in enemies:
            screen.blit(enemy.surf, enemy.rect)
        for player in players:
            screen.blit(player.surf, player.rect)
        # Zeichnen des Coins-Counters
        text = font.render("Coins: " + str(constants.current_coins), False, YELLOW)
        text_rect = title.get_rect(center=(75, 10))
        screen.blit(text, text_rect)
        # Zeichnen des Tode-Counters
        text2 = font.render("Tode: " + str(constants.current_deaths), False, YELLOW)
        text2_rect = title.get_rect(center=(75, 30))
        screen.blit(text2, text2_rect)

    def events(self, events):
        for e in events:
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                pygame.display.quit()
                pygame.quit()
                exit()

    def update(self):
        players.update()
        check_collision()
        enemies.update()
        movingwhiteblocks.update()
        coins.update()

    def clear(self, screen):
        screen.fill(BLACK)


class EndState(State):

    def init(self):
        super(EndState, self).init()

    def draw(self, screen):
        self.clear(screen)
        screen.blit(constants.background, (0, 0))
        font = pygame.font.SysFont(None, 32)
        title = font.render("Game Over", False, WHITE)
        title_rect = title.get_rect(center=(SCREEN_WIDTH / 2, 10))
        screen.blit(title, title_rect)
        # der Score der aktuellen Runde wird gezeichnet
        coin_text = font.render("Dein Score " + str(constants.current_coins * 100 - constants.current_deaths * 10),
                                False, WHITE)
        coin_text_rect = title.get_rect(center=(SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2))
        screen.blit(coin_text, coin_text_rect)
        # die Highscores werden gezeichnet
        coin_most_text = font.render("Highscores", False, WHITE)
        coin_most_text_rect = title.get_rect(center=(SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2 + 20))
        screen.blit(coin_most_text, coin_most_text_rect)
        sqlite.get_scores(font, screen)

    def events(self, events):
        for e in events:
            if e.type == KEYDOWN and e.key == K_RETURN:
                self.manager.go_to(MenuState())

    def clear(self, screen):
        screen.fill(constants.BLACK)
