import pygame
import sys
from pygame.time import Clock
from State import State



# Main functie
def main():
    # Maak main surface
    surface = create_main_surface()
    state = State()
    pause = state.pause

    # Maakt klok
    klok = Clock()
    klok.tick()
    tijd = 1
    
    while True:
        # Pauzeert spel
        for event in pygame.event.get(eventtype=None, pump=True):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = not pause
            
            if event.type == pygame.QUIT:
                sys.exit(0)
  
        if not pause:
            state.update(tijd)

      # Berekent FPS
        tijd = klok.tick(144)/1000
      
        state.render(surface)


def create_main_surface():
    # Initialiseer Pygame
    pygame.init()
    
    screen_size = (1200, 800)

    # Create window with given size
    surface = pygame.display.set_mode(screen_size)

    return surface


# Run main functie
main()
