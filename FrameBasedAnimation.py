import math

class FrameBasedAnimation:
    def __init__(self, frames, position):
        self.__frames = frames
        self.__position_x = position[0]
        self.__position_y = position[1]
        self.__time_passed = 0
        self.disposed = False
    
    def render(self, surface):
        foto = self.__frames[math.floor(self.__time_passed)]
        surface.blit(foto,(self.__position_x-foto.get_height()/2,self.__position_y-foto.get_height()/2))
    
    def update(self, elapsed_seconds, tijd):
        self.__time_passed += elapsed_seconds
        self.__position_x-=tijd
        if self.__time_passed >= 9:
            self.disposed = True
