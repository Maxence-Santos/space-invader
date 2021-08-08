############## IMPORT #################

import pygame
import sys
from random import randint
from scripts.player import Player
from scripts.ammo import Ammo
from scripts.alien import Alien
from scripts.acid import Acid

############ INIT ###########

pygame.init()

################### CONSTANTS ################################

HEIGHT = 854
WIDTH = 576  # mix between EDTV and 576i format
BACKGROUND = (18, 23, 28)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.Font("font/visitor.ttf", 30)
CLOCK = pygame.time.Clock()

############ MAIN FUNCTION ###############################


def main():

    ######  INIT GAME  ###########
    RUNNING = True
    pygame.display.set_caption("Space Invader")
    player = Player()
    alien = Alien()
    ammos = []
    fire_rate = 18 # The higher , the slower the player shoots
    ########### MAIN LOOP ################
    while RUNNING:
        input = pygame.key.get_pressed() # Gets input
        for event in pygame.event.get():    # Allow the user to quit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        ###### CREATE NEW AMMOS #######
        if input[pygame.K_SPACE] and player.step > fire_rate:
            ammos.append(Ammo(player.X))
            player.step = 0 # Reset the step so the player can't shoot right away
        if randint(0,50) == 0 and alien.step > fire_rate: # Fire is based on luck
            ammos.append(Acid(alien.X,alien.Y))
            alien.step = 0 # Reset the step so the alien can't shoot right away
        ###### UPDATE SCREEN ########
        player.update(input)     # Apply the changes depending on the input
        SCREEN.fill(BACKGROUND)  # We place it here to overwrite the old dino image
        player.draw_image(SCREEN)
        for ammo in ammos:
            ammo.update_and_draw(SCREEN)
        alien.draw_image(SCREEN)
        pygame.display.update()  # Update the game with a 60 FPS rate
        CLOCK.tick(60)


main()