import time
from functools import cache

start = time.time()

def part1(blinks):

    with open('input.txt', encoding="UTF-8", mode="r") as file:
        data = file.read()
        stones = (x for x in data.split(" "))

        for i in range(blinks):
            print(f"starting blink nr {i} (Total time = {time.time() - start} seconds)")

            stones_copy = []
            for stone in stones:
                
                new_stones = handle_stone(stone)
                
                #Seems faster than concatenating the lists
                for new_stone in new_stones:
                    stones_copy.append(new_stone)

            stones = stones_copy

        print(f"Amount of stones after {blinks} times blinking = {len(stones)}")
        print(f"Total time = {time.time() - start} seconds")

def part2(blinks):
    with open('input.txt', encoding="UTF-8", mode="r") as file:
        data = file.read()
        stones = (x for x in data.split(" "))

        splits = [count_splits(stone, blinks) for stone in stones]
        print(f"Amount of stones after {blinks} times blinking = {sum(splits)}")
        print(f"Total time = {time.time() - start} seconds")


@cache
def handle_stone(stone):
    if stone == "0":
        return ["1"]
    elif len(stone) % 2 == 0:
        l = int(len(stone) / 2)
        left = stone[:l]
        right = stone[l:]
        return [left, right]            
    else:
        return [str(int(stone) * 2024)]

@cache
#Stole this solution for Marick. Very nice and very fast!
def count_splits(stone, splits):
    if splits == 0:
        return 1
    
    if stone == "0":
        return count_splits("1", splits-1)
    elif len(stone) % 2 == 0:
        l = int(len(stone) / 2)
        left = stone[:l]
        right = stone[l:]
        return count_splits(left, splits-1) + count_splits(right, splits-1)            
    else:
        return count_splits(str(int(stone) * 2024), splits-1)


if __name__=="__main__":
    part1(35)
    part2(75)