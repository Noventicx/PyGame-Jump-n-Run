import pygame

import constants
from entities.spritegroups import whiteblocks, players, finishblocks, spikes, checkpoints, enemies, movingwhiteblocks
from levelloader import LevelLoader


def check_collision():
    for player in players:
        for whiteblock in whiteblocks:
            collision = pygame.Rect.colliderect(player.rect, whiteblock.rect)
            if collision:
                # TODO irgendiwe noch buggy wenn möglich fixxen oder neu implementieren
                if player.rect.centery < whiteblock.rect.centery:
                    print("bottom")
                    player.rect.bottom = whiteblock.rect.top
                    player.onground = True
                elif player.rect.centerx > whiteblock.rect.centerx:
                    print("left")
                    player.rect.left = whiteblock.rect.right
                    player.onground = False
                elif player.rect.centerx < whiteblock.rect.centerx:
                    print("right")
                    player.rect.right = whiteblock.rect.left
                    player.onground = False
                if player.rect.centery > whiteblock.rect.centery:
                    print("top")
                    player.rect.top = whiteblock.rect.bottom
                    player.onground = False

        for movingwhiteblock in movingwhiteblocks:
            collision = pygame.Rect.colliderect(player.rect, movingwhiteblock.rect)
            if collision:
                # TODO irgendiwe noch buggy wenn möglich fixxen oder neu implementieren
                if player.rect.centery < movingwhiteblock.rect.centery:
                    print("bottom")
                    player.rect.bottom = movingwhiteblock.rect.top
                    if movingwhiteblock.moves_right is True:
                        player.rect.x = player.rect.x + movingwhiteblock.speed
                    elif movingwhiteblock.moves_right is False:
                        player.rect.x = player.rect.x - movingwhiteblock.speed
                    player.onground = True
                elif player.rect.centerx > movingwhiteblock.rect.centerx:
                    print("left")
                    player.rect.left = movingwhiteblock.rect.right
                    player.onground = False
                elif player.rect.centerx < movingwhiteblock.rect.centerx:
                    print("right")
                    player.rect.right = movingwhiteblock.rect.left
                    player.onground = False
                if player.rect.centery > movingwhiteblock.rect.centery:
                    print("top")
                    player.rect.top = movingwhiteblock.rect.bottom
                    player.onground = False

        for finishblock in finishblocks:
            collision = pygame.Rect.colliderect(player.rect, finishblock.rect)
            if collision:
                print("finish")
                constants.current_level = constants.current_level + 1
                whiteblocks.empty()
                movingwhiteblocks.empty()
                finishblocks.empty()
                spikes.empty()
                players.empty()
                enemies.empty()
                checkpoints.empty()
                LevelLoader.gen_level_group(constants.current_level)

        for spike in spikes:
            collision = pygame.Rect.colliderect(player.rect, spike.rect)
            if collision:
                print("spike")
                player.rect.x = player.start_x
                player.rect.y = player.start_y

        for enemy in enemies:
            collision = pygame.Rect.colliderect(player.rect, enemy.rect)
            if collision:
                if player.rect.centery < enemy.rect.centery:
                    print("enemy killed")
                    enemies.remove(enemy)
                else:
                    print("killed by enemy")
                    player.rect.x = player.start_x
                    player.rect.y = player.start_y

        for checkpoint in checkpoints:
            collision = pygame.Rect.colliderect(player.rect, checkpoint.rect)
            if collision:
                print("checkpoint")
                player.start_x = checkpoint.rect.x
                player.start_y = checkpoint.rect.y

    for enemy in enemies:
        for whiteblock in whiteblocks:
            collision = pygame.Rect.colliderect(enemy.rect, whiteblock.rect)
            if collision:
                if enemy.moves_right is True:
                    enemy.moves_right = False
                elif enemy.moves_right is False:
                    enemy.moves_right = True

    for movingwhiteblock in movingwhiteblocks:
        for whiteblock in whiteblocks:
            collision = pygame.Rect.colliderect(movingwhiteblock.rect, whiteblock.rect)
            if collision:
                if movingwhiteblock.moves_right is True:
                    movingwhiteblock.moves_right = False
                elif movingwhiteblock.moves_right is False:
                    movingwhiteblock.moves_right = True