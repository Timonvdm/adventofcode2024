UP = 0
RIGHT = 90
DOWN = 180
LEFT = 270

class GuardRoute():
    grid = []
    guard = []

    def __init__(self):

        with open('input.txt', encoding="UTF-8", mode="r") as file:
            lines = file.readlines()

            #create the grid
            for y, line in enumerate(lines):
                for x, char in enumerate(line):
                    if char == '^':
                        self.guard = Guard(x, y)

                self.grid.append(list(line.strip()))


    def part1(self):
        outofbounds = False

        while not outofbounds:
            try:
                if self.guard.y < 0 or self.guard.x < 0:
                    raise IndexError()
                
                self.grid[self.guard.y][self.guard.x] = "X"
                
                self.guard.detect_collission(self.grid)
                self.guard.move()

            except IndexError:
                #out of grid, end walk
                outofbounds = True
                for lines in self.grid:
                    print("".join(lines))
                print(f"Distinct positions the guard has been: {self.count_distinct_positions()}")

    #Count the unique positions the guard has walked
    def count_distinct_positions(self):
        counter = 0
        for y, line in enumerate(self.grid):
                for x, char in enumerate(line):
                    if char == 'X':
                        counter += 1
        return counter
        

class Guard():
    x = 0
    y = 0
    heading = UP

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        if self.heading == 360:
            self.heading = 0

        if self.heading == UP:
            self.y -= 1
        elif self.heading == RIGHT:
            self.x += 1
        elif self.heading == DOWN:
            self.y += 1
        elif self.heading == LEFT:
            self.x -= 1
    
    def detect_collission(self, grid):
        if ((self.heading == UP and grid[self.y-1][self.x] == '#') or 
            (self.heading == RIGHT and grid[self.y][self.x+1] == '#') or 
            (self.heading == DOWN and grid[self.y+1][self.x] == '#') or 
            (self.heading == LEFT and grid[self.y][self.x-1] == '#')):
            self.heading += 90

if __name__=="__main__":
    gru = GuardRoute()
    gru.part1()
