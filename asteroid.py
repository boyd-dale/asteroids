import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color(255,255,255), self.position,2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_low = Asteroid(self.position.x, self.position.y, asteroid_radius)
        asteroid_high = Asteroid(self.position.x, self.position.y, asteroid_radius)

        asteroid_low.velocity = self.velocity.rotate(-1*angle) * 1.2
        asteroid_high.velocity = self.velocity.rotate(angle) * 1.2
