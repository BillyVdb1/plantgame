import pygame

class Bullet:
    def __init__(self, start_x, start_y):
        self.x_cord = start_x+60
        self.y_cord = start_y+10
        self.x_hitbox_min = self.x_cord
        self.x_hitbox_max = 37
        self.y_hitbox_min = self.y_cord
        self.y_hitbox_max = 35
        
    def update(self, x_cord, y_cord):
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.x_hitbox_min = self.x_cord
        self.y_hitbox_min = self.y_cord

    def render(self, surface):
        render_bullet(surface,self.x_cord,self.y_cord)

def render_bullet(surface, x_cord, y_cord):
    pea = pygame.image.load('PEA.png')
    surface.blit(pea,(x_cord,y_cord))