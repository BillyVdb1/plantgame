from asyncore import loop
import pygame

from looping import LoopingVariable


class Background:
    def __init__(self):
        self.__image = self.__create_image()
        self.__x = -100
        self.loop = LoopingVariable(self.__image.get_width())

    def __create_image(self):
        bg = pygame.image.load('gras_officieel.png')
        return bg

    def render(self, surface):
        surface.blit(self.__image, (self.__x, 0))
        surface.blit(self.__flip_image_horizontally(self.__image), (self.__x + self.__image.get_width()/2, 0))
       
    def update(self, elapsed_seconds):
        self.loop.increase(elapsed_seconds)
        self.__x = -self.loop.value

    def __flip_image_horizontally(self, surface):
        return pygame.transform.flip(surface, True, False)