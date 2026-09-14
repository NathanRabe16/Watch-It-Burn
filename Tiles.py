import random
import TileTypes

class Tile:

    def __init__(self, state, x, y, grid):
        self.state = state
        self.grid_x = x
        self.grid_y = y
        self.grid = grid
        self.burning = False
        self.burned = False
        self.apply_state(state)
        

    def apply_state(self, state):
        self.state = state
        self.type = TileTypes.STATES[state]
        self.burn_clock = self.type["burn_duration"]
        self.car = self.type["car"]
        self.BURN_PROB = {
            "burn": self.type["flammability"],
            }

    def get_car(self):
        return self.car

    def tick(self):
        if self.burned == True:
            pass
        # Do nothing cause already burned to ashes but honestly should never be called for tick after burned

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
            if random.random() < self.BURN_PROB["burn"][burn_chance]:
                self.burning = True
                self.on_fire()

    def get_burning(self):
        return self.burning

    def on_fire(self):
    # change sprites and stuff
        self.car = 'F'

    def to_ashes(self):
    # change sprites and stuff, clean up thread/simplify logic for remaining sim
        self.apply_state("Ashes")