import pygame
import os

class Speed_fire:
    
    def __init__(self,X):
        self.X = X
        self.Y = 700
        self.image = pygame.image.load(os.path.join("img/speed_fire_power_up.png"))
        self.image = pygame.transform.scale(self.image, (55, 55))
    
    def update_and_draw(self,screen):
        screen.blit(self.image, (self.X, self.Y))