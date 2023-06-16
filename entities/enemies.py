import pygame


# In dieser Datei werden Enemies erstellt.
class MovingEnemy(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super(MovingEnemy, self).__init__()
        self.surf = pygame.transform.flip(
            pygame.transform.scale(pygame.image.load("sprites/enemies/enemy.png"), (75, 25)), True, False)
        self.rect = self.surf.get_rect()
        self.rect.x = x * 100
        self.rect.y = y * 100 + 75
        self.moves_right = False
        self.speed = 1

    # logik für die Fortbewegung
    def update(self):
        if self.moves_right:
            self.surf = pygame.transform.scale(pygame.image.load("sprites/enemies/enemy.png"), (75, 25))
            self.rect.x += self.speed
        elif not self.moves_right:
            self.surf = pygame.transform.flip(
                pygame.transform.scale(pygame.image.load("sprites/enemies/enemy.png"), (75, 25)), True, False)
            self.rect.x -= self.speed
