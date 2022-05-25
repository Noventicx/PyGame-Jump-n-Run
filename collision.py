import pygame

import constants
from entities.spritegroups import whiteblocks, players, finishblocks, spikes, checkpoints
from levelloader import LevelLoader


def check_collision():
    for player in players:
        for whiteblock in whiteblocks:
            collision = pygame.Rect.colliderect(player.rect, whiteblock.rect)
            if collision:
                # TODO irgendiwe noch buggy wenn möglich fixxen oder neu implementieren
                if player.rect.centery <= whiteblock.rect.centery:
                    print("bottom")
                    player.rect.bottom = whiteblock.rect.top
                    player.onground = True
                elif player.rect.centerx >= whiteblock.rect.centerx:
                    print("left")
                    player.rect.left = whiteblock.rect.right
                    player.onground = False
                elif player.rect.centerx <= whiteblock.rect.centerx:
                    print("right")
                    player.rect.right = whiteblock.rect.left
                    player.onground = False
                if player.rect.centery >= whiteblock.rect.centery:
                    print("top")
                    player.rect.top = whiteblock.rect.bottom
                    player.onground = False

        for finishblock in finishblocks:
            collision = pygame.Rect.colliderect(player.rect, finishblock.rect)
            if collision:
                print("finish")
                constants.current_level = constants.current_level + 1
                whiteblocks.empty()
                finishblocks.empty()
                spikes.empty()
                players.empty()
                checkpoints.empty()
                LevelLoader.gen_level_group(constants.current_level)

        for spike in spikes:
            collision = pygame.Rect.colliderect(player.rect, spike.rect)
            if collision:
                print("spike")
                player.rect.x = player.start_x
                player.rect.y = player.start_y

        for checkpoint in checkpoints:
            collision = pygame.Rect.colliderect(player.rect, checkpoint.rect)
            if collision:
                print("checkpoint")
                player.start_x = checkpoint.rect.x
                player.start_y = checkpoint.rect.y