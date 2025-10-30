import pygame
from constants import *

def main():
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Pygame screen", screen, "initialized and window created. pygame.get_init =", pygame.get_init())
  
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill("black")
        pygame.display.flip()
        dt = clock.tick(60) / 1000  # Limit to 60 FPS and get delta time
        

if __name__ == "__main__":
    main()
