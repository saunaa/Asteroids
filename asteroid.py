import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)
        
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20, 50)
        vector1 = self.velocity.rotate(angle)
        vector2 = self.velocity.rotate(-angle)

        vector1_radius = self.radius - ASTEROID_MIN_RADIUS
        vector2_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, vector1_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, vector2_radius)

        asteroid1.velocity = vector1 * 1.2
        asteroid2.velocity = vector2 * 1.2








