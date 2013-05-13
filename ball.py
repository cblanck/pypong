import pygame, random

random.seed()

class Ball(pygame.sprite.Sprite):
    """This class is for the ball, spawns where you tell it to"""
    def __init__(self, location, group):
        pygame.sprite.Sprite.__init__(self, group)
        
        self.image = pygame.Surface([8,8])
        self.image.fill((255,255,255))

        self.rect = self.image.get_rect()
        self.rect.x = location[0]
        self.rect.y = location[1]
        
        self.dx = 0
        self.dy = 0
        
        while self.dx == 0:
            self.dx = random.randint(-3, 3)
        while self.dy == 0:
            self.dy = random.randint(-3, 3)
    
    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
        
    def collide(self):
        self.dx = -self.dx
        self.dy = -self.dy
