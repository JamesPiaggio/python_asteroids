import pygame
import constants
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.SHOT_RADIUS)

    # Draws shot
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, constants.LINE_WIDTH)

    # Updates shot to allow for constant straight line speed
    def update(self, dt):
        self.position += self.velocity * dt