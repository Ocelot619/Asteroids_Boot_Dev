import pygame
from constants import *
from logger import log_state
from circleshape import *
from player import Player

def main():
    print(f"Starting Asteroids with pygame version:{pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    # Tworzymy grupy przed stworzeniem Playera
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    #  Dodajemy Player do tych grup przed stworzeniem instancji
    Player.containers = (updatable, drawable)

    # Tworzymy instancję Player
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    running = True
    while running:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        dt = clock.tick(60) / 1000

        # Aktualizacja wszystkich obiektów w grupie updatable
        updatable.update(dt)

        #Rysowanie wszystkich obiektów w grupie drawable
        screen.fill((0, 0, 0))
        for obj in drawable:
            obj.draw(screen, "white", obj.points, LINE_WIDTH)

        pygame.display.flip()  # zawsze na końcu

if __name__ == "__main__":
    main()