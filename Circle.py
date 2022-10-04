from keyboard import is_key_down
import pygame


class Circle:
    def __init__(self):
        self.x_cord = 0
        self.y_cord = 0
    
    def update(self, x_cord, y_cord):
        # coordinaten cirkel aanpassen
        self.x_cord = x_cord
        self.y_cord = y_cord
               
    # Teken cirkel en toon op scherm
    def render(self, surface):
        draw_circle(self.x_cord, self.y_cord, surface)

# Teken een cirkel
def draw_circle(x_cord, y_cord, surface):
    # Teken cirkel op back buffer
    pos = (x_cord, y_cord)
    RED = (255,0,0)
    pygame.draw.circle(surface, RED, pos, 50)