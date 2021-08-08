import pygame
import os

class Ammo:
    
    def __init__(self,X):
        self.X = X + 30
        self.Y = 670
        self.image = pygame.image.load(os.path.join("img/fireball.png"))
        self.image = pygame.transform.scale(self.image, (22, 37))
    
    def update_and_draw(self,screen):
        screen.blit(self.image, (self.X, self.Y))
        self.Y -= 15