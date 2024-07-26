import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

# Get the initial time
start_time = pygame.time.get_ticks()
print(start_time)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the current time
    current_time = pygame.time.get_ticks()
    
    # Calculate elapsed time
    elapsed_time = current_time - start_time
    
    # Display elapsed time in seconds
    print(f"Elapsed Time: {elapsed_time / 1000:.2f} seconds")

    screen.fill((0, 0, 0))
    pygame.display.flip()
    clock.tick(60)
