import random
import os

random.seed(os.urandom(512))
class Grid:
    def __init__(self, height,width):
        self.grid = self.make2DGrid(int(height/20),int(width/20))
    def updateValues(self, grid):
        self.grid = grid
    def getGrid(self):
        return self.grid

    def make2DGrid(self,rows, colls):
        arr = []
        for i in range(colls):
            temp = []
            for j in range(rows):
                temp.append(random.randint(0, 1))
            arr.append(temp)
        return arr