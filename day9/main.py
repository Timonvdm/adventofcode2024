class DiskMapper():
    input = []

    def __init__(self):

        with open('input.txt', encoding="UTF-8", mode="r") as file:
            self.input = list(file.read())
            # print(self.input)


    #Part 1 of the challenge
    def part1(self):
        #Translate to individual blocks
        translated = self.translate_blocks(self.input)
        blocks = self.reorganize_blocks(translated)
        checksum = self.calculate_checksum(blocks)
        
        print(f"Resulting (fragmented) filesystem checksum: {checksum}")

    #Part 2 of the challenge
    def part2(self):
        translated = self.translate_blocks(self.input)
        blocks = self.reorganize_files(translated)
        checksum = self.calculate_checksum(blocks)

        print(f"Resulting (unfragmented) filesystem checksum: {checksum}")
       
    #Translate input to blocks in filesystem
    def translate_blocks(self, input):
        output = []

        block_id = 0
        for index, amount in enumerate(input):
            block = '.'
            if index % 2 == 0:
                block = block_id
                block_id += 1
            
            for i in range(int(amount)):
                output.append(str(block))

        return output

    #Reorganize the blocks so all BLOCKS are at the beginning of the hard drive (fragmented)
    def reorganize_blocks(self, input):
        output = input

        for index, block in enumerate(output):
            if block == '.':
                #Get last value that is not a dot
                index2 = 0
                for i, e in enumerate(reversed(output)):
                    if not e == '.':
                        index2 = len(output) - i - 1
                        break

                #swap
                if index2 > 0 and index2 > index:
                    temp = output[index]
                    output[index] = output[index2]
                    output[index2] = temp

        return output

    #Reorganize the blocks so all FILES are at the beginning of the hard drive (UNfragmented)
    def reorganize_files(self, input):
        output = input

        #Get highest nr in the list
        for nr in reversed(range(1, int(max(output)) + 1)):
            file_pos = [i for i, x in enumerate(output) if x == str(nr)]

            #Find first occurence of empty space with the minimum length in the list
            empty_space_pos = self.find_empty_space_by_size(output, len(file_pos))

            if len(empty_space_pos) > 0 and empty_space_pos[0] < file_pos[0]:
                #Replace (part of) them with the file
                for index, block in enumerate(file_pos):
                    index2 = empty_space_pos[index]
                    temp = output[block]
                    output[block] = output[index2]
                    output[index2] = temp

        return output

    #Find the first bit of empty space with a specific size
    def find_empty_space_by_size(self, blocks, size):
        empty_space_pos = []
        found = False
        for i, x in enumerate(blocks):
            if x == '.':
                empty_space_pos.append(i)
            else:
                empty_space_pos.clear()

            #Found it, get to the chopper!!!
            if len(empty_space_pos) == size:
                found = True
                break

        return empty_space_pos if found else []
    
    #Calculate the checksum of the full drive
    def calculate_checksum(self, input):
        total = 0
        for index, block in enumerate(input):
            if not block == '.':
                total += (index * int(block))

        return total

if __name__=="__main__":
    dma = DiskMapper()

    dma.part1()
    dma.part2()