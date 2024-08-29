from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        split_angle = random.uniform(20, 50)
        velocity0 = self.velocity.rotate(-split_angle)
        velocity1 = self.velocity.rotate(split_angle)
        asteroid0, asteroid1, = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS), Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        asteroid0.velocity = velocity0 * 1.2
        asteroid1.velocity = velocity1 * 1.2
        self.kill()

        #if self.radius <= ASTEROID_MIN_RADIUS:
        #    return
        #split_angle = random.uniform(20, 50)
        #asteroid0, asteroid1, = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS), Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        #asteroid0.velocity = pygame.Vector2(self.velocity.rotate(-split_angle)) * pygame.Vector2(1.2, 1.2)
        #asteroid1.velocity = pygame.Vector2(self.velocity.rotate(split_angle)) * pygame.Vector2(1.2, 1.2)

    
    def update(self, dt):
        self.position += (self.velocity * dt)