from random import randrange
import pygame

class Zombie:
    def __init__(self):
        self.type = randrange(100)
        self.score_reward = 0
        self.x_cord = 1400
        self.y_cord = randrange(600)+15
        self.lifes = 1
        self.is_ge_hit = False
        self.hit_counter = 0
        self.speed = 1

        self.y_hitbox_min = self.y_cord
        self.x_hitbox_min = self.x_cord

        if 0<=self.type<=74:
            self.lifes = 3
            self.sprite = 'Zombies\PVZ_Zombie_Suit.png'
            self.sprite_hit = 'Zombies\Zombie_hit.png'
            self.score_reward = 1
            self.x_hitbox_max = 100
            self.y_hitbox_max = 160
            
        if 75<=self.type<=90:
            self.lifes = 6
            self.sprite = 'Zombies\Conehead2009HD.png'
            self.sprite_hit = 'Zombies\Conehead_hit.png'
            self.score_reward = 2
            self.x_hitbox_max = 93
            self.y_hitbox_max = 181
            
        if 91<=self.type<=100:
            self.lifes = 9
            self.sprite = 'Zombies\Buckethead_Zombie.png'
            self.sprite_hit = 'Zombies\Buckethead_hit.png'
            self.score_reward = 3
            self.x_hitbox_max = 89
            self.y_hitbox_max = 155
        
    def update(self, tijd):
        beweging=tijd*self.speed
        self.x_cord = self.x_cord-beweging
        self.y_cord = self.y_cord
        self.y_hitbox_min = self.y_cord
        self.x_hitbox_min = self.x_cord
    
    def render_hit(self, surface):
        render_zombie(surface, self.x_cord,self.y_cord, self.sprite_hit)
    
    def render_not_hit(self, surface):
        render_zombie(surface, self.x_cord, self.y_cord, self.sprite)

def render_zombie(surface, x_cord, y_cord, sprite):
    zombie = pygame.image.load(sprite)
    surface.blit(zombie,(x_cord,y_cord))