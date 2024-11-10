import pygame
import random
from circleshape import *
from constants import *
from score import *


class Nuke(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.active = False
        self.timer = 60

    def draw(self, screen):
        pygame.draw.circle(screen, "green", self.position, self.radius)

    def activate(self):
        self.active = True
        


    def update(self, dt):
        if self.timer < NUKE_TIME:
            self.kill()
        if self.active == True:
            self.timer -= 1
            self.radius = self.radius * NUKE_SPEED

class NukeSpawn(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0
        self.score_spawn_counter = 0
        self.can_spawn = False

    def spawn(self, x, y):
        nuke_spawned = Nuke(x, y, NUKE_START_RADIUS)

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > NUKE_SPAWN_RATE and self.can_spawn:
            self.can_spawn = False
            self.spawn_timer = 0
            positionx= (SCREEN_WIDTH / 2) + random.uniform(-60, 60)
            positiony= SCREEN_HEIGHT / 2 + random.uniform(-60, 60)
            self.spawn(positionx, positiony)