import pygame
from enum import Enum

from grid import TileType
from settings import *

class Direction(Enum):
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"

class Player:
    def __init__(self):
        # ticks per movement
        self.last_move = 0
        self.MOVE_DELAY = 150

        self.score = 0

        self.row = 4
        self.column = 1

        self.direction = Direction.RIGHT

        self.length = 1
        self.worm_coords = [[self.row, self.column]]

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and self.direction != Direction.DOWN:
            self.direction = Direction.UP
        if keys[pygame.K_a] and self.direction != Direction.RIGHT:
            self.direction = Direction.LEFT
        if keys[pygame.K_s] and self.direction != Direction.UP:
            self.direction = Direction.DOWN
        if keys[pygame.K_d] and self.direction != Direction.LEFT:
            self.direction = Direction.RIGHT

    def move(self, grid: object, food: object) -> bool:
        # Every 0.5 Seconds do this
        now = pygame.time.get_ticks()
        if now - self.last_move >= self.MOVE_DELAY:
            self.last_move = now

            last_pos = self.row, self.column

            match self.direction:
                case Direction.UP:
                    new_pos = self.row - 1, self.column

                case Direction.LEFT:
                    new_pos = self.row, self.column - 1

                case Direction.DOWN:
                    new_pos = self.row + 1, self.column

                case Direction.RIGHT:
                    new_pos = self.row, self.column + 1

            self.row, self.column = new_pos

            # Checking for out of bounds
            if new_pos[0] >= GRID_SIZE or new_pos[0] < 0 or new_pos[1] >= GRID_SIZE or new_pos[1] < 0:
                return False

            # Eat Food
            if new_pos == food.get_coords():
                self.length += 1
                self.worm_coords.append(last_pos)
                self.add_score()

                food.respawn()

            # Eat Yourself
            if grid.get_tiletype(new_pos) == TileType.SNAKE:
                return False

            # Making last pos empty and new pos Snake
            #grid.grid_draw(TileType.EMPTY, last_pos[0], last_pos[1])
            #grid.grid_draw(TileType.SNAKE, new_pos[0], new_pos[1])
            self.update_worm(grid, new_pos, last_pos)

            return True

    def update_worm(self, grid: object, new_pos, last_pos):
        # Clear the tail
        grid.grid_draw(TileType.EMPTY, *self.worm_coords[0])

        # Shift all the segments forward
        for i in range(len(self.worm_coords) - 1):
            self.worm_coords[i] = self.worm_coords[i + 1]

        # Set head to new pos
        self.worm_coords[-1] = new_pos
        grid.grid_draw(TileType.SNAKE, *new_pos)

    def add_score(self):
        self.score += 1

    def get_score(self):
        return self.score

    def get_length(self):
        return self.length

    def add_length(self, int: value):
        self.length += value

    
        
