from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot

import pygame
import sys

def main():
    pygame.init()

    asteroid_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()
    updatable_group = pygame.sprite.Group()

    Asteroid.containers = (asteroid_group, updatable_group, drawable_group)
    AsteroidField.containers = (updatable_group)
    Player.containers = (updatable_group, drawable_group)
    Shot.containers = (shot_group, updatable_group, drawable_group)

    asteroid_field = AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable_group.update(dt)
        for asteroid in asteroid_group:
            if asteroid.collides(player):
                print("Game over!")
                sys.exit()
            
            for shot in shot_group:
                if shot.collides(asteroid):
                    shot.kill()
                    asteroid.kill()

        screen.fill("black")
        
        for drawable in drawable_group:
            drawable.draw(screen)
        pygame.display.flip()
        dt = clock.tick(120) / 1000

if __name__ == "__main__":
    main()