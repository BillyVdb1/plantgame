import pygame

class Lives:
    def __init__(self):
        pygame.font.init()
        self.epic_font = pygame.font.Font('fonts/DiloWorld-mLJLv.ttf', 45)
        self.x_cord = 20
        self.y_cord = 680
        self.lives = 3
        
    def update(self, nieuwe_lives):
        self.lives = nieuwe_lives+1

    def render(self, surface):
        text_surface = self.epic_font.render('Lives: {}'.format(self.lives), False, (255, 255, 255))
        render_score(surface, text_surface ,self.x_cord ,self.y_cord)


def render_score(surface, text, x_cord, y_cord):
    surface.blit(text,(x_cord,y_cord))
    