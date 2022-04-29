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
    combinations = {}
    counts = {}
    firstletter = starter[0]
    for i in puzzle[2:]:
        k, v = i.split(" -> ")
        rules[k] = v
        combinations[k] = 0

    for i in starter:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1

    for v, w in zip(starter[:-1], starter[1:]):
        combinations[v+w] += 1

    for j in range(40):
        changes = []
        for i in combinations.keys():
            if combinations[i] > 0:
                firstletter, secondletter, middleletter = i[0], i[1], rules[i]
                # using "changes" to avoid changing the list as we iterate over it
                changes.append((firstletter + middleletter, combinations[i]))
                changes.append((middleletter + secondletter,  combinations[i]))
                changes.append((firstletter + secondletter, -combinations[i]))

        # add changes to the combinations dictionary and update counts
        for k, v in changes:
            # counts only update on the changes where a letter is added, which also removes a combination
            if v < 0 and rules[k] in counts:
                counts[rules[k]] -= v
            elif v < 0 and rules[k] not in counts:
                counts[rules[k]] = -v
            combinations[k] += v


    bestcount = 0
    worstcount = 24998671673256760416
    bestletter, worstletter = 0, 0
    for i in counts.keys():
        if counts[i] > bestcount:
            bestcount = counts[i]
            bestletter = i
        elif counts[i] < worstcount:
            worstcount = counts[i]
            worstletter = i
    #print(bestcount, bestletter, worstcount, worstletter)
    return bestcount - worstcount



if __name__ == "__main__":
    print("Part 1 Answer:")
    print(part1())
    print("Part 2 Answer:")
    print(part2())