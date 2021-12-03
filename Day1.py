with open("Day2Input") as f:
    puzzle = f.read().split("\n")
    puzzle = [int(i) for i in puzzle[0:-1:]]

#PART 1
def increasing():
    previous = puzzle[0]
    counter = 0
    for i in range(1, len(puzzle)):
        current = puzzle[i]
        if current > previous:
            counter += 1
        previous = current
    return counter

#PART 2
def increasingWindow():
    previous = puzzle[0]
    counter = 0
    for i in range(3, len(puzzle)):
        current = puzzle[i]
        if current > previous:
            counter += 1
        previous = puzzle[i-2]
    return counter


if __name__ == "__main__":
    print("Part 1 Answer:")
    print(increasing())
    print("Part 2 Answer:")
    print(increasingWindow())




