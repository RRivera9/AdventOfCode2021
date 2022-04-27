with open("Day14Input") as f:
    puzzle = f.read().split("\n")

def part1():
    starter = puzzle[0]
    rules = {}
    counts = {}
    for i in puzzle[2:]:
        k, v = i.split(" -> ")
        rules[k] = v
    for j in range(10):
        polymer = []
        newpolymer = []
        for v, w in zip(starter[:-1], starter[1:]):
            polymer.append(v+w)
        for pair in polymer:
            if pair in rules:
                trio = pair[0] + rules[pair] + pair[1]
            else:
                trio = pair
            newpolymer.append(trio)
        starter = polymer[0][0]
        for trio in newpolymer:
            starter = starter + trio[1::]
    for letter in starter:
        if letter not in counts:
            counts[letter] = 0
        else:
            counts[letter] += 1
    bestcount = 0
    worstcount = 100000000
    bestletter, worstletter = 0, 0
    for i in counts.keys():
        if counts[i] > bestcount:
            bestcount = counts[i]
            bestletter = i
        elif counts[i] < worstcount:
            worstcount = counts[i]
            worstletter = i
    return bestcount-worstcount



"""Failed my first time attempting this, got some ideas from the subreddit"""
def part2():
    starter = puzzle[0]
    rules = {}
    firstletter = starter[0]
    for i in puzzle[2:]:
        k, v = i.split(" -> ")
        rules[k] = v
    for j in range(40):
        counts = {}
        count = 0
        polymers = []
        newpolymer = {}
        for i in starter:
            newpolymer[count] = i
            count += 1
        print("dict", count)
        for i in range(count-1):
            pair = newpolymer[i] + newpolymer[i+1]
            if pair in rules:
                trio = rules[pair] + newpolymer[i+1]
            else:
                trio = newpolymer[i+1]
            polymers.append(trio)
        print("pair")
        starter = firstletter + "".join(polymers)
        #print(starter, polymers)

        print(j)



    for letter in starter:
        if letter not in counts:
            counts[letter] = 1
        else:
            counts[letter] += 1
    bestcount = 0
    worstcount = 100000000
    bestletter, worstletter = 0, 0
    for i in counts.keys():
        if counts[i] > bestcount:
            bestcount = counts[i]
            bestletter = i
        elif counts[i] < worstcount:
            worstcount = counts[i]
            worstletter = i
    print(bestcount, bestletter, worstcount, worstletter, starter)
    return bestcount - worstcount



if __name__ == "__main__":
    print("Part 1 Answer:")
    print(part1())
    print("Part 2 Answer:")
    print(part2())