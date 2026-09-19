

class CLI:

    def __init__(self, size=10):
        self.grid_size = size

        self.grid = [['.' for _ in range(self.grid_size)] for _ in range(self.grid_size)]

    def print_grid(self):
        for row in self.grid:
            print(' '.join(row))

    def set_cell(self, x, y, char):
        self.grid[y][x] = char

    # Example usage
    # set_cell(grid, 3, 4, 'X')
    # set_cell(grid, 7, 7, 'O')
    #cprint_grid(grid)
