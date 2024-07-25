import pygame
import sys
import random

class Pong:
    def __init__(self) -> None:
        # General setup
        pygame.init()
        self.clock = pygame.time.Clock()
        
        # Setting up the main window
        self.screen_width = 1280
        self.screen_height = 960
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Pong Game")

        # Game Rectangles
        self.ball = pygame.Rect(self.screen_width/2 - 15, self.screen_height/2 - 15, 30, 30)    # placed at the centre of screen
        self.player = pygame.Rect(self.screen_width - 20, self.screen_height/2 - 70, 10, 140)
        self.opponent = pygame.Rect(10, self.screen_height/2 - 70, 10, 140)

        # Game Color
        self.bg_color = pygame.Color('grey12')
        self.light_grey = (200, 200, 200)   # RGB color code

        # Speed Var
        self.ball_speed_x = 7 * random.choice((1, -1))
        self.ball_speed_y = 7 * random.choice((1, -1))
        self.player_speed = 0
        self.opponent_speed = 7
        
        # Text variables
        self.player_score = 0
        self.opponent_score = 0
        self.game_font = pygame.font.Font("freesansbold.ttf", 32)

        # Score Timer
        self.score_time = True
        
            
    def player_animations(self):
        """Animate the player's paddle and keep it within the screen bounds."""
        self.player.y += self.player_speed
        # This condition ensures that player bar doesn't move outside the screen
        if self.player.top <= 0:
            self.player.top = 0

        if self.player.bottom >= self.screen_height:
            self.player.bottom = self.screen_height
            
    def opponent_ai(self):
        """Simple AI to move the opponent paddle towards the ball."""
        if self.opponent.top < self.ball.y:
            self.opponent.top += self.opponent_speed
        if self.opponent.bottom > self.ball.y:
            self.opponent.bottom -= self.opponent_speed

        if self.opponent.top <= 0:
            self.opponent.top = 0

        if self.opponent.bottom >= self.screen_height:
            self.opponent.bottom = self.screen_height
            
    def ball_start(self):
        """Restart the ball in the center with a random direction."""
        self.current_time = pygame.time.get_ticks()
        self.ball.center = (self.screen_width/2, self.screen_height/2)

        if self.current_time - self.score_time < 700:
            number_three = self.game_font.render("3", False, self.light_grey)
            self.screen.blit(number_three, (self.screen_width/2 - 10, self.screen_height/2 + 20))

        if 700 < self.current_time - self.score_time < 1400:
            number_two = self.game_font.render("2", False, self.light_grey)
            self.screen.blit(number_two, (self.screen_width/2 - 10, self.screen_height/2 + 20))

        if 1400 < self.current_time - self.score_time < 2100:
            number_one = self.game_font.render("1", False, self.light_grey)
            self.screen.blit(number_one, (self.screen_width/2 - 10, self.screen_height/2 + 20))


        if self.current_time - self.score_time < 2100:
            self.ball_speed_x, self.ball_speed_y = 0, 0
        else:
            self.ball_speed_y = 7 * random.choice((1, -1))
            self.ball_speed_x = 7 * random.choice((1, -1))
            self.score_time = None
        
    def ball_animations(self):
        """Animate the ball and handle collisions."""
        self.ball.x += self.ball_speed_x
        self.ball.y += self.ball_speed_y

        # Making the ball bounce around the border
        if self.ball.top <= 0 or self.ball.bottom >= self.screen_height:
            self.ball_speed_y *= -1

        if self.ball.left <= 0:
            self.player_score += 1
            self.score_time = pygame.time.get_ticks()

        if self.ball.left >= self.screen_width:
            self.opponent_score += 1
            self.score_time = pygame.time.get_ticks()
            
        # Colissions
        if self.ball.colliderect(self.player) or self.ball.colliderect(self.opponent):
            self.ball_speed_x *= -1
            
    def handle_input(self):
        """Handle user input for quitting and moving the player's paddle."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.player_speed += 7
                if event.key == pygame.K_UP:
                    self.player_speed -= 7
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    self.player_speed -= 7
                if event.key == pygame.K_UP:
                    self.player_speed += 7
    
    def run(self):
        """Main game loop."""
        while True:
            self.handle_input()
            #ball_animations(ball_speed_x, ball_speed_y)     # this is only update the local variables
            self.ball_animations()
            self.player_animations()
            self.opponent_ai()
            
            # Visuals
            self.screen.fill(self.bg_color)
            pygame.draw.rect(self.screen, self.light_grey, self.player)        
            pygame.draw.rect(self.screen, self.light_grey, self.opponent)
            pygame.draw.ellipse(self.screen, self.light_grey, self.ball) 
            pygame.draw.aaline(self.screen, self.light_grey, (self.screen_width/2,0), (self.screen_width/2, self.screen_height))  # Draws the center ling
            
            if self.score_time:
                self.ball_start()

            player_text = self.game_font.render(f"{self.player_score}", False, self.light_grey)
            self.screen.blit(player_text, (660, 470))
    
            opponent_text = self.game_font.render(f"{self.opponent_score}", False, self.light_grey)
            self.screen.blit(opponent_text, (600, 470))
            
            # Updating the window
            pygame.display.flip()
            self.clock.tick(60)  # FPS for rendering
        
if __name__ == "__main__":
    game = Pong()
    game.run()