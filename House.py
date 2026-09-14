import random

class House:

    def __init__(self, state, x, y, grid):
        self.state = state
        self.grid_x = x
        self.grid_y = y
        self.grid = grid
        self.burning = False
        self.burned = False
        self.damaged = False
        self.burn_clock = 5
        self.car = "@"

    def tick(self):
        if self.burned == True:
            pass

        elif self.burning == True:
            if self.burn_clock == 0:
                self.to_ashes()
            else:
                self.burn_clock -= 1

        else:
            burn_chance = 0
            if self.grid[self.grid_x + 1][self.grid_y].get_burning() == True:
                burn_chance += 1
            if self.grid[self.grid_x - 1][self.grid_y].get_burning() == True:
                burn_chance += 1
            if self.grid[self.grid_x][self.grid_y + 1].get_burning() == True:
                burn_chance += 1
            if self.grid[self.grid_x][self.grid_y - 1].get_burning() == True:
                burn_chance += 1
            if random.random() < (burn_chance / 4):
                self.burning = True
                self.on_fire()

    def get_burning(self):
        return self.burning

    def get_car(self):
        return self.car
    
    def on_fire(self):
    # change sprites and stuff
        self.car = 'F'

    def to_ashes(self):
    # houses have a chance to resist burning and return as a damaged house
        pass