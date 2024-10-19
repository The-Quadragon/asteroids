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
        