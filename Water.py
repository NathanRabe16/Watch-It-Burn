from Grid import Grid

class Water:

    def __init__(self, type, x, y, grid):
        self.state = type
        self.grid_x = x
        self.grid_y = y
        self.grid = grid


    def tick(self):
        pass
    # water can't burn and therefore does nothing acting as an obstacle for fire
            
