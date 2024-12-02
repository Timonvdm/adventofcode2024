import csv

#Test the row for the safe report conditions (all steps are between 1 and 3)
def test_row(row):
    differences = [j - i for i, j in zip(row[:-1], row[1:])]
            
    if len([x for x in differences if x > 3 or x < 1]) == 0:
        return True
    return False


counter_part1 = 0
counter_part2 = 0
with open('input.txt', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
        #Convert to int
        row = [int(item) for item in row]

        #Flip when decreasing
        if row[0] > row[-1]:
            row.reverse()

        #Exclude rows that do not increase or decrease
        if not row[0] == row[-1]:

            #Safe reports without removing a value
            if test_row(row) == True:
                counter_part1 += 1
            else:
                #Try to remove a value and test the report again
                for i in range(0, len(row)):
                    temp_row = [x for index, x in enumerate(row) if index != i]
                    if test_row(temp_row) == True:
                        counter_part2 += 1
                        break
                    
print(f"Safe reports part one: {counter_part1}")
print(f"Safe reports after removing a value: {counter_part2}")
print(f"Safe reports part two: {counter_part1 + counter_part2}")
        