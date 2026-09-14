

class CLI:

    def __init__(self):
        self.grid_size = 10

        self.grid = [['.' for _ in range(self.grid_size)] for _ in range(self.grid_size)]

    def print_grid(grid):
        for row in grid:
            print(' '.join(row))

    def set_cell(grid, x, y, char):
        grid[y][x] = char

    # Example usage
    # set_cell(grid, 3, 4, 'X')
    # set_cell(grid, 7, 7, 'O')
    #cprint_grid(grid)
