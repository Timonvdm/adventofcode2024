class TrailFinder():
    grid = []

    def __init__(self):
        with open('input.txt', encoding="UTF-8", mode="r") as file:
            lines = file.readlines()
            
            #create the grid
            for line in lines:
                self.grid.append(list(line.strip()))

    def start(self):
        #Find all the trail starters
        trails = []
        for y, col in enumerate(self.grid):
            for x, val in enumerate(col):
                if val == '0':
                    trails.append([[x, y]])

        for step in range(1, 10):
            trails_copy = []
            #For each trail starter find a trail
            for trail in trails:
                next_steps = self.find_next_steps(trail[-1], str(step))

                #If trail splits up, create copy and follow along that path
                for next_step in next_steps:
                    trail_copy = trail[:]
                    trail_copy.append(next_step)
                    trails_copy.append(trail_copy)

            trails = trails_copy
            
        #Search for unique combinations of start and end point
        begin_end = []
        for trail in trails:
            begin_end.append([trail[0], trail[-1]])

        unique = []
        [unique.append(val) for val in begin_end if val not in unique]

        print(f"Unique start and end point combinations (part1): {len(unique)}")
        print(f"Unique routes from start to end point (part2): {len(trails)}")


    #Finds next step from starting point in all 4 directions
    def find_next_steps(self, start, step):
        result = []
        #Find up
        if start[1] > 0 and self.grid[start[1]-1][start[0]] == step:
            result.append([start[0], start[1]-1])

        #Find down
        if start[1] < len(self.grid)-1 and self.grid[start[1]+1][start[0]] == step:
            result.append([start[0], start[1]+1])

        #Find left
        if start[0] > 0 and self.grid[start[1]][start[0]-1] == step:
            result.append([start[0]-1, start[1]])

        #Find right
        if start[0] < len(self.grid[0])-1 and self.grid[start[1]][start[0]+1] == step:
            result.append([start[0]+1, start[1]])

        return result


if __name__=="__main__":
    tf = TrailFinder()

    tf.start()