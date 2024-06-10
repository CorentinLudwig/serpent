import pygame
import sys
import random
from enum import Enum
from const import *


class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    DOWN = 3
    UP = 4
    
class Even(Enum):
    NOTHING = 1
    EAT = 2
    DIE = 3

    
def is_dead(snake, head):
    for e in snake:
        if head.colliderect(e):
            return True
    return False

class Snake:
    def __init__(self,  window) -> None:
        self.snake = [pygame.Rect((0), (0), SQUARE_SIZE, SQUARE_SIZE)]
        self.window = window
        self.direction = None  # No initial direction


    def move(self):
        if self.direction is None:
            return
        head = self.snake[0].copy()  # Create a new head based on the current head
        match self.direction:
            case Direction.UP:
                head.top -= SQUARE_SIZE
            case Direction.DOWN:
                head.top += SQUARE_SIZE
            case Direction.LEFT:
                head.left -= SQUARE_SIZE
            case Direction.RIGHT:
                head.left += SQUARE_SIZE
        self.snake = [head] + self.snake[:-1]  # Move the snake
        
    def can_move(self, fruit):
        if self.direction is None:
            return 
        head = self.snake[0].copy()  # Create a new head based on the current head
        match self.direction:
            case Direction.UP:
                head.top -= SQUARE_SIZE
            case Direction.DOWN:
                head.top += SQUARE_SIZE
            case Direction.LEFT:
                head.left -= SQUARE_SIZE
            case Direction.RIGHT:
                head.left += SQUARE_SIZE
        if(head.colliderect(fruit)):
            return Even.EAT
        elif is_dead(self.snake, head):
            return Even.DIE
        return Even.NOTHING
        
              
    def draw_snake(self):
        for e in self.snake:
            pygame.draw.rect(self.window, green, e)

    def grow(self, fruit: pygame.Rect):
        new_part = pygame.Rect(fruit.left, fruit.top, SQUARE_SIZE, SQUARE_SIZE)
        self.snake.insert(0,new_part)
    
    def eat(self, fruit):
        if self.snake[0].colliderect(fruit):
            self.grow_snake(fruit)

