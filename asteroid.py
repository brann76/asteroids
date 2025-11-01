import pygame
import random

from circleshape import *
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        #pygame.draw.circle(screen, "gray", self.position.x, self.position.y, self.radius, 2)
        pygame.draw.circle(screen, "gray", self.position, self.radius, 2)



    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.randint(10, 50)
        
        new_astr = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        new_astr.velocity = self.velocity.rotate(angle) * 1.2
        new_astr = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        new_astr.velocity = self.velocity.rotate(-angle) * 1.2

