import pygame
import sys
from constants import *
from player import *
from asteroidfield import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0
    
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)

    field = AsteroidField()
    
    Player.containers = (updateable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        
        for item in updateable:
            item.update(dt)
        
        for item in drawable:
            item.draw(screen) 

        for roid in asteroids:
            if player.collision(roid):
                print("Game Over!")
                sys.exit()
            
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
        
if __name__ == "__main__":
    main()