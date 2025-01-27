# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()

    Player.containers = (updatable_group, drawable_group)
    Asteroid.containers = (asteroids_group, updatable_group, drawable_group)
    AsteroidField.containers = (updatable_group,)
    Shot.containers = (shots_group, updatable_group, drawable_group)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    player = Player(x, y)
    AsteroidField()

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return        

        screen.fill((0, 0, 0))

        for u in updatable_group:
            u.update(dt)

        for a in asteroids_group:
            hit_player = a.check_collision(player)

            if hit_player:
                print("Game over!")
                sys.exit()

            for s in shots_group:
                hit_shot = a.check_collision(s)

                if hit_shot:
                    s.kill()
                    new_asteroids = a.split()
                    asteroids_group.add(*new_asteroids)

        for d in drawable_group:
            d.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
