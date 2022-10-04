import pygame

class Avatar:
    def __init__(self):
        self.x_cord = 100
        self.y_cord = 350
        self.x_hitbox_min = self.x_cord
        self.x_hitbox_max = 99
        self.y_hitbox_min = self.y_cord
        self.y_hitbox_max = 104
        self.image = 'Sprites/peashooter.png'
        self.lives = 2
        
    def update(self, x_cord, y_cord):
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.x_hitbox_min = self.x_cord
        self.y_hitbox_min = self.y_cord

    def changeImage(self, waarde):
        if waarde == 0:
            # go back to default
            self.image = 'Sprites/peashooter.png'
            self.x_hitbox_max = 99
            self.y_hitbox_max = 104
        if waarde == 1:
            # machinegun
            self.image = 'Sprites/machinegun_plant.png'
            self.x_hitbox_max = 100
            self.y_hitbox_max = 98
        if waarde == 2:
            # coneshooter
            self.image = 'Sprites/Threepeater.png'
            self.x_hitbox_max = 99
            self.y_hitbox_max = 112
        if waarde == 3:
            # freez shooter
            self.image = 'Sprites/Shield.png'
            self.x_hitbox_max = 99
            self.y_hitbox_max = 170

    def render(self, surface):
        render_avatar(surface,self.x_cord,self.y_cord, self.image)

def render_avatar(surface, x_cord, y_cord, image):
    pea = pygame.image.load(image)
    surface.blit(pea,(x_cord,y_cord))