import random
from circleshape import *
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    #ovveride draw from circleshape
    def draw(self, screen):
        coordinates = (self.position.x, self.position.y)
        color = (255, 255, 255)
        pygame.draw.circle(screen, color, coordinates, self.radius, 2)
    
    #move asteroid in a straight line
    def update(self, dt):
        self.position += self.velocity * dt
    
    #split asteroids on collision
    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)

        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = a * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = b * 1.2