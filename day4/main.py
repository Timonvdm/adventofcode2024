class WordSearch():

    grid = []
    searchfor = ''
    occurences = 0

    def __init__(self, searchfor):
        self.searchfor = searchfor

        with open('input.txt', encoding="UTF-8", mode="r") as file:
            lines = file.readlines()

            #create the grid
            for line in lines:
                self.grid.append(list(line.strip()))


    def start(self):
        for y, row in enumerate(self.grid):
            for x, char in enumerate(row):
                #Find first char
                if char == list(self.searchfor)[0]:

                    self.occurences += self.find_horizontally(x, y)
                    self.occurences += self.find_horizontally(x, y, True) #Reverse
                    self.occurences += self.find_vertically(x, y)
                    self.occurences += self.find_vertically(x, y, True)
                    self.occurences += self.find_diagonally(x, y)
                    self.occurences += self.find_diagonally(x, y, True)
                    self.occurences += self.find_diagonally_other(x, y)
                    self.occurences += self.find_diagonally_other(x, y, True)

        print(f"The amount of {self.searchfor} in the wordsearch is {self.occurences}")

    #Find searchfor horizontally from starting position
    def find_horizontally(self, x, y, rev = False):
        for index, char in enumerate(list(self.searchfor)):
            try:
                newx = x+(index if not rev else index * -1)
                if newx < 0:
                    raise IndexError()

                if not self.grid[y][newx] == char:
                    return False
            except IndexError:
                return False

        print(f"Found {self.searchfor} horizontally{' (reverse)' if rev else ''} on {x},{y}")
        return True

    #Find searchfor vertically from starting position
    def find_vertically(self, x, y, rev = False):
        for index, char in enumerate(list(self.searchfor)):
            try:
                newy = y+(index if not rev else index * -1)
                if newy < 0:
                    raise IndexError()

                if not self.grid[newy][x] == char:
                    return False
            except IndexError:
                return False

        print(f"Found {self.searchfor} vertically{' (reverse)' if rev else ''} on {x},{y}")
        return True

    #Find searchfor diagonally (top-left to bottom-right) from starting position
    def find_diagonally(self, x, y, rev = False):
        for index, char in enumerate(list(self.searchfor)):
            try:
                newx = x+(index if not rev else index * -1)
                newy = y+(index if not rev else index * -1)
                if newx < 0 or newy < 0:
                    raise IndexError()

                if not self.grid[newy][newx] == char:
                    return False
            except IndexError:
                return False

        print(f"Found {self.searchfor} diagonally{' (reverse)' if rev else ''} on {x},{y}")
        return True

    #TODO: Better name for this one?
    #Find searchfor diagonally (bottom-left to top-right) from starting position
    def find_diagonally_other(self, x, y, rev = False):
        for index, char in enumerate(list(self.searchfor)):
            try:
                newx = x-(index if not rev else index * -1)
                newy = y+(index if not rev else index * -1)
                if newx < 0 or newy < 0:
                    raise IndexError()

                if not self.grid[newy][newx] == char:
                    return False
            except IndexError:
                return False

        print(f"Found {self.searchfor} diagonally other{' (reverse)' if rev else ''} on {x},{y}")
        return True


if __name__=="__main__":
    finder = WordSearch('XMAS')
    finder.start()
