import numpy as np
import Grass
import random
import House
import Water
import Tree
import Shrub


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
        for x in range(1, 10):
            for y in range(1, 10):
                if self.grid[x][y] == 0:
                    zero_counter += 1
        for i in range(0, zero_counter):
            self.fill_grid()

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
                #Lake generation logic
                found = False
                while found is False:
                    x =  random.randint(1, 10)
                    y =  random.randint(1, 10)
                    if self.grid[x][y] == 0:
                        found = True
                        self.grid[x][y] = Water("Lake", x, y, self)
                    for i in range(1,4):
                        found = False
                        while found is False:
                            x2 = x + random.randint(-1,1)
                            y2 = y + random.randint(-1,1)
                            if self.grid[x][y] == 0:
                                found = True
                                x = x2
                                y = y2
                                self.grid[x][y] = Water("Lake", x, y, self)
            else:
                #River + Bridge generation logic
                startx, starty = self.find_edge_point()
                endx, endy = self.find_edge_point()
                x_dist = startx - endx
                y_dist = starty - endy
                # x_dist > 0 -> go left otherwise right
                # y_dist > 0 go down otherwise up
                x = startx
                y = starty
                tile_count = abs(y_dist) + abs(x_dist)
                for i in range(0, tile_count):
                    self.grid[x][y] = Water("River", x, y)
                    if x != endx:
                        if(x_dist > 0):
                            x -+ 1
                        else:
                            x += 1
                    if y != endy:
                        if(y_dist > 0):
                            y -+ 1
                        else:
                            y += 1

    def find_edge_point(self):
        coinflip =  random.randint(1, 2)
        if coinflip == 1:
            x = random.randint(1, 10)
            coinflip =  random.randint(1, 2)
            if coinflip == 1:
                y == 1
            else:
                y == 10
        if coinflip == 2:
            y = random.randint(1, 10)
            coinflip =  random.randint(1, 2)
            if coinflip == 1:
                x == 1
            else:
                x == 10
        return x, y

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
                    self.grid[x][y] = House("House", x, y, self)
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
                    self.grid[x][y] = Tree("Tree", x, y)
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
                    self.grid[x][y] = Shrub("Shrub", x, y)
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
                    self.grid[x][y] = Grass("Grass", x, y)
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
                    self.grid[x][y] = Water("Pond", x, y)
                else:
                    pass

    def weighted_random(self):
        if self.gen_water is True:
            return random.choices([1, 2, 3, 4], weights=[35, 25, 25, 15])[0]
        else:
            return random.choices([1, 2, 3, 4], weights=[40, 30, 30, 0])[0]