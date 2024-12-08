import itertools
from toolz import itertoolz
import operator


class Calibrator():
    calculations = []
    operators = {
        '+': operator.add, 
        '*': operator.mul,
        # '||': ''
    }
    
    def __init__(self):

        with open('input.txt', encoding="UTF-8", mode="r") as file:
            lines = file.readlines()

            for line in lines:
                self.calculations.append(line.strip().split(":"))

    #Main function for calculations
    def calculate(self):
        result = 0
        for calc in self.calculations:
            nrs = calc[1].strip().split(" ")

            #Generate all options for operators between each number
            for ops in itertools.product(*[ self.operators ], repeat=len(nrs)-1):
                #Generate sum with these operators
                sum = list(itertoolz.interleave([nrs, ops]))

                total = int(sum[0])
                #Start with the first number and handle each operator and following number
                for i in range(2, len(sum), 2):
                    #Handle the concat operator by concatenating the number
                    if (sum[i-1] == '||'):
                        total = int(str(total) + sum[i])
                    else:
                        op_func = self.operators[sum[i-1]]
                        total = op_func(total, int(sum[i]))

                if int(calc[0]) == total:
                    result += total
                    break

        print(f"Total calibration result: {result}")


if __name__=="__main__":
    cab = Calibrator()

    #Part 1 uses only + and * operators
    #Part 2 also uses the || operator
    cab.calculate()