import pygame
import os

class Lives:
    def __init__(self,X) -> None:
        self.X = X
        self.Y = 20
        self.image = pygame.image.load(os.path.join("img/coeur.png"))
        self.image = pygame.transform.scale(self.image,(20,20))

    def draw(self,screen):
        screen.blit(self.image,(self.X,self.Y))