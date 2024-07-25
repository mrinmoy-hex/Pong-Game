import pygame, sys, random

# General setup
pygame.init()
clock = pygame.time.Clock()

def ball_animations():
    global ball_speed_x, ball_speed_y, player_score, opponent_score, score_time
    # Animationg ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    # Making the ball bounce around the border
    if (ball.top <= 0 or ball.bottom >= screen_height):
        ball_speed_y *= -1
        
    if ball.left <= 0:
        player_score += 1
        score_time = pygame.time.get_ticks()
        
    if ball.left >= screen_width:
        opponent_score += 1
        score_time = pygame.time.get_ticks()
        
        
    # Colissions
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1
        
    # return ball_speed_x, ball_speed_y # this method is also applicable

def player_animations():
    player.y += player_speed
    # This condition ensures that player bar doesn't move outside the screen
    if player.top <= 0:
        player.top = 0
        
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_ai():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
        
    if opponent.top <= 0:
        opponent.top = 0
        
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def ball_start():
    global ball_speed_x, ball_speed_y, score_time
    
    current_time = pygame.time.get_ticks()
    ball.center = (screen_width/2, screen_height/2)
    
    if current_time - score_time < 700:
        number_three = game_font.render("3", False, light_grey)
        screen.blit(number_three, (screen_width/2 - 10, screen_height/2 + 20))
        
    if 700 < current_time - score_time < 1400:
        number_two = game_font.render("2", False, light_grey)
        screen.blit(number_two, (screen_width/2 - 10, screen_height/2 + 20))
        
    if 1400 < current_time - score_time < 2100:
        number_one = game_font.render("1", False, light_grey)
        screen.blit(number_one, (screen_width/2 - 10, screen_height/2 + 20))
    
    
    if current_time - score_time < 2100:
        ball_speed_x, ball_speed_y = 0, 0
    else:
        ball_speed_y = 7 * random.choice((1, -1))
        ball_speed_x = 7 * random.choice((1, -1))
        score_time = None


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
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
opponent_speed = 7

# Text variables
player_score = 0
opponent_score = 0
game_font = pygame.font.Font("freesansbold.ttf", 32)

# Score Timer
score_time = True

while True:
    # Handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:  # This checks if the released key is the Down arrow key.
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7
            
    #ball_animations(ball_speed_x, ball_speed_y)     # this is only update the local variables
    ball_animations()
    player_animations()
    opponent_ai()
    
    # Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)        
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball) 
    pygame.draw.aaline(screen, light_grey, (screen_width/2,0), (screen_width/2, screen_height))  # Draws the center ling

    if score_time:
        ball_start()

    player_text = game_font.render(f"{player_score}", False, light_grey)
    screen.blit(player_text, (660, 470))
    
    opponent_text = game_font.render(f"{opponent_score}", False, light_grey)
    screen.blit(opponent_text, (600, 470))
    
    # Updating the window
    pygame.display.flip()
    clock.tick(60)  # this may be the FPS