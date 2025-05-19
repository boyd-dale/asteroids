import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

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

    # Groups
    group_updatable = pygame.sprite.Group()
    group_drawable = pygame.sprite.Group()
    group_asteroids = pygame.sprite.Group()
    group_shots = pygame.sprite.Group()
    Player.containers = (group_updatable, group_drawable)
    Asteroid.containers = (group_asteroids, group_drawable, group_updatable)
    AsteroidField.containers = (group_updatable)
    Shot.containers = (group_shots, group_drawable, group_updatable)

    # Init player
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()


    while(True):
        
        # Return if the user has closed the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Rendering
        # Fill the screen black
        screen.fill(0)


        # Update call
        group_updatable.update(dt)

        for asteroid in group_asteroids:
            if asteroid.check_collision(player):
                print("Game over!")
                return
            for shot in group_shots:
                if asteroid.check_collision(shot):
                    asteroid.split()
                    shot.kill()

        # Draw call
        for item in group_drawable:
            item.draw(screen)





        # Refresh the screen, must be called last
        pygame.display.flip()

        # Pause the game loop until 1/60th of a second has passed
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
