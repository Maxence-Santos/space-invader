import pygame
import os

class Player:
    
    def __init__(self):
        self.X = 248
        self.Y = 700
        self.image = pygame.image.load(os.path.join("img/ship.png"))
        self.image = pygame.transform.scale(self.image, (80, 75)) 
    
    def draw_image(self, screen):
        screen.blit(self.image, (self.X, self.Y))
    
    def update(self,input):
        if input[pygame.K_RIGHT] and self.X < 494:
            self.X += 5
        elif input[pygame.K_LEFT] and self.X > 0:
            self.X -= 5
