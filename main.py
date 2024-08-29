import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    AsteroidField.containers = (updateable)
    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)

    asteroidfield = AsteroidField()
    player1 = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for entity in updateable:
            entity.update(dt)

        screen.fill((0, 0, 0))

        for entity in drawable:
            entity.draw(screen)

        for asteroid in asteroids:
            if asteroid.collides_with(player1):
                sys.exit("game over")
        

        dt = clock.tick(60) / 1000
        pygame.display.update()


if __name__ == "__main__":
    main()
