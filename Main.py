import time
import CLI_Grid
import Grid
import random

class Main:

    def __init__(self):
        self.grid = Grid.Grid(True, False)
        self.grid.generate()
        self.size = self.grid.size
        self.cli = CLI_Grid.CLI(self.size)
        for i in range (0, self.size):
            for j in range (0, self.size):
                car = self.grid.get(j, i).get_car()
                self.cli.set_cell(j, i, car)
        self.cli.print_grid()


    def run(self):
        # while not everything is ashes or there's no more fire
        while self.grid.all_ashes() is not True: #and self.grid.any_burn() is True
            actions = []
            print("--------------------")
            time.sleep(2)
            for i in range (0, self.size):
                for j in range (0, self.size):
                    result = self.grid.get(j, i).tick()
                    if result is not None:
                        actions.append([j, i, result])
            for b in actions:
                x = b[0]
                y = b[1]
                result = b[2]
                self.grid.get(x, y).apply_action(result)
                car = self.grid.get(x, y).get_car()
                self.cli.set_cell(x, y, car)
            self.cli.print_grid()

    def ignite(self):
        done = False
        while done is False:
            tile = self.random_tile()
            if tile.get_burning() is not True and tile.burn_clock != 0:
                tile.set_ablaze()
                self.cli.set_cell(tile.grid_x, tile.grid_y, tile.car)
                done = True


    def random_tile(self):
        x = random.randint(0, self.size - 1)
        y = random.randint(0, self.size - 1)
        return self.grid.get(x, y)

if __name__ == "__main__":
    main = Main()
    print("--------------------")
    main.ignite()
    main.cli.print_grid()
    main.run()