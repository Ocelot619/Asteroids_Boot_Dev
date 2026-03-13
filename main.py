import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, LINE_WIDTH
from logger import log_state
from circleshape import *
from player import *

def main():
    print(f"Starting Asteroids with pygame version:{pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    pygame.time.Clock()
    dt = 0
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(400,300)
    
    
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0,0,0))
        player.draw(screen, "white", player.points,LINE_WIDTH)
        dt = clock.tick(60) / 1000
        
        pygame.display.flip() #always last!
        
        


if __name__ == "__main__":
    main()
    