import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys 
from player import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    asteroids = pygame.sprite.Group()
    updateables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateables, drawables)
    Asteroid.containers = (asteroids, updateables, drawables)
    AsteroidField.containers = (updateables)
    Shot.containers = (updateables, drawables, shots)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)    
    asteroidfield = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
          
        screen.fill("black")

        for drawing in drawables:
            drawing.draw(screen)
        
        for asteroid in asteroids:
            if asteroid.check_collision(player):
                sys.exit("Game over")
            for shot in shots:
                if asteroid.check_collision(shot):
                    asteroid.split()
                    
        updateables.update(dt)
        
        pygame.display.flip()
        time = clock.tick(60)
        dt = time/1000


    
if __name__ == "__main__":
    main()


