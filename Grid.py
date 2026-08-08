import numpy as np
import Tile
import random


class Grid:

    def __init__(self, water : bool, houses : bool):
        self.grid = [[0 for _ in range(10)] for _ in range(10)]
        self.gen_water = water
        self.gen_houses = houses


    def generate_grid(self):
        if self.gen_water is True:
            self.generate_water()
        if self.gen_houses is True:
            self.generate_houses()
        zero_counter = 0
        for 

    def generate_water(self):
        types = []
        bodies = random.randint(0, 4) # 0-4 bodies of water
        if bodies == 0:
            return

        for i in range(bodies):
            type = random.randint(1, 2) # 1=lake, 2=river
            types.append(type)

        for i in types:
            if i == 1:
                #Lake + Bridge generation logic
            else:
                #River + Bridge generation logic

    def generate_houses(self):
        num_houses = random.randint(0, 6) # 0-6 houses
        if num_houses == 0:
            return

        for i in num_houses:
            found = False
            while found is False:
                x =  random.randint(1, 10)
                y =  random.randint(1, 10)
                if self.grid[x][y] == 0:
                    found = True
                    self.grid[x][y] = Tile("House", x, y)
                else:
                    pass


    def fill_grid(self):
        type = self.weighted_random()
        if type == 1:
            # Tree gen logic
            found = False
            while found is False:
                x =  random.randint(1, 10)
                y =  random.randint(1, 10)
                if self.grid[x][y] == 0:
                    found = True
                    self.grid[x][y] = Tile("Tree", x, y)
                else:
                    pass
        elif type == 2:
            # Shrub gen logic
            found = False
            while found is False:
                x =  random.randint(1, 10)
                y =  random.randint(1, 10)
                if self.grid[x][y] == 0:
                    found = True
                    self.grid[x][y] = Tile("Tree", x, y)
                else:
                    pass
        elif type == 3:
            # Grass gen logic
            found = False
            while found is False:
                x =  random.randint(1, 10)
                y =  random.randint(1, 10)
                if self.grid[x][y] == 0:
                    found = True
                    self.grid[x][y] = Tile("Tree", x, y)
                else:
                    pass
        else:
            # Pond gen logic
            found = False
            while found is False:
                x =  random.randint(1, 10)
                y =  random.randint(1, 10)
                if self.grid[x][y] == 0:
                    found = True
                    self.grid[x][y] = Tile("Tree", x, y)
                else:
                    pass



    def weighted_random(self):
        if self.gen_water is True:
            return random.choices([1, 2, 3, 4], weights=[35, 25, 25, 15])[0]
        else:
            return random.choices([1, 2, 3, 4], weights=[40, 30, 30, 0])[0]