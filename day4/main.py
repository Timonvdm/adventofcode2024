class CrossWordSearch():
    grid = []

    def __init__(self):

        with open('input.txt', encoding="UTF-8", mode="r") as file:
            lines = file.readlines()

            #create the grid
            for line in lines:
                self.grid.append(list(line.strip()))


    #Starter for part 1 where we search for a specific string in all directions
    def part1(self, searchfor):
        occurences = 0
        for y, row in enumerate(self.grid):
            for x, char in enumerate(row):
                #Find first char
                if char == list(searchfor)[0]:

                    occurences += self.find_horizontally(searchfor, x, y)
                    occurences += self.find_horizontally(searchfor, x, y, True) #Reverse
                    occurences += self.find_vertically(searchfor, x, y)
                    occurences += self.find_vertically(searchfor, x, y, True)
                    occurences += self.find_diagonally(searchfor, x, y)
                    occurences += self.find_diagonally(searchfor, x, y, True)
                    occurences += self.find_diagonally_other(searchfor, x, y)
                    occurences += self.find_diagonally_other(searchfor, x, y, True)

        print(f"The amount of {searchfor} in the wordsearch is {occurences}")

    #Starter for part 2 where we search for a crosses MAS (X-MAS)
    def part2(self):
        occurences = 0
        for y, row in enumerate(self.grid):
            for x, char in enumerate(row):

                #Start with the A
                if char == "A":
                    #Get the characters around the A in a cross
                    cross = self.get_cross(x,y)
                    #Check output if it matches. Chars go left top, right top, right bottom,
                    # left bottom
                    if cross in ['MMSS', 'SMMS', 'SSMM', 'MSSM']:
                        #print(f"Found X-MAS cross on {x},{y} with cross {cross}")
                        occurences += 1

        print(f"Found a whopping total of X-MAS crosses: {occurences}")


    #Get cross letters from starting point
    def get_cross(self, x, y):
        try:
            #Cannot find cross along left border, others are handled by out of bounds issues
            if y == 0:
                raise IndexError()

            result = [
                self.grid[y-1][x-1],
                self.grid[y-1][x+1],
                self.grid[y+1][x+1],
                self.grid[y+1][x-1]
            ]
        except IndexError:
            return ""

        return "".join(result)

    #Find searchfor horizontally from starting position
    def find_horizontally(self, searchfor, x, y, rev = False):
        for index, char in enumerate(list(searchfor)):
            try:
                newx = x+(index if not rev else index * -1)
                if newx < 0:
                    raise IndexError()

                if not self.grid[y][newx] == char:
                    return False
            except IndexError:
                return False

        #print(f"Found {searchfor} horizontally{' (reverse)' if rev else ''} on {x},{y}")
        return True

    #Find searchfor vertically from starting position
    def find_vertically(self, searchfor, x, y, rev = False):
        for index, char in enumerate(list(searchfor)):
            try:
                newy = y+(index if not rev else index * -1)
                if newy < 0:
                    raise IndexError()

                if not self.grid[newy][x] == char:
                    return False
            except IndexError:
                return False

        #print(f"Found {searchfor} vertically{' (reverse)' if rev else ''} on {x},{y}")
        return True

    #Find searchfor diagonally (top-left to bottom-right) from starting position
    def find_diagonally(self, searchfor, x, y, rev = False):
        for index, char in enumerate(list(searchfor)):
            try:
                newx = x+(index if not rev else index * -1)
                newy = y+(index if not rev else index * -1)
                if newx < 0 or newy < 0:
                    raise IndexError()

                if not self.grid[newy][newx] == char:
                    return False
            except IndexError:
                return False

        #print(f"Found {searchfor} diagonally{' (reverse)' if rev else ''} on {x},{y}")
        return True

    #TODO: Better name for this one?
    #Find searchfor diagonally (bottom-left to top-right) from starting position
    def find_diagonally_other(self, searchfor, x, y, rev = False):
        for index, char in enumerate(list(searchfor)):
            try:
                newx = x-(index if not rev else index * -1)
                newy = y+(index if not rev else index * -1)
                if newx < 0 or newy < 0:
                    raise IndexError()

                if not self.grid[newy][newx] == char:
                    return False
            except IndexError:
                return False

        #print(f"Found {searchfor} diagonally other{' (reverse)' if rev else ''} on {x},{y}")
        return True


if __name__=="__main__":
    cws = CrossWordSearch()
    cws.part1('XMAS')
    cws.part2()
