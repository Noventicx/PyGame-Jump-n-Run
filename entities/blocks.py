import pygame

from constants import WHITE, GREEN, RED


class WhiteBlock(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super(WhiteBlock, self).__init__()
        self.surf = pygame.Surface((100, 100))
        self.surf.fill(WHITE)
        self.rect = self.surf.get_rect()
        self.rect.x = x * 100
        self.rect.y = y * 100


class FinishBlock(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super(FinishBlock, self).__init__()
        self.surf = pygame.Surface((100, 100))
        self.surf.fill(GREEN)
        self.rect = self.surf.get_rect()
        self.rect.x = x * 100
        self.rect.y = y * 100


class Spike(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super(Spike, self).__init__()
        self.surf = pygame.Surface((100, 100))
        self.surf.fill(RED)
        self.rect = self.surf.get_rect()
        self.rect.x = x * 100
        self.rect.y = y * 100


class SmallSpikeBottom(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super(SmallSpikeBottom, self).__init__()
        self.surf = pygame.Surface((100, 25))
        self.surf.fill(RED)
        self.rect = self.surf.get_rect()
        self.rect.x = x * 100
        self.rect.y = y * 100


class SmallSpikeTop(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super(SmallSpikeTop, self).__init__()
        self.surf = pygame.Surface((100, 25))
        self.surf.fill(RED)
        self.rect = self.surf.get_rect()
        self.rect.x = x * 100
        self.rect.y = y * 100
