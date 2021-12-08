with open("Day8Input") as f:
    puzzle = f.read().split("\n")
    lines = []
    for i in puzzle:
        currentline = i.split(" | ")
        lines.append((currentline[0].split(" "), currentline[1].split(" ")))


#PART 1
def part1():
    count = 0
    for j in lines:
        for i in j[1]:
            if len(i) == 2 or len(i) == 4 or len(i) == 3 or len(i) == 7:
                count += 1
    return count

#PART 2
"""first step: find all of the easy numbers, so 1, 4, 7, 8. Then loop through again to find 6, 9, and 0,
using the fact that all of the "bars" in 4 are in 9, and 7 would be in 0, but not in 6
Do similar deduction using sets for the rest of the numbers, using sets to determin which outputs go to which number"""
def part2():
    processedlines = []
    for segment in lines:
        signals = {}
        outputline = []
        outputstring = ""
        for i in segment[0]:
            if len(i) == 2:
                signals[i] = 1
                signals[1] = set(x for x in i)
            elif len(i) == 4:
                signals[i] = 4
                signals[4] = set(x for x in i)
            elif len(i) == 3:
                signals[i] = 7
                signals[7] = set(x for x in i)
            elif len(i) == 7:
                signals[i] = 8
                signals[8] = set(x for x in i)
        for i in segment[0]:
            if len(i) == 6:
                setI = set(x for x in i)

                if signals[4].issubset(setI):
                    signals[i] = 9
                    signals[9] = set(x for x in i)
                elif signals[7].issubset(setI):
                    signals[i] = 0
                    signals[0] = set(x for x in i)
                else:
                    signals[i] = 6
                    signals[6] = set(x for x in i)


        for i in segment[0]:
            if len(i) == 5:
                setI = set(x for x in i)
                if signals[7].issubset(setI):
                    signals[i] = 3
                    signals[3] = set(x for x in i)
                elif setI.issubset(signals[9]):
                    signals[i] = 5
                    signals[5] = set(x for x in i)
                else:
                    signals[i] = 2
                    signals[2] = set(x for x in i)
        for i in segment[1]:
            setI = {x for x in i}
            for j in range(10):
                if setI == signals[j]:
                    outputline.append(j)
        for i in outputline:
            outputstring += str(i)
        processedlines.append(int(outputstring))
    return sum(processedlines)


if __name__ == "__main__":
    print("Part 1 Answer:")
    print(part1())
    print("Part 2 Answer:")
    print(part2())

