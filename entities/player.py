import pygame.draw

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super(Player, self).__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((255, 0, 255))
        self.rect = self.surf.get_rect()
        self.speed = 1
        self.start_x = 100 * x
        self.start_y = 100 * y
        self.rect.x = 100 * x
        self.rect.y = 100 * y
        self.gravity = -1
        self.jump = 130
        self.onground = True

    def update(self, events):
        self.rect.y = self.rect.y - self.gravity
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x = self.rect.x - self.speed
        if key[pygame.K_RIGHT]:
            self.rect.x = self.rect.x + self.speed
        if key[pygame.K_UP]:
            if self.onground is True:
                print("jump")
                #TODO nochmal neue Idee ausarbeiten ist eigentlich kein Sprung
                self.onground = False
                self.rect.y = self.rect.y - self.jump