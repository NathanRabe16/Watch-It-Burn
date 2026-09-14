
class Water:

    def __init__(self, state, x, y, grid):
        self.state = state
        self.grid_x = x
        self.grid_y = y
        self.grid = grid
        self.car = "O"


    def tick(self):
        pass
    # water can't burn and therefore does nothing acting as an obstacle for fire
    def get_car(self):
        return self.car
        
