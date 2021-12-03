with open("Day2Input") as f:
    puzzle = f.read().split("\n")

#PART 1
def part1():
    horizontal = 0
    vertical = 0
    for i in puzzle:
        magnitude = int(i[-1])
        if i[0][0] == "f":
            horizontal += magnitude
        elif i[0][0] == "d":
            vertical += magnitude
        elif i[0][0] == "u":
            vertical -= magnitude
    return horizontal*vertical

#PART 2
def part2():
    horizontal = 0
    vertical = 0
    aim = 0
    for i in puzzle:
        magnitude = int(i[-1])
        if i[0][0] == "f":
            horizontal += magnitude
            vertical += aim * magnitude
        elif i[0][0] == "d":
            aim += magnitude
        elif i[0][0] == "u":
            aim -= magnitude
    return horizontal*vertical


if __name__ == "__main__":
    print("Part 1 Answer:")
    print(part1())
    print("Part 2 Answer:")
    print(part2())




