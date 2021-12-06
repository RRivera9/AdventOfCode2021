with open("Day6Input") as f:
    puzzle = f.read().split(",")


#PART 1
def part1():
    lanturns = []
    for i in puzzle:
        lanturns.append(int(i))
    count = 80
    while count > 0:
        newlanturns = []
        for i in lanturns:
            if i == 0:
                newlanturns.append(6)
                newlanturns.append(8)
            else:
                newlanturns.append(i-1)
        lanturns = newlanturns
        count -= 1
    return len(lanturns)



#PART 2
def part2():
    lanturns = {x: 0 for x in range(9)}
    for i in puzzle:
        lanturns[int(i)] += 1
    count = 256
    total = 0
    while count > 0:
        newlanturns = {x: 0 for x in range(9)}
        for i in range(9):
            if i == 0:
                newlanturns[6] += lanturns[i]
                newlanturns[8] += lanturns[i]
            else:
                newlanturns[i-1] += lanturns[i]
        lanturns = newlanturns
        count -= 1
    for i in range(9):
        total += lanturns[i]
    return total



if __name__ == "__main__":
    print("Part 1 Answer:")
    print(part1())
    print("Part 2 Answer:")
    print(part2())

