import pygame
import sketchpy

pygame.init()                      #initialize

WIDTH, HEIGHT = 1000, 600
wn= pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("pong_but_better")
run = True

#colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0,0,0)
# for the ball
radius = 15
ball_x, ball_y = WIDTH//2 -radius, HEIGHT//2 - radius 
ball_vel_x, ball_vel_y = 0.3, 0.3

# for the paddle dimensions
paddle_width, paddle_height = 20, 120
left_paddle_y = HEIGHT//2 - paddle_height//2
right_paddle_y = HEIGHT//2 - paddle_height//2
left_paddle_x = right_paddle_x = 100 - paddle_width // 2  # Fixed the assignment
right_paddle_x = WIDTH - (100 + paddle_width // 2)  # Added right paddle's x-coordinate
right_paddle_vel = left_paddle_vel = 0


#main loop
while run:
    wn.fill(BLACK)                # THE ball line hiding 
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        elif i.type == pygame.KEYDOWN :          # ''keydown'' is for key arrows for movement 
            if i.key == pygame.K_UP :
                right_paddle_vel = -0.9
            if i.key == pygame.K_DOWN :
                right_paddle_vel = 0.9
            if i.key == pygame.K_w :          # press 'W' for up 
                left_paddle_vel = -0.9
            if i.key == pygame.K_s :          # press "S" for down
                left_paddle_vel = 0.9
        
        if i.type == pygame.KEYUP :
            right_paddle_vel = 0
            left_paddle_vel = 0

    #ball's movement controls
    #if ball_y <= 0 + radius or ball_y >= HEIGHT - radius :
    #    ball_vel_y*= -1
    if ball_y <= 0 or ball_y >= HEIGHT :
        ball_vel_y *= -1
    if ball_x <= 0 or ball_x >= WIDTH :
        ball_x, ball_y = WIDTH//2 -radius, HEIGHT//2 - radius
        ball_vel_x *= -1
        ball_vel_y *= -1
    if ball_x <= 0 + radius :
        ball_x, ball_y = WIDTH//2 -radius, HEIGHT//2 - radius 
        ball_vel_x, ball_vel_y = 0.3, 0.3     
    

    # paddle movement controls
    if left_paddle_y >= HEIGHT - paddle_height:         # without crossing borders
        left_paddle_y = HEIGHT - paddle_height
    if left_paddle_y <= 0 :
        left_paddle_y = 0
    
    if right_paddle_y >= HEIGHT - paddle_height:
        right_paddle_y = HEIGHT - paddle_height
    if right_paddle_y <= 0:
        right_paddle_y = 0

    # paddle collisions          
    # left paddle
    if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
        if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
            ball_x = left_paddle_x + paddle_width
            ball_vel_x *= -1

    if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
        if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
            ball_x = right_paddle_x 
            ball_vel_x *= -1


    #movements
    ball_x += ball_vel_x
    ball_y += ball_vel_y  

    right_paddle_y += right_paddle_vel      #paddle movement
    left_paddle_y += left_paddle_vel
    #right_paddle_x += right_paddle_vel
    #left_paddle_x += left_paddle_vel


    #objects
    pygame.draw.circle(wn, BLUE, (ball_x, ball_y), radius)   # is for ball position and width height

    pygame.draw.rect(wn, RED, pygame.Rect(left_paddle_x, left_paddle_y, paddle_width, paddle_height))

    pygame.draw.rect(wn, RED, pygame.Rect(right_paddle_x, right_paddle_y, paddle_width, paddle_height))


    pygame.display.update()

pygame.quit()