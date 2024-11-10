from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.color = 255
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, self.color, self.color), self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt
        if self.color > 0:
            self.color -= 1
    
    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        
        random_angle = random.uniform(20, 50)
        new_velocity_positive = self.velocity.rotate(random_angle)
        random_angle_negative = -random_angle
        new_velocity_negative = self.velocity.rotate(random_angle_negative)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        Asteroid.spawn(self, new_radius, self.position, new_velocity_positive * random.uniform(1.0, 1.2))
        Asteroid.spawn(self, new_radius, self.position, new_velocity_negative * random.uniform(1.0, 1.2))
        
        self.kill()
            
    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity


