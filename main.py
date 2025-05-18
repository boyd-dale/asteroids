import pygame
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Init pygame
    pygame.init()

    # Init screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Init clock
    clock = pygame.time.Clock()
    dt = 0


    while(True):
        
        # Return if the user has closed the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        
        # Fill the screen black
        screen.fill(0)



        # Refresh the screen, must be called last
        pygame.display.flip()

        # Pause the game loop until 1/60th of a second has passed
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
