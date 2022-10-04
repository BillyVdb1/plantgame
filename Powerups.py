import pygame
from random import randrange

class Powerups:
    def __init__(self):
        self.powerup_type_procent = randrange(100)
        self.powerup_type = 0
        self.y_cord = -100
        self.x_cord = randrange(800) + 300
        self.y_hitbox_min = self.y_cord
        self.x_hitbox_min = self.x_cord
        self.y_hitbox_max = 82
        self.x_hitbox_max = 75
        self.sprite = 'Powerups/sun_machinegun.png'

        if 0<=self.powerup_type_procent<=33:
            # machinegun 
            self.powerup_type = 1
                        
        if 34<=self.powerup_type_procent<=66:
            # cone shooter
            self.powerup_type = 2

        if 67<=self.powerup_type_procent<=100:
            # cone shooter
            self.powerup_type = 3

    def update(self, x_cord, y_cord):
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.y_hitbox_min = self.y_cord
        self.x_hitbox_min = self.x_cord
        
    def render(self, surface):
        render_powerup(surface, self.x_cord, self.y_cord, self.sprite)

def render_powerup(surface, x_cord, y_cord, sprite):
    img_machinegun = pygame.image.load(sprite)
    surface.blit(img_machinegun, (x_cord, y_cord))