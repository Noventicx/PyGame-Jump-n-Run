import pygame

import constants
from entities.spritegroups import whiteblocks, players, finishblocks, spikes, checkpoints, enemies, movingwhiteblocks, \
    coins
from levelloader import LevelLoader


# mit dieser Funktion wird die Kolision zwischen allen möglichen Sprites und Spritesgroups getestet
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
                    if player.is_jumping:
                        player.jump_height = 0
        # hier wird überprüft ob der Spieler springt oder in eine Richtung läuft.
        for movingwhiteblock in movingwhiteblocks:
            collision = pygame.Rect.colliderect(player.rect, movingwhiteblock.rect)
            if collision:
                # TODO irgendiwe noch buggy wenn möglich fixxen oder neu implementieren
                if player.rect.centery < movingwhiteblock.rect.centery:
                    print("bottom")
                    player.rect.bottom = movingwhiteblock.rect.top
                    if movingwhiteblock.moves_right:
                        player.rect.x += movingwhiteblock.speed
                    elif not movingwhiteblock.moves_right:
                        player.rect.x -= movingwhiteblock.speed
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
        # Nach einem erfolgreichen Level werden alle Daten zurückgesetzt.
        for finishblock in finishblocks:
            collision = pygame.Rect.colliderect(player.rect, finishblock.rect)
            if collision:
                print("finish")
                constants.current_level += 1
                whiteblocks.empty()
                movingwhiteblocks.empty()
                finishblocks.empty()
                spikes.empty()
                coins.empty()
                players.empty()
                enemies.empty()
                checkpoints.empty()
                LevelLoader.gen_level_group(constants.current_level)
        # Eine Kollision mit einem Spike tötet den spieler
        for spike in spikes:
            collision = pygame.Rect.colliderect(player.rect, spike.rect)
            if collision:
                print("spike")
                player.kill()
        # Eine Kollision mit einem Enemy tötet den Spieler, dabei wird kill.mp3 gespielt.
        for enemy in enemies:
            collision = pygame.Rect.colliderect(player.rect, enemy.rect)
            if collision:
                if player.rect.centery < enemy.rect.centery:
                    print("enemy killed")
                    effect = pygame.mixer.Sound('music/kill.mp3')
                    effect.set_volume(0.06)
                    effect.play()
                    enemies.remove(enemy)
                else:
                    print("killed by enemy")
                    player.kill()
        # Checkpoint wird erstellt und kann benutzt werden
        for checkpoint in checkpoints:
            collision = pygame.Rect.colliderect(player.rect, checkpoint.rect)
            if collision and not checkpoint.checked:
                checkpoint.checked = True
                effect = pygame.mixer.Sound('music/checkpoint.mp3')
                effect.set_volume(0.06)
                effect.play()
                print("checkpoint")
                checkpoint.surf = pygame.transform.scale(pygame.image.load("sprites/blocks/checkpoint_check.png"),
                                                         (50, 50))
                player.start_x = checkpoint.rect.x + 12.5
                player.start_y = checkpoint.rect.y + 25
        # Eine Kollision mit einem Coin vergößert die Anzahl der gesammelten Coins
        for coin in coins:
            collision = pygame.Rect.colliderect(player.rect, coin.rect)
            if collision:
                print("coin")
                constants.current_coins += 1
                effect = pygame.mixer.Sound('music/coin.mp3')
                effect.set_volume(0.05)
                effect.play()
                coins.remove(coin)

    for enemy in enemies:
        for whiteblock in whiteblocks:
            collision = pygame.Rect.colliderect(enemy.rect, whiteblock.rect)
            if collision:
                if enemy.moves_right:
                    enemy.moves_right = False
                elif not enemy.moves_right:
                    enemy.moves_right = True

    for movingwhiteblock in movingwhiteblocks:
        for whiteblock in whiteblocks:
            collision = pygame.Rect.colliderect(movingwhiteblock.rect, whiteblock.rect)
            if collision:
                if movingwhiteblock.moves_right:
                    movingwhiteblock.moves_right = False
                elif not movingwhiteblock.moves_right:
                    movingwhiteblock.moves_right = True
