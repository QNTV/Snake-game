import pygame
import random

# Initialize pygame and create a window
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snake Game")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Create the snake
snake_block = 10
snake_speed = 30
snake_list = [(200, 200), (210, 200), (220, 200)]

# Create the food
foodx = round(random.randrange(0, 800-snake_block) / 10.0) * 10.0
foody = round(random.randrange(0, 600-snake_block) / 10.0) * 10.0

# Define the direction of the snake
direction = "right"

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Change direction based on key presses
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != "right":
                direction = "left"
            elif event.key == pygame.K_RIGHT and direction != "left":
                direction = "right"
            elif event.key == pygame.K_UP and direction != "down":
                direction = "up"
            elif event.key == pygame.K_DOWN and direction != "up":
                direction = "down"

    # Move the snake
    if direction == "right":
        head = [(snake_list[0][0] + snake_block) %800, snake_list[0][1]]
    elif direction == "left":
        head = [(snake_list[0][0] - snake_block) % 800, snake_list[0][1]]
    elif direction == "up":
       head = [snake_list[0][0], (snake_list[0][1] - snake_block) % 600]
    elif direction == "down":
       head = [snake_list[0][0], (snake_list[0][1] + snake_block) % 600]
# Check for collision with food
    if head[0] == foodx and head[1] == foody:
        foodx = round(random.randrange(0, 800-snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, 600-snake_block) / 10.0) * 10.0
    else:
        snake_list.pop()

# Check for collision with the boundaries
    if head[0] >= 800 or head[0] < 0 or head[1] >= 600 or head[1] < 0:
        running = False

# Check for collision with the snake's body
    if head in snake_list[1:]:
        running = False

# Insert the new head
    snake_list.insert(0, head)

# Clear the screen
    screen.fill(black)

# Draw the snake
    for x, y in snake_list:
        pygame.draw.rect(screen, white, [x, y, snake_block, snake_block])

# Draw the food
    pygame.draw.rect(screen, red, [foodx, foody, snake_block, snake_block])

# Update the display
    pygame.display.update()
    pygame.time.Clock().tick(snake_speed)
