import os
import random

random.seed(os.urandom(512))


class Grid:
    def __init__(self, height, width):
        self.grid = self.make_2d_grid(int(height / 20), int(width / 20))

    def update_values(self, grid):
        self.grid = grid

    def get_grid(self):
        return self.grid

    def make_2d_grid(self, rows, colls):
        arr = []
        for i in range(colls):
            temp = []
            for j in range(rows):
                temp.append(random.randint(0, 1))
            arr.append(temp)
        return arr
