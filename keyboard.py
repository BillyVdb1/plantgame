import pygame


def is_key_down(key):
    # pause = False

    return pygame.key.get_pressed()[key]

    # if pygame.key.get_pressed()[pygame.K_RIGHT]== True:   
    #     return True
    # if pygame.key.get_pressed()[pygame.K_LEFT] == True:
    #     return True
   
    # if pygame.key.get_pressed()[pygame.K_P] == True:
    #     pause = True



# is_key_down(pygame.K_LEFT)