import random
from turtle import color 
import pygame
import time

# Initialize pygame
pygame.init()

# Set the screen size
width = 600
height = 600

# Create the screen
screen = pygame.display.set_mode((width, height))

# Set the title of the window
pygame.display.set_caption("Python Snake Game")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)

# Create the snake
snake_block = 10
snake_speed = 30
snake_list = []

# Create the snake starting position and length
x1 = 300
y1 = 300
length = 1

# Create the food
foodx = 0
foody = 0

# Create the clock
clock = pygame.time.Clock()

# Create the game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Move the snake
    x1 += 10
    y1 += 0

    # Create the snake's body
    snake_head = []
    snake_head.append(x1)
    snake_head.append(y1)
    snake_list.append(snake_head)
    if len(snake_list) > length:
        del snake_list[0]

    # Create the food
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    # Clear the screen
    screen.fill(black)

    # Draw the snake
    for x in snake_list:
        pygame.draw.rect(screen, white, [x[0], x[1], snake_block, snake_block])

    # Draw the food
    pygame.draw.rect(screen, white, [foodx, foody, snake_block, snake_block])
    # Check for collision with food
    if x1 == foodx and y1 == foody:
        length += 1

    # Check for collision with the edges of the screen
    if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
        pygame.quit()
        quit()

    # Check for collision with the body of the snake
    for block in snake_list[:-1]:
        if x1 == block[0] and y1 == block[1]:
            pygame.quit()
            quit()

    # Update the screen
    pygame.display.update()
    clock.tick(snake_speed)
