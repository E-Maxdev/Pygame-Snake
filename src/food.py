import random

from settings import *
from grid import TileType

class Food:
    def __init__(self, grid: object):
        self.row = random.randint(0, GRID_SIZE - 1)
        self.column = random.randint(0, GRID_SIZE - 1)

        self.grid = grid

        self.grid.grid_draw(TileType.FOOD, self.row, self.column)

    def respawn(self):
        self.row = random.randint(0, GRID_SIZE - 1)
        self.column = random.randint(0, GRID_SIZE - 1)

        if self.grid.get_tiletype((self.row, self.column)) == TileType.SNAKE:
            self.respawn()

        self.grid.grid_draw(TileType.FOOD, self.row, self.column)

    def get_coords(self):
        return self.row, self.column