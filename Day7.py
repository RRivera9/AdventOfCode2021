import math

with open("Day7Input") as f:
    puzzle = f.read().split(",")

#PART 1
def part1():
    crabs = [int(x) for x in puzzle]
    bestcount = 100000000
    bestmean = 0
    for j in range(1000):
        count = 0
        for i in crabs:
            diff = abs(i - j)
            count += diff
        if count < bestcount:
            bestcount = count
            bestmean = j
    return bestcount, bestmean

#PART 2
def part2():
    crabs = [int(x) for x in puzzle]
    bestcount = 100000000
    bestpos = 0
    for j in range(1000):
        count = 0
        for i in crabs:
            diff = crabdif(i, j)
            count += diff
        if count < bestcount:
            bestcount = count
            bestpos = j
    return bestcount, bestpos

def crabdif(start, goal):
    diff = abs(start - goal)
    fuel = (diff)*(diff+1) / 2
    return int(fuel)

if __name__ == "__main__":
    print("Part 1 Answer:")
    print(part1())
    print("Part 2 Answer:")
    print(part2())

