import pygame
from constants import *
from logger import log_state
from circleshape import *
from player import Player

def main():
    print(f"Starting Asteroids with pygame version:{pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    pygame.time.Clock()
    my_group = pygame.sprite.Group()
    Player.cointainers = (group_a, group_b)
    dt = 0
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2 ,SCREEN_HEIGHT/2)
  
    
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        player.update(dt)
        screen.fill((0,0,0))
        player.draw(screen, "white", player.points,LINE_WIDTH)
       
        pygame.display.flip() #always last!
        
        


if __name__ == "__main__":
    main()
    