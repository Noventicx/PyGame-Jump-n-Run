import os.path

import pygame

from entities.enemies import MovingEnemy
from entities.player import Player
from entities.spritegroups import whiteblocks, players, finishblocks, spikes, checkpoints, enemies, movingwhiteblocks, \
    coins
from entities.blocks import WhiteBlock, FinishBlock, Spike, SmallSpikeBottom, SmallSpikeTop, Checkpoint, \
    MovingWhiteBlock, Coin


class LevelLoader:

    def get_level_info(level):
        file = "levels/level" + str(level) + ".txt"
        if os.path.isfile("levels/level" + str(level) + ".txt"):
            o = open(file, 'r')
            data = o.read()
            o.close()
        else:
            print("You completed all levels")
            pygame.display.quit()
            pygame.quit()
            exit()

        return data

    def gen_level_group(level):
        level_data = LevelLoader.get_level_info(level)
        x = 0
        y = 0
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
                spike = SmallSpikeBottom(x, y + 0.75)
                spikes.add(spike)
            if i == "ö":
                spike = SmallSpikeTop(x, y)
                spikes.add(spike)
            if i == "c":
                checkpoint = Checkpoint(x, y)
                checkpoints.add(checkpoint)
            if i == "€":
                coin = Coin(x + 0.45, y + 0.75)
                coins.add(coin)
            if i == "e":
                enemy = MovingEnemy(x, y + 0.75)
                enemies.add(enemy)
            if i == "p":
                player = Player(x, y + 0.75)
                players.add(player)
            if i == "y":
                y = y + 1
                x = -1
            if i != "y":
                x = x + 1