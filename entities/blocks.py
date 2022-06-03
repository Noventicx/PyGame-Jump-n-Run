import pygame

from constants import WHITE, GREEN, RED, BLUE, YELLOW


# Ideen für Blöcke:
# bewegende Blöcke
# Teleporter
# Münzen

class WhiteBlock(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super(WhiteBlock, self).__init__()
        # self.surf = pygame.Surface((100, 100))
        # self.surf.fill(WHITE)
        # self.rect = self.surf.get_rect()
        self.surf = pygame.transform.scale(pygame.image.load("sprites/blocks/whiteblock.png"), (100, 100))
        self.rect = self.surf.get_rect()
        self.rect.x = x * 100
        self.rect.y = y * 100


class MovingWhiteBlock(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super(MovingWhiteBlock, self).__init__()
        # self.surf = pygame.Surface((100, 100))
        # self.surf.fill(WHITE)
        # self.rect = self.surf.get_rect()
        self.surf = pygame.transform.scale(pygame.image.load("sprites/blocks/whiteblock.png"), (100, 100))
        self.rect = self.surf.get_rect()
        self.rect.x = x * 100
        self.rect.y = y * 100
        self.moves_right = False
        self.speed = 1

    def update(self):
        if self.moves_right is True:
            self.rect.x = self.rect.x + self.speed
        elif self.moves_right is False:
            self.rect.x = self.rect.x - self.speed


class FinishBlock(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super(FinishBlock, self).__init__()
        #self.surf = pygame.Surface((100, 100))
        #self.surf.fill(GREEN)
        #self.rect = self.surf.get_rect()
        self.surf = pygame.transform.scale(pygame.image.load("sprites/blocks/finish.png"), (50, 50))
        self.rect = self.surf.get_rect()
        self.rect.x = x * 100 + 25
        self.rect.y = y * 100 + 50


class Spike(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super(Spike, self).__init__()
        #self.surf = pygame.Surface((100, 100))
        #self.surf.fill(RED)
        #self.rect = self.surf.get_rect()
        self.surf = pygame.transform.scale(pygame.image.load("sprites/blocks/spike.png"), (100, 100))
        self.rect = self.surf.get_rect()
        self.rect.x = x * 100
        self.rect.y = y * 100


class SmallSpikeBottom(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super(SmallSpikeBottom, self).__init__()
        #self.surf = pygame.Surface((100, 25))
        #self.surf.fill(RED)
        #self.rect = self.surf.get_rect()
        self.surf = pygame.transform.scale(pygame.image.load("sprites/blocks/spikesmall.png"), (100, 25))
        self.rect = self.surf.get_rect()
        self.rect.x = x * 100
        self.rect.y = y * 100 + 75


class SmallSpikeTop(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super(SmallSpikeTop, self).__init__()
        #self.surf = pygame.Surface((100, 25))
        #self.surf.fill(RED)
        #self.rect = self.surf.get_rect()
        self.surf = pygame.transform.flip(pygame.transform.scale(pygame.image.load("sprites/blocks/spikesmall.png"), (100, 25)), False, True)
        self.rect = self.surf.get_rect()
        self.rect.x = x * 100
        self.rect.y = y * 100


class Checkpoint(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super(Checkpoint, self).__init__()
        # self.surf = pygame.Surface((100, 100))
        # self.surf.fill(BLUE)
        # self.rect = self.surf.get_rect()
        self.surf = pygame.transform.scale(pygame.image.load("sprites/blocks/checkpoint.png"), (50, 50))
        self.rect = self.surf.get_rect()
        self.rect.x = x * 100 + 25
        self.rect.y = y * 100 + 50
        self.checked = False


class Coin(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super(Coin, self).__init__()
        # self.surf = pygame.Surface((25, 25))
        # self.surf.fill(YELLOW)
        # self.rect = self.surf.get_rect()
        self.surf = pygame.transform.scale(pygame.image.load("sprites/blocks/coin1.png"), (25, 25))
        self.rect = self.surf.get_rect()
        self.rect.x = x * 100 + 37.5
        self.rect.y = y * 100 + 37.5
        self.turn_anim = 0
        self.elapsed = pygame.time.get_ticks()

    def update(self):
        now = pygame.time.get_ticks()
        image_sprite_turn = [pygame.transform.scale(pygame.image.load("sprites/blocks/coin1.png"), (25, 25)),
                             pygame.transform.scale(pygame.image.load("sprites/blocks/coin2.png"), (25, 25)),
                             pygame.transform.scale(pygame.image.load("sprites/blocks/coin3.png"), (25, 25)),
                             pygame.transform.scale(pygame.image.load("sprites/blocks/coin4.png"), (25, 25)),
                             pygame.transform.scale(pygame.image.load("sprites/blocks/coin5.png"), (25, 25)),
                             pygame.transform.scale(pygame.image.load("sprites/blocks/coin6.png"), (25, 25))]
        if self.turn_anim >= len(image_sprite_turn):
            self.turn_anim = 0
        if now - self.elapsed > 250:
            self.surf = image_sprite_turn[self.turn_anim]
            self.turn_anim = self.turn_anim + 1
            self.elapsed = now
