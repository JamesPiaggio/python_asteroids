import pygame
import constants
import circleshape

# Creates a Player object
class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0

    # Method to set triangle dimensions and movement
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    # Method to draw player
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), constants.LINE_WIDTH) 

    # Method to rotate player
    def rotate(self, dt):
        self.rotation += constants.PLAYER_TURN_SPEED * dt

    # Method for key bindings
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
            print(self.rotation)
        if keys[pygame.K_d]:
            self.rotate(dt)
            print(self.rotation)