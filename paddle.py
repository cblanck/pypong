import pygame

class Paddle(pygame.sprite.Sprite):
    """This class is for the pong paddles and takes as an argument where it is
    """
    def __init__(self, location, group):
        pygame.sprite.Sprite.__init__(self, group)

        self.width  = 10
        self.height = 30
        
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((255,255,255))

        self.rect   = self.image.get_rect()
        self.rect.x = location[0]
        self.rect.y = location[1]
        
        self.speed = 0

    def update(self):
        self.rect.y += self.speed
