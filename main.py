import pygame
import sys
from constants import *
from player import *
from asteroidfield import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    #Create groups for concentrated updates
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    #initialize screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #create clock and delta variable
    clock = pygame.time.Clock()
    dt = 0
    
    #initilize asteroid containers
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)

    #create asteroid field
    field = AsteroidField()
    
    #initialize player and starting position
    Player.containers = (updateable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    #main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #create screen fill - always first
        screen.fill("black")
        
        #perform updates - done first after screen
        for item in updateable:
            item.update(dt)
        
        #draw updates - second
        for item in drawable:
            item.draw(screen) 

        #check for collisions - checking if player collides
        for roid in asteroids:
            if player.collision(roid):
                print("Game Over!")
                sys.exit()
        
        #update display
        pygame.display.flip()
        
        #limit to 60 FPS
        dt = clock.tick(60) / 1000
        
if __name__ == "__main__":
    main()