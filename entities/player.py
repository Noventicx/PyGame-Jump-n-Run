import pygame.draw
import constants


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super(Player, self).__init__()
        self.surf = pygame.transform.scale(pygame.image.load("sprites/player/idle1.png"), (25, 25))
        self.rect = self.surf.get_rect()
        self.speed = 2
        self.start_x = 100 * x + 37.5
        self.start_y = 100 * y + 75
        self.rect.x = 100 * x + 37.5
        self.rect.y = 100 * y + 75
        self.gravity = -1
        self.jump_height = 130
        self.is_jumping = False
        self.onground = True
        self.walking_anim = 0
        self.idle_anim = 0
        self.walking_right = True
        self.elapsed = pygame.time.get_ticks()

    # logik für die Fortbewegung und Animationen
    def update(self):
        self.rect.y -= self.gravity
        key = pygame.key.get_pressed()
        image_sprite_walking = [pygame.transform.scale(pygame.image.load("sprites/player/walking1.png"), (25, 25)),
                                pygame.transform.scale(pygame.image.load("sprites/player/walking2.png"), (25, 25))]
        image_sprite_idle = [pygame.transform.scale(pygame.image.load("sprites/player/idle1.png"), (25, 25)),
                             pygame.transform.scale(pygame.image.load("sprites/player/idle2.png"), (25, 25))]
        if key[pygame.K_LEFT]:
            now = pygame.time.get_ticks()
            self.walking_right = False
            if self.walking_anim >= len(image_sprite_walking):
                self.walking_anim = 0
            if now - self.elapsed > 250:
                if not self.is_jumping:
                    self.surf = pygame.transform.flip(image_sprite_walking[self.walking_anim], True, False)
                else:
                    self.surf = pygame.transform.flip(
                        pygame.transform.scale(pygame.image.load("sprites/player/jumping.png"), (25, 25)), True, False)
                self.walking_anim += 1
                self.elapsed = now
            self.rect.x -= self.speed
        if key[pygame.K_RIGHT]:
            now = pygame.time.get_ticks()
            self.walking_right = True
            if self.walking_anim >= len(image_sprite_walking):
                self.walking_anim = 0
            if now - self.elapsed > 250:
                if not self.is_jumping:
                    self.surf = image_sprite_walking[self.walking_anim]
                else:
                    self.surf = pygame.transform.scale(pygame.image.load("sprites/player/jumping.png"), (25, 25))
                self.walking_anim += 1
                self.elapsed = now
            self.rect.x += self.speed
        if key[pygame.K_UP]:
            if self.onground:
                if self.walking_right:
                    self.surf = pygame.transform.scale(pygame.image.load("sprites/player/jumping.png"), (25, 25))
                elif not self.walking_right:
                    self.surf = pygame.transform.flip(
                        pygame.transform.scale(pygame.image.load("sprites/player/jumping.png"), (25, 25)), True, False)
                print("jump")
                # Musik beim Springen
                effect = pygame.mixer.Sound('music/jump.mp3')
                effect.set_volume(0.05)
                effect.play()
                self.onground = False
                self.jump()
        if self.onground and not key[pygame.K_UP] and not key[pygame.K_LEFT] and not key[pygame.K_RIGHT]:
            now = pygame.time.get_ticks()
            # print(now - self.elapsed)
            if self.idle_anim >= len(image_sprite_idle):
                self.idle_anim = 0
            if now - self.elapsed > 250:
                if self.walking_right:
                    self.surf = image_sprite_idle[self.idle_anim]
                else:
                    self.surf = pygame.transform.flip(image_sprite_idle[self.idle_anim], True, False)
                self.idle_anim += 1
                self.elapsed = now
        if self.is_jumping:
            self.gravity = 5
            self.jump_height -= 5
        if self.jump_height <= 0:
            self.is_jumping = False
            self.jump_height = 130
            self.gravity = -2

    def jump(self):
        self.is_jumping = True

    # Anzahl der Tode wird um 1 erhöht
    def kill(self):
        self.rect.x = self.start_x
        self.rect.y = self.start_y
        constants.current_deaths += 1
