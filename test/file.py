ball_speed_x = 7
ball_speed_y = 7

def ball_animations(ball_speed_x, ball_speed_y):
    ball_speed_x *= -1
    ball_speed_y *= -1
    print("Inside function:", ball_speed_x, ball_speed_y)

ball_animations(ball_speed_x, ball_speed_y)
print("Outside function:", ball_speed_x, ball_speed_y)
