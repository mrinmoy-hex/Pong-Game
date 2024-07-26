import pygame
import sys
import random

# General setup
pygame.init()
clock = pygame.time.Clock()

# Screen setup
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Timer Example")

# Font setup
game_font = pygame.font.Font(None, 74)
light_grey = (200, 200, 200)
bg_color = pygame.Color('grey12')

# Initial variables
score_time = pygame.time.get_ticks()  # Start the timer
countdown_active = True  # Variable to track if countdown is active

def display_countdown():
    """Display countdown numbers on the screen and print statements."""
    global countdown_active
    current_time = pygame.time.get_ticks()
    
    # Calculate time difference
    time_difference = current_time - score_time
    
    print(f"Current time: {current_time}")
    print(f"Score time: {score_time}")
    print(f"Time difference: {time_difference}")
    
    # # Display "3" for the first second (0-1000 ms)
    # if time_difference < 1000:
    #     number_three = game_font.render("3", True, light_grey)
    #     screen.blit(number_three, (screen_width / 2 - 20, screen_height / 2))
    #     print("Displaying 3")
        
    # # Display "2" for the second second (1000-2000 ms)
    # elif 1000 <= time_difference < 2000:
    #     number_two = game_font.render("2", True, light_grey)
    #     screen.blit(number_two, (screen_width / 2 - 20, screen_height / 2))
    #     print("Displaying 2")
        
    # # Display "1" for the third second (2000-3000 ms)
    # elif 2000 <= time_difference < 3000:
    #     number_one = game_font.render("1", True, light_grey)
    #     screen.blit(number_one, (screen_width / 2 - 20, screen_height / 2))
    #     print("Displaying 1")
    
    # # After 3000 ms, end the countdown
    # if time_difference >= 3000:
    #     countdown_active = False
    #     print("Countdown finished")

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Fill the screen with background color
    screen.fill(bg_color)
    
    # Display countdown if it's active
    if countdown_active:
        display_countdown()
    
    # Update the display
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(60)
