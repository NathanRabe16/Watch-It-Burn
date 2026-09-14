import time
import CLI_Grid
import Grid

class Main:

    def __init__(self):
        self.grid = Grid.Grid(False, False)
        self.grid.generate_grid()
        self.cli = CLI_Grid.CLI()
        x = 0
        y = 0
        for i in range (0, 9):
            for j in range (0, 9):
                car = self.grid.grid[x][y].get_car()
                self.cli.set_cell(self.cli.grid, x, y, f'{car}')
                x+=1
            y+=1
        self.cli.print_grid(self.cli.grid)


    def run(self):
        time.sleep(3)
        x = 0
        y = 0
        for i in range (0, 9):
            for j in range (0, 9):
                self.grid[x][y].tick()
                car = self.grid.grid[x][y].get_car()
                self.cli.set_cell(self.cli.grid, x, y, f'{car}')
                x+=1
            y+=1
        self.cli.print_grid(self.cli.grid)

if __name__ == "__main__":
    main = Main()
    main.run()