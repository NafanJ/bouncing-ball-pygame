import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bouncing Ball")

# Set up the ball
ball_radius = 20
max_ball_speed = 15  # Maximum speed for the ball
ball_speed = [5, 5]  # Initial speed in x and y directions
ball_position = [width // 2, height // 2]  # Initial position at the center
ball_color = (255, 0, 0)

# Set up the background
background_color = (0, 0, 0)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update ball position
    ball_position[0] += ball_speed[0]
    ball_position[1] += ball_speed[1]

    # Bounce the ball off the walls
    if ball_position[0] - ball_radius <= 0 or ball_position[0] + ball_radius >= width:
        ball_speed[0] = -ball_speed[0]
        ball_speed[0] *= 1.2  # Increase speed in x direction
        ball_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # Change color

    if ball_position[1] - ball_radius <= 0 or ball_position[1] + ball_radius >= height:
        ball_speed[1] = -ball_speed[1]
        ball_speed[1] *= 1.2  # Increase speed in y direction
        ball_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # Change color

    # Limit the ball speed
    ball_speed[0] = min(max_ball_speed, abs(ball_speed[0])) * (1 if ball_speed[0] > 0 else -1)
    ball_speed[1] = min(max_ball_speed, abs(ball_speed[1])) * (1 if ball_speed[1] > 0 else -1)

    # Fill the background with black
    screen.fill(background_color)

    # Draw the ball
    pygame.draw.circle(screen, ball_color, (int(ball_position[0]), int(ball_position[1])), ball_radius)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(60)
