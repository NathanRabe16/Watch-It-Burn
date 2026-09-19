import random
import TileTypes

class Tile:

    ACTIONS = ("to_ashes", "reduce_burn_time", "set_ablaze", "withstand")

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
        self.type = self.type[0]
        self.burn_clock = self.type["burn_duration"]
        self.car = self.type["car"]
        self.BURN_PROB = {
            "burn": self.type["flammability"],
            }

    def apply_action(self, action):
        if action not in self.ACTIONS:
            raise ValueError("Tile at (%s, %s) returned unknown action: %r"
                             % (self.grid_x, self.grid_y, action))
        getattr(self, action)()

    def get_car(self):
        return self.car

    def get_burned(self):
        return self.burned
    

    def tick(self):
        if self.burned == True:
            pass

        elif self.burning == True:
            if self.burn_clock == 0:
                if self.state == "House" and random.randint(1,2) == 2:
                    return("withstand")
                else:
                    return("to_ashes")
            else:
                return("reduce_burn_time")

        else:
            burn_chance = 0
            for neighbor in self.grid.neighbors(self.grid_x, self.grid_y):
                if neighbor.get_burning():
                    burn_chance += 1
            if random.random() < self.BURN_PROB["burn"][burn_chance]:
                return("set_ablaze")

    def get_burning(self):
        return self.burning

    def withstand(self):
        self.burn_clock = 2
        self.burning = False
        self.car = "H"
    
    def reduce_burn_time(self):
        self.burn_clock -= 1

    def on_fire(self):
    # change sprites and stuff
        self.car = '\033[1m' + '#' + '\033[0m'

    def to_ashes(self):
    # change sprites and stuff, clean up thread/simplify logic for remaining sim
        self.burned = True
        self.burning = False
        self.apply_state("Ashes")

    def set_ablaze(self):
        self.burning = True
        self.on_fire()