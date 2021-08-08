############## IMPORT #################

import pygame
import sys
from scripts.player import Player
from scripts.ammo import Ammo

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
        if input[pygame.K_SPACE]:
            if player.step > fire_rate:
                ammos.append(Ammo(player.X))
                player.step = 0 # Reset the step so the player can't shoot right away
        ###### UPDATE SCREEN ########
        player.update(input)     # Apply the changes depending on the input
        SCREEN.fill(BACKGROUND)  # We place it here to overwrite the old dino image
        player.draw_image(SCREEN)
        for ammo in ammos:
            ammo.update_and_draw(SCREEN)
        pygame.display.update()  # Update the game with a 60 FPS rate
        CLOCK.tick(60)


main()