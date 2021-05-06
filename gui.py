import pygame as pygame
import sys

from grid import Grid


class Gui:
    BLACK = (0, 0, 0)
    WHITE = (200, 200, 200)
    BLUE = (0, 0, 255)

    def __init__(self, height, width, time):
        self.WINDOW_HEIGHT = height * 20
        self.WINDOW_WIDTH = width * 20
        self.time = time
        pygame.init()
        self.SCREEN = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.CLOCK = pygame.time.Clock()
        self.SCREEN.fill(self.BLACK)
        self.main_grid = Grid(self.WINDOW_WIDTH, self.WINDOW_HEIGHT)

    def draw_grid(self, grid_class):
        grid = grid_class.get_grid()
        grid_global = grid_class.get_grid()
        block_size = 20
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                rect = pygame.Rect(j * 20, i * 20, block_size, block_size)
                if grid[i][j] == 1:
                    pygame.draw.rect(self.SCREEN, self.WHITE, rect, 0)
                else:
                    pygame.draw.rect(self.SCREEN, self.BLACK, rect, 0)

        for x in range(0, self.WINDOW_WIDTH, block_size):
            for y in range(0, self.WINDOW_HEIGHT, block_size):
                rect = pygame.Rect(x, y, block_size, block_size)
                pygame.draw.rect(self.SCREEN, self.BLUE, rect, 1)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                state = grid[i][j]
                neighbours = self.count_neighbours(grid, i, j)
                if state == 0 and neighbours == 3:
                    grid_global[i][j] = 1
                elif state == 1 and (neighbours < 2 or neighbours > 3):
                    grid_global[i][j] = 0
                else:
                    grid_global[i][j] = state
        grid_class.update_values(grid_global)
        pygame.time.wait(self.time)

    def count_neighbours(self, grid, x, y):
        sum_of_neighbours = 0
        for i in range(-1, +2):
            for j in range(-1, +2):
                col = int((x + i + int(self.WINDOW_WIDTH / 20)) % int(self.WINDOW_WIDTH / 20))
                row = int((y + j + int(self.WINDOW_HEIGHT / 20)) % int(self.WINDOW_HEIGHT / 20))
                sum_of_neighbours += grid[row][col]
        sum_of_neighbours -= grid[x][y]
        return sum_of_neighbours

    def run(self):
        while True:
            self.draw_grid(self.main_grid)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
