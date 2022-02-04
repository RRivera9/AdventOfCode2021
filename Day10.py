with open("Day10Input") as f:
    puzzle = f.read().split("\n")

starter = {"<", "(", "[", "{"}
ender = {">", ")", "]", "}"}
matching = {">":"<", ")":"(", "]":"[", "}":"{", "<":">", "(":")", "[":"]", "{":"}"}
value = {">":25137, ")":3, "]":57, "}":1197}
repair = {">":4, ")":1, "]":2, "}":3}

def isStarter(character):
    if character in starter:
        return True
    elif character in ender:
        return False

def part1():
    linescore = 0
    for line in puzzle:
        currentline = line
        starterStack = []
        for letter in currentline:
            if letter in starter:
                starterStack.append(letter)
            elif letter in ender:
                if matching[letter] == starterStack.pop():
                    continue
                else:
                    linescore += value[letter]
                    break

        if len(starterStack) > 0:
            pass
        elif len(starterStack) == 0:
            pass

    return linescore




def part2():
    allScores = []

    for line in puzzle:
        currentline = line
        starterStack = []
        score = 0
        error = False
        for letter in currentline:
            if letter in starter:
                starterStack.append(letter)
            elif letter in ender:
                if matching[letter] == starterStack.pop():
                    pass
                else:
                    error = True
                    break

        if len(starterStack) > 0 and not error:
            while len(starterStack) > 0:
                score *= 5
                score += repair[matching[starterStack.pop()]]
            allScores.append(score)

    allScores = sorted(allScores)
    length = len(allScores)
    middle = int(length/2)
    return allScores[middle]

if __name__ == "__main__":
    print("Part 1 Answer:")
    print(part1())
    print("Part 2 Answer:")
    print(part2())