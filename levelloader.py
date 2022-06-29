import os.path
import pygame
from pygame import mixer
import constants
import sqlite
from entities.enemies import MovingEnemy
from entities.player import Player
from entities.spritegroups import whiteblocks, players, finishblocks, spikes, checkpoints, enemies, movingwhiteblocks, \
    coins
from entities.blocks import WhiteBlock, FinishBlock, Spike, SmallSpikeBottom, SmallSpikeTop, Checkpoint, \
    MovingWhiteBlock, Coin


# diese Klasse ist für das Laden eines Levels zuständig
class LevelLoader:

    # einlesen des Levels
    def get_level_info(level):
        file = "levels/level" + str(level) + ".txt"
        if os.path.isfile("levels/level" + str(level) + ".txt"):
            # wenn die Leveldatei existiert wird diese zurückgegeben
            o = open(file, 'r', encoding='utf-8')
            data = o.read()
            o.close()
            return data
        else:
            # wenn die Leveldatei nicht vorhanden ist wird der end-Screen gezeigt
            sqlite.insert_score()
            print("You completed all levels")
            mixer.music.stop()
            effect = pygame.mixer.Sound('music/end.mp3')
            effect.set_volume(0.05)
            effect.play()
            constants.end_state = True
            return None

    def gen_level_group(level):
        level_data = LevelLoader.get_level_info(level)
        x = 0
        y = 0
        if level_data is not None:
            # iterieren durch die Level-data
            # je nach Symbol wird ein andere Block mit x und y Koodrinate erstellt
            for i in level_data:
                if i == "1":
                    whiteblock = WhiteBlock(x, y)
                    whiteblocks.add(whiteblock)
                if i == "m":
                    movingblock = MovingWhiteBlock(x, y)
                    movingwhiteblocks.add(movingblock)
                if i == "f":
                    finishblock = FinishBlock(x, y)
                    finishblocks.add(finishblock)
                if i == "K":
                    spike = Spike(x, y)
                    spikes.add(spike)
                if i == "k":
                    spike = SmallSpikeBottom(x, y)
                    spikes.add(spike)
                if i == "ö":
                    spike = SmallSpikeTop(x, y)
                    spikes.add(spike)
                if i == "c":
                    checkpoint = Checkpoint(x, y)
                    checkpoints.add(checkpoint)
                if i == "€":
                    coin = Coin(x, y)
                    coins.add(coin)
                if i == "e":
                    enemy = MovingEnemy(x, y)
                    enemies.add(enemy)
                if i == "p":
                    player = Player(x, y)
                    players.add(player)
                if i == "y":
                    # zeigt an das die Zeile zuende ist
                    y += 1
                    x = -1
                if i != "y":
                    x += 1
