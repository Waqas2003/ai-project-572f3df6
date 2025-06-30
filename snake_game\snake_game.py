import pygame
import sys
import random
import time

pygame.init()

# Game constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLOCK_SIZE = 20
SPEED = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Game variables
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
food_pos = [random.randrange(1, (SCREEN_WIDTH // BLOCK_SIZE)) * BLOCK_SIZE, random.randrange(1, (SCREEN_HEIGHT // BLOCK_SIZE)) * BLOCK_SIZE]
food_spawn = True
direction = 'RIGHT'
score = 0

# Pygame display
pygame.display.set_caption('Snake Game')
game_display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'

    # Move snake
    if direction == 'UP':
        snake_pos[1] -= BLOCK_SIZE
    elif direction == 'DOWN':
        snake_pos[1] += BLOCK_SIZE
    elif direction == 'LEFT':
        snake_pos[0] -= BLOCK_SIZE
    elif direction == 'RIGHT':
        snake_pos[0] += BLOCK_SIZE

    # Snake body mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos == food_pos:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    # Food spawn
    if not food_spawn:
        food_pos = [random.randrange(1, (SCREEN_WIDTH // BLOCK_SIZE)) * BLOCK_SIZE, random.randrange(1, (SCREEN_HEIGHT // BLOCK_SIZE)) * BLOCK_SIZE]
        food_spawn = True

    # Game over conditions
    if snake_pos[0] < 0 or snake_pos[0] > SCREEN_WIDTH or snake_pos[1] < 0 or snake_pos[1] > SCREEN_HEIGHT:
        pygame.quit()
        sys.exit()
    for block in snake_body[1:]:
        if snake_pos == block:
            pygame.quit()
            sys.exit()

    # Game display
    game_display.fill(BLACK)
    for pos in snake_body:
        pygame.draw.rect(game_display, WHITE, pygame.Rect(pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(game_display, RED, pygame.Rect(food_pos[0], food_pos[1], BLOCK_SIZE, BLOCK_SIZE))
    pygame.display.update()

    # Frame rate control
    time.sleep(1 / SPEED)