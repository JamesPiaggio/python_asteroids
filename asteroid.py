import pygame
import constants
from logger import log_event
import random
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    # Draws asteroid
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, constants.LINE_WIDTH)

    # Updates asteroid to allow for constant straight line speed
    def update(self, dt):
        self.position += self.velocity * dt

    # Splits asteroid when shot
    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20, 50)
            vector1 = self.velocity.rotate(random_angle)
            vector2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
            first = Asteroid(self.position.x, self.position.y, new_radius)
            second = Asteroid(self.position.x, self.position.y, new_radius)
            first.velocity = vector1 * 1.2
            second.velocity = vector2 * 1.2