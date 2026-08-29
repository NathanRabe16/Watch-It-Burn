import Grid
import random

class Tile:

    def __init__(self, type, x, y, grid):
        self.state = type
        self.grid_x = x
        self.grid_y = y
        self.grid = grid
        self.burning = False
        self.burned = False
        self.burn_clock = 6

    def set_up(self):
        pass

    def tick(self):
        if self.burned == True:
            pass
        # Do nothing cause already burned to ashes

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

    def on_fire(self):
    # change sprites and stuff
        pass

    def to_ashes(self):
    # change sprites and stuff, clean up thread/simplify logic for remaining sim
        pass

