import itertools

class AntidotePlacer():
    grid = []
    antennas = {}

    def __init__(self):

        with open('input.txt', encoding="UTF-8", mode="r") as file:
            lines = file.readlines()

            #create the grid
            for y, line in enumerate(lines):
                self.grid.append(list(line.strip()))

                for x, char in enumerate(line.strip()):
                    if not char == '.':
                        if not char in self.antennas:
                            self.antennas[char] = []

                        self.antennas[char].append([x, y])

    #TODO: The horror of this. I should probably learn more about itertools etc
    def part1(self):
        #Get unique antenna frequencies
        antidotes = []
        
        for freq in self.antennas.keys():
            combinations = []

            #Generate all possible combinations
            for index, coords in enumerate(self.antennas[freq]):
                length = len(self.antennas[freq])
                
                for i in range(index+1, length):
                    combinations.append([coords,self.antennas[freq][i]])

            #Calculate antidote for each combination
            for combination in combinations:
                
                loc_a = combination[0]
                loc_b = combination[1]
                diff_x = loc_a[0] - loc_b[0]
                diff_y = loc_a[1] - loc_b[1]
                
                #Filter out values that are out of bounds 
                #TODO: For lack of a better way to do this 
                if  (0 <= (loc_a[0] + diff_x) <= len(self.grid[0])-1 and
                    0 <= (loc_a[1] + diff_y) <= len(self.grid)-1):
                    #Add antidote 1
                    antidotes.append([loc_a[0] + diff_x, loc_a[1] + diff_y])
                if (0 <= (loc_b[0] - diff_x) <= len(self.grid[0])-1 and
                    0 <= (loc_b[1] - diff_y) <= len(self.grid)-1):
                    #Add antidote 2
                    antidotes.append([loc_b[0] - diff_x, loc_b[1] - diff_y])
        
        #Sort and filter out duplicates
        antidotes.sort()
        antidotes = list(k for k,_ in itertools.groupby(antidotes))
        print(f"Amount of unique antidote antennas on the grid: {len(antidotes)}")

if __name__=="__main__":
    apl = AntidotePlacer()

    apl.part1()