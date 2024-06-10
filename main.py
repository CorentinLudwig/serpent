import pygame
import sys
import random
from enum import Enum
from snake import Snake, Direction, Even
from const import *
from time import sleep


pygame.init()

def random_position(fruit: pygame.Rect):
    fruit.top = random.randrange(0, stop=WIDTH, step=SQUARE_SIZE)
    fruit.left = random.randrange(0, stop=HEIGHT, step=SQUARE_SIZE)



# Set up display
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Serpent")
clock = pygame.time.Clock()

# Initialize font
pygame.font.init()
font = pygame.font.SysFont('Arial', 48)  # You can also use pygame.font.Font(None, 48

# Render the text
dead_message = font.render('You are dead', True, white)
dead_rec = dead_message.get_rect(center=(WIDTH // 2, HEIGHT // 2))


snake = Snake(window)


# Initialize the fruit
fruit = pygame.Rect(0, 0, SQUARE_SIZE, SQUARE_SIZE)
random_position(fruit)


running = True
alive = True
while running:
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and snake.direction != Direction.RIGHT:
        snake.direction = Direction.LEFT
    elif keys[pygame.K_RIGHT] and snake.direction != Direction.LEFT:
        snake.direction = Direction.RIGHT
    elif keys[pygame.K_UP] and snake.direction != Direction.DOWN:
        snake.direction = Direction.UP
    elif keys[pygame.K_DOWN] and snake.direction != Direction.UP:
        snake.direction = Direction.DOWN
    else:
        snake.direction = None

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    


    if alive:
        # Fill the screen with white color (background)
        window.fill(grey)
        test = snake.can_move(fruit)
        match test:
            case Even.NOTHING:
                snake.move()
            case Even.EAT:
                snake.grow(fruit)
                random_position(fruit)
            case Even.DIE:
                window.blit(dead_message, dead_rec)
                alive = False
    elif keys[pygame.K_SPACE]:
        alive = True
        snake = Snake(window)
        random_position(fruit)
        


    # Draw the green square
    snake.draw_snake()
    
    pygame.draw.rect(window, red, fruit)

    pygame.display.flip()
    clock.tick(FPS)
    sleep(0.2)
    


# Quit Pygame
pygame.quit()
sys.exit()