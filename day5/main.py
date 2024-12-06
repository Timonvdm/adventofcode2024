class PrinterUpdates():
    rules = []
    updates = []

    def __init__(self):

        with open('input.txt', encoding="UTF-8", mode="r") as file:
            lines = file.readlines()

            #create the grid
            for line in lines:
                #Rules
                if "|" in line:
                    self.rules.append(list(map(int,line.strip().split('|'))))
                #Updates
                elif "," in line:
                    self.updates.append(list(map(int,line.strip().split(','))))

    def start(self):

        correct_sum = 0
        corrected_sum = 0
        for update in self.updates:
            #Part 1
            if self.check_rules(update):
                #Find middle number and add it to the sum
                correct_sum += update[int((len(update) - 1)/2)]
            #Part 2
            else:
                correct = False
                while not correct:
                    correct = self.enforce_rules(update)

                corrected_sum += update[int((len(update) - 1)/2)]

        print(f"Summed up the middle page numbers of CORRECT ordered updates for you (bliep bloep): {correct_sum}")
        print(f"Summed up the middle page numbers of CORRECTED ordered updates for you (bliep bloep): {corrected_sum}")

    #Check if the update respects the rules
    def check_rules(self, update):
        for rule in self.rules:
            if rule[0] in update and rule[1] in update and update.index(rule[0]) > update.index(rule[1]):
                return False
        return True
    
    #Enforce the rules that are not respected and double check
    def enforce_rules(self, update):
        for rule in self.rules:
            if rule[0] in update and rule[1] in update and update.index(rule[0]) > update.index(rule[1]):
                update.insert(update.index(rule[1]), update.pop(update.index(rule[0])))

        #Double check to be certain
        return self.check_rules(update)
            

if __name__=="__main__":
    pus = PrinterUpdates()
    pus.start()
