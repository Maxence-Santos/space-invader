import pygame
import os

alien1 = pygame.image.load(os.path.join("img/alien/alien1.png"))
alien2 = pygame.image.load(os.path.join("img/alien/alien2.png"))

class Alien:
    
    def __init__(self):
        self.X = 248
        self.Y = 200
        self.image = alien1
        self.image = pygame.transform.scale(self.image, (60, 40))
        self.step = 0 # For the fire rate 
    
    def draw_image(self, screen):
        screen.blit(self.image, (self.X, self.Y))
        
        self.step += 1 # We put it here because this function is always executed once per frame