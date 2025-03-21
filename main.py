import pygame
from constants import *

def main():
    pygame.init()
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while True:
        # Check for quit events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # This exits the main() function
        
        # Fill the screen with black
        screen.fill("black")
        
        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()