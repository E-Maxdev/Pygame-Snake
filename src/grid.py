import pygame

from color import *
from settings import *

from enum import Enum

class TileType(Enum):
    EMPTY = 0
    SNAKE = 1
    FOOD = 2

    def getColor(self):
        match self:
            case TileType.EMPTY:
                return EMPTY_COLOR

            case TileType.SNAKE:
                return SNAKE_COLOR

            case TileType.FOOD:
                return FOOD_COLOR

class Grid:
    def __init__(self, screen):
        self.screen = screen
        
        self.TILE_SIZE = 50
        
        # 8x8 grid
        # 0 = EMPTY
        # 1 = SNAKE
        # 2 = FOOD
        self.grid = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],]

    def draw(self, screen):
        for row_index, row_value in enumerate(self.grid):
            # if row 1, y = 100
            tile_y = (row_index + 2) * self.TILE_SIZE

            for col_index, tile_value in enumerate(row_value):
                # if column 1, x = 100
                tile_x = (col_index + 2) * self.TILE_SIZE
                tile_rect = pygame.Rect(tile_x, tile_y,  self.TILE_SIZE, self.TILE_SIZE)
                
                match tile_value:
                    # Empty 
                    case 0:
                        pygame.draw.rect(screen, EMPTY_COLOR, tile_rect, 2)

                    # Snake
                    case 1:
                        pygame.draw.rect(screen, SNAKE_COLOR, tile_rect)

                    # Food
                    case 2:
                        pygame.draw.rect(screen, FOOD_COLOR, tile_rect)

    def get_coords(self, row: int, column: int) -> tuple[int, int]:
        tile_x = (column + 1) * self.TILE_SIZE
        tile_y = (row + 1) * self.TILE_SIZE

        return tile_x, tile_y

    def grid_draw(self, tiletype: TileType, row: int, column: int):
        self.grid[row][column] = tiletype.value

        tile_coords = self.get_coords(row, column)

        tile_rect = pygame.Rect(*tile_coords,  self.TILE_SIZE, self.TILE_SIZE)
        pygame.draw.rect(self.screen, tiletype.getColor(), tile_rect)

    def get_tiletype(self, coords: tuple[int, int]) -> TileType:
        return TileType(self.grid[coords[0]][coords[1]])  

    def get_grid(self) -> list:
        return self.grid