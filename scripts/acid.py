import pygame
import os

class Acid:
    
    def __init__(self,X,Y):
        self.X = X + 20
        self.Y = Y + 20
        self.image = pygame.image.load(os.path.join("img/acid.png"))
        self.image = pygame.transform.scale(self.image, (22, 37))
    
    def update_and_draw(self,screen):
        screen.blit(self.image, (self.X, self.Y))
        self.Y += 15