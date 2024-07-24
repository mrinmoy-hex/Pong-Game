import pygame, sys

# General setup
pygame.init()
clock = pygame.time.Clock()

def ball_animations():
    global ball_speed_x, ball_speed_y
    # Animationg ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    # Making the ball bounce around the border
    if (ball.top <= 0 or ball.bottom >= screen_height):
        ball_speed_y *= -1
    if (ball.left <= 0 or ball.left >= screen_width):
        ball_speed_x *= -1
        
    # Colissions
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1
        
    # return ball_speed_x, ball_speed_y # this method is also applicable


# Setting up the main window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

# Game Rectangles
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15,30, 30)    # placed at the centre of screen
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height/2 - 70,10, 140)

# Game Color
bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)

# Speed Var
ball_speed_x = 7
ball_speed_y = 7

while True:
    # Handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    #ball_animations(ball_speed_x, ball_speed_y)     # this is only update the local variables
    ball_animations()

    # Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)        
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball) 
    pygame.draw.aaline(screen, light_grey, (screen_width/2,0), (screen_width/2, screen_height))  # Draws the center ling

    
    # Updating the window
    pygame.display.flip()
    clock.tick(60)  # this may be the FPS