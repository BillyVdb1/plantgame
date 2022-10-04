import pygame

class Sounds:
    pygame.mixer.init()
    begin_level = pygame.mixer.Sound('Audio/Begin_level.wav')
    brains = pygame.mixer.Sound('Audio/Brains1.wav')
    game_over = pygame.mixer.Sound('Audio/Game_over_nerd.wav')
    splat = pygame.mixer.Sound('Audio/Splat.wav')
    moan1 = pygame.mixer.Sound('Audio/Zombie_moan1.wav')
    moan2 = pygame.mixer.Sound('Audio/Zombie_moan2.wav')
    explosion = pygame.mixer.Sound('Audio/Explosion.wav')
