import random
import Tiles


class Grid:

    def __init__(self, water: bool, houses: bool, size: int = 10):
        self.size = size
        self.cells = [[None] * size for _ in range(size)]
        self.gen_water = water
        self.gen_houses = houses

    def in_bounds(self, x, y):
        return 0 <= x < self.size and 0 <= y < self.size

    def get(self, x, y):
        return self.cells[x][y] if self.in_bounds(x, y) else None

    def is_empty(self, x, y):
        return self.in_bounds(x, y) and self.cells[x][y] is None

    def place(self, state, x, y):
        if not self.is_empty(x, y):
            return False
        self.cells[x][y] = Tiles.Tile(state, x, y, self)
        return True

    def empty_cells(self):
        return [(x, y)
                for x in range(self.size)
                for y in range(self.size)
                if self.cells[x][y] is None]

    def neighbors(self, x, y):
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            tile = self.get(x + dx, y + dy)
            if tile is not None:
                yield tile

    def all_ashes(self):
        for i in range (0, self.size):
            for j in range (0, self.size):
                check = self.get(j, i).get_burning()
                if check is True:
                    return False
        return True

    def any_burn(self):
        for i in range (0, self.size):
            for j in range (0, self.size):
                check = self.get(j, i).get_burning()
                if check is True:
                    return True
        return False

    def generate(self):
        if self.gen_water:
            self.generate_water()
        if self.gen_houses:
            self.generate_houses()
        self.fill_vegetation()

    def generate_water(self, max=4):
        for _ in range(random.randint(0, max)):
            if random.random() < 0.5:
                self.generate_lake()
            else:
                self.generate_river()

    def generate_lake(self, size=4):
        spots = self.empty_cells()
        if not spots:
            return
        x, y = random.choice(spots)
        self.place("Lake", x, y)
        for _ in range(size - 1):
            options = [(x + dx, y + dy)
                       for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))
                       if self.is_empty(x + dx, y + dy)]
            if not options:          # boxed in then stop growing
                break
            x, y = random.choice(options)
            self.place("Lake", x, y)

    def generate_river(self):
        start = self.random_edge_point()
        end = self.random_edge_point()
        if start == end:
            return
        x, y = start
        ex, ey = end
        bridge_chance = 4
        while True:
            if self.is_empty(x, y):
                on_bank = (x, y) in (start, end)
                if not on_bank and random.randint(1, bridge_chance) == 1:
                    self.place("Bridge", x, y)
                    bridge_chance += 2
                else:
                    self.place("River", x, y)
            if (x, y) == end:
                break
            if x != ex:
                x += 1 if ex > x else -1
            else:
                y += 1 if ey > y else -1

    def random_edge_point(self):
        last = self.size - 1
        if random.random() < 0.5:
            return random.randint(0, last), random.choice((0, last))
        return random.choice((0, last)), random.randint(0, last)

    def generate_houses(self, max_houses=6):
        spots = self.empty_cells()
        random.shuffle(spots)
        for x, y in spots[:random.randint(0, max_houses)]:
            self.place("House", x, y)

    def fill_vegetation(self):
        if self.gen_water:
            weights = {"Tree": 35, "Shrub": 25, "Grass": 25, "Pond": 15}
        else:
            weights = {"Tree": 40, "Shrub": 30, "Grass": 30}
        states, w = list(weights), list(weights.values())
        for x, y in self.empty_cells():
            self.place(random.choices(states, weights=w)[0], x, y)
