import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
from nuke import *
from score import *


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    nukes = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    Nuke.containers = (updatable, drawable, nukes)
    NukeSpawn.containers = (updatable)

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    score = 0
    clock = pygame.time.Clock()
    dt = 0
    x_center = SCREEN_WIDTH / 2
    y_center = SCREEN_HEIGHT / 2
    player = Player(x_center, y_center)
    asteroidfield = AsteroidField()
    nukespawns = NukeSpawn()
    scoreboard = Score()
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game Over!")
                print(f"Score: {scoreboard.score} Nuke Level: {scoreboard.nuke_level}")
                exit(0)
            for shot in shots:
                if shot.collision(asteroid):
                    asteroid.split()
                    shot.kill()
                    scoreboard.scoreadd(1, False)
            for nuke in nukes:
                if nuke.collision(asteroid) and nuke.active == True:
                    asteroid.split()
                    scoreboard.scoreadd(1, True)

        for nuke in nukes:
            for shot in shots:
                if shot.collision(nuke):
                    nuke.activate()

        if scoreboard.nuke_spawn_score >= NUKE_SPAWN_SCORE and len(nukes) == 0:
            nukespawns.can_spawn = True
            scoreboard.nuke_spawn()

        # Update the things
        for thing in updatable:
            thing.update(dt)
        # Draw the things
        for thing in drawable:
            thing.draw(screen)

        # render 
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()