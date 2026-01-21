import pygame
import constants
import player

from logger import log_state

def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0
    new_player = player.Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2) # Creates player instance
    clock.tick(60) # Sets FPS to 60 frames per second

    while True:
        log_state()
        # Allows program to close with exit button on window
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                return
        new_player.update(dt) # Updates players direction
        screen.fill("black")
        new_player.draw(screen) # Displays players current position
        pygame.display.flip()
        dt = clock.tick() / 1000 # Calculates the delta time



            
if __name__ == "__main__":
    main()
