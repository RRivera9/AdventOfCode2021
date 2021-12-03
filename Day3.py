

with open("Day3Input") as f:
    puzzle = f.read().split("\n")

def getEpsilonOmega(input):
    epsilon = ""
    omega = ""
    commonThreshold = len(input) / 2
    for j in range(0, len(input[0])):
        count = 0
        for value in input:
            if value[j] == "1":
                count += 1
        if count >= commonThreshold:
            epsilon += "1"
            omega += "0"
        else:
            epsilon += "0"
            omega += "1"
    return epsilon, omega

#PART 1
def part1():
    epsilon, omega = getEpsilonOmega(puzzle)
    return int(epsilon,2) * int(omega,2)


#PART 2
def part2():

    mostCommon = puzzle.copy()
    leastCommon = puzzle.copy()
    for j in range(0, len(puzzle[0])):
        epsilon1, omega1 = getEpsilonOmega(mostCommon)
        epsilon2, omega2 = getEpsilonOmega(leastCommon)

        #make this a lambda function in future
        def isIndexSameEspilon(x):
            if x[j] == epsilon1[j]:
                return True
            else:
                return False

        def isIndexSameOmega(x):
            if x[j] == omega2[j]:
                return True
            else:
                return False

        if len(mostCommon) != 1:
            mostCommon = list(filter(isIndexSameEspilon, mostCommon))
        if len(leastCommon) != 1:
            leastCommon = list(filter(isIndexSameOmega, leastCommon))

        print(f'{j =} {mostCommon = }  {leastCommon = }')
    return int(mostCommon[0], 2) * int(leastCommon[0], 2)

if __name__ == "__main__":
    print("Part 1 Answer:")
    print(part1())
    print("Part 2 Answer:")
    print(part2())

