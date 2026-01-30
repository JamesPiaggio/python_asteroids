import pygame
import constants
import player
import asteroid
import asteroidfield
import sys
from shot import Shot

from logger import log_state, log_event

def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    # Groups containers
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    clock = pygame.time.Clock()
    dt = 0
    player.Player.containers = (updatable, drawable)
    asteroid.Asteroid.containers = (asteroid_group, updatable, drawable)
    asteroidfield.AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    asteroidfield.AsteroidField()
    new_player = player.Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2) # Creates player instance
    clock.tick(60) # Sets FPS to 60 frames per second

    while True:
        log_state()
        # Allows program to close with exit button on window
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                return
        updatable.update(dt) # Triggers the update method for the updateable grouping
        for a in asteroid_group:
            if a.collides_with(new_player):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()
        screen.fill("black")
        for drawing in drawable: # Triggers the draw method for each in drawable grouping
            drawing.draw(screen) # Draws each object
        pygame.display.flip()
        dt = clock.tick() / 1000 # Calculates the delta time



            
if __name__ == "__main__":
    main()
