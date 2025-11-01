import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Pygame screen", screen, "initialized and window created. pygame.get_init =", pygame.get_init())
  
    clock = pygame.time.Clock()
    dt = 0

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    Player.containers = (updatables, drawables)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = asteroids, updatables, drawables

    AsteroidField.containers = updatables
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        updatables.update(dt)

        for obj in asteroids:
            if obj.collides_with(player):
                print("Game over!")
                return

        screen.fill("black")

        for obj in drawables:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000  # Limit to 60 FPS and get delta time
        

if __name__ == "__main__":
    main()
