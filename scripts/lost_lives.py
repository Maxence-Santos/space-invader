import pygame
import os

class Lost_lives:
    def __init__(self,X) -> None:
        self.X = X + 50
        self.Y = 50
        self.image = pygame.immage.load(os.path.join("img/coeur_vide"))    