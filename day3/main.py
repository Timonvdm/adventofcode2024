import re

#Sums up all the multipliers filtered by the regexp
def sumup_multipliers(input):
    matches = re.findall("mul\(([0-9]{1,3}),([0-9]{1,3})\)", input)

    total = 0
    for match in matches:
        total += int(match[0]) * int(match[1])
    return total


with open('input.txt', newline='') as file:
    input = file.read()

    #Part 1
    total = sumup_multipliers(input)
    print(f"Sum of all mul instructions (part 1): {total}")

    #Part 2
    #TODO: Not a very clean way to do it. The split creates a result that is relies on process flags to work
    # There is probably a better way to do this
    #Split the input on do() and don't()
    result = re.split('(do\(\))|(don\'t\(\))', input)
    total = 0
    process = True
    for res in result:
        # Skip the nonetypes
        if (res):
            
            #Only process if our last instruction was do()
            if process:
                total += sumup_multipliers(res)

            if res == 'do()':
                process = True
            elif res == 'don\'t()':
                process = False
            
    print(f"Sum of all mul instructions we should process (part 2): {total}")