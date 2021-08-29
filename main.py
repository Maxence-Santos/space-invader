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
    fire_power_up = []
    speed_power_up = []
    time_f = 0
    fire_t = 0
    speed_t = 0
    act_fire = False
    act_speed = False
    fire_rate = 18 # The higher , the slower the player shoots
    t_fire = []
    t_speed = []
    
    for i in range(3):
            hearts.append(Lives(lives_X))
            lives_X += 20
            
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
                
        ######  CREATE POWER_UPS ######
        if fire_t > 300:
            fire_alea_X = random.randint(8,520)
            if fire_alea_X in t_fire or fire_alea_X in t_speed:
                fire_alea_X = random.randint(8,520)
            t_fire.append(fire_alea_X)
            t_fire.append(fire_alea_X-50)
            t_fire.append(fire_alea_X+50)
            fire_power_up.append(Speed_fire(fire_alea_X))
            fire_t = 0
        
        if speed_t > 300:
            speed_alea_X = random.randint(27,520)
            if speed_alea_X in t_fire or speed_alea_X in t_speed:
                speed_alea_X = random.randint(8,520)
            t_speed.append(speed_alea_X)
            t_speed.append(speed_alea_X-50)
            t_speed.append(speed_alea_X+50)
            speed_power_up.append(Speed(speed_alea_X))
            speed_t = 0
            
        ###### UPDATE SCREEN ########
        if act_speed:
            player.update_power(input)
        else:
            player.update(input)     # Apply the changes depending on the input
        SCREEN.fill(BACKGROUND)  # We place it here to overwrite the old dino image
        player.draw_image(SCREEN)
        fire_t += 1
        speed_t += 1
        for ammo in ammos:
            ammo.update_and_draw(SCREEN)
        
        for power in fire_power_up:
            #act_fire = False
            time_f = 0
            fire_rate = 36
            if power.X-50 <= player.X <= power.X+50:
                fire_power_up.remove(power)
                t_fire.remove(power.X)
                t_fire.remove(power.X+50)
                t_fire.remove(power.X-50)
                act_fire = True
                if act_fire:
                    if time_f <= 300:
                        time_f += 1
                        fire_rate = 9
                    else:
                        act_fire = False
            
            power.update_and_draw(SCREEN)

        for speed in speed_power_up:
            act_speed = False
            if speed.X-50 <= player.X <= speed.X+50:
                speed_power_up.remove(speed)
                t_speed.remove(speed.X)
                t_speed.remove(speed.X+50)
                t_speed.remove(speed.X-50)
                act_speed = True
            speed.update_and_draw(SCREEN)
            
        pygame.display.update()  # Update the game with a 60 FPS rate
        CLOCK.tick(60)


main()
