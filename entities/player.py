import pygame.draw

import constants


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super(Player, self).__init__()
        #self.surf = pygame.Surface((25, 25))
        #self.surf.fill((255, 0, 255))
        self.surf = pygame.image.load("entities/Sprite1.png")
        self.rect = self.surf.get_rect()
        self.speed = 1
        self.start_x = 100 * x
        self.start_y = 100 * y
        self.rect.x = 100 * x
        self.rect.y = 100 * y
        self.gravity = -1
        self.jump_height = 130
        self.is_jumping = False
        self.onground = True

    def update(self, events):
        self.rect.y = self.rect.y - self.gravity
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.surf = pygame.image.load("entities/Sprite2.png")
            self.rect.x = self.rect.x - self.speed
        if key[pygame.K_RIGHT]:
            self.surf = pygame.image.load("entities/Sprite3.png")
            self.rect.x = self.rect.x + self.speed
        if key[pygame.K_UP]:
            if self.onground is True:
                self.surf = pygame.image.load("entities/Sprite4.png")
                print("jump")
                effect = pygame.mixer.Sound('music/jump.mp3')
                effect.set_volume(0.05)
                effect.play()
                # TODO nochmal neue Idee ausarbeiten ist eigentlich kein Sprung
                self.onground = False
                #self.rect.y = self.rect.y - self.jump_height
                #Idee für neu Implementation siehe jump()
                self.jump()
        if self.is_jumping is True:
            self.gravity = 5
            self.jump_height = self.jump_height - 5
        if self.jump_height <= 0:
            self.is_jumping = False
            self.jump_height = 130
            self.gravity = -1

    def jump(self):
        self.is_jumping = True

    def kill(self):
        self.rect.x = self.start_x
        self.rect.y = self.start_y
        constants.current_deaths = constants.current_deaths + 1


