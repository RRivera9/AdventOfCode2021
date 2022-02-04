import itertools

with open("Day11Input") as f:
    puzzle = f.read().split("\n")

def flash(pointX, pointY):
    all_x = [pointX, pointX-1, pointX+1]
    all_x = list(filter(lambda a: a != -1, all_x))
    all_x = list(filter(lambda a: a != 10, all_x))
    all_y = [pointY, pointY-1, pointY+1]
    all_y = list(filter(lambda a: a != -1, all_y))
    all_y = list(filter(lambda a: a != 10, all_y))
    all_points = list(itertools.product(all_x, all_y))
    return all_points

def part1():
    grid = {}
    for i, w in enumerate(puzzle):
        for j, v in enumerate(w):
            grid[(j, i)] = int(v)

    flashes = 0
    for steps in range(100):
        flashing = set()
        currentflashes = []
        for i in range(10):
            for j in range(10):
                grid[i, j] += 1
                if grid[i, j] >= 10:
                    flashing.add((i, j))
                    currentflashes.append((i, j))

        while len(currentflashes) > 0:
            octopusLocation = currentflashes.pop()
            increment = flash(octopusLocation[0], octopusLocation[1])
            #print(increment, flashing)
            increment = [x for x in increment if x not in flashing]
            #print(increment, flashing)
            for point in increment:
                grid[(point[0], point[1])] += 1
                if grid[(point[0], point[1])] >= 10:
                    flashing.add((point[0], point[1]))
                    currentflashes.append((point[0], point[1]))

        #print(flashing)

        for i, j in flashing:
            #print(i, j)
            grid[(i, j)] = 0
            flashes += 1
        #print(grid.values(), steps)

    return flashes


def part2():
    grid = {}
    for i, w in enumerate(puzzle):
        for j, v in enumerate(w):
            grid[(j, i)] = int(v)

    for steps in range(1000):
        flashing = set()
        currentflashes = []
        for i in range(10):
            for j in range(10):
                grid[i, j] += 1
                if grid[i, j] >= 10:
                    flashing.add((i, j))
                    currentflashes.append((i, j))

        while len(currentflashes) > 0:
            octopusLocation = currentflashes.pop()
            increment = flash(octopusLocation[0], octopusLocation[1])
            # print(increment, flashing)
            increment = [x for x in increment if x not in flashing]
            # print(increment, flashing)
            for point in increment:
                grid[(point[0], point[1])] += 1
                if grid[(point[0], point[1])] >= 10:
                    flashing.add((point[0], point[1]))
                    currentflashes.append((point[0], point[1]))

        # print(flashing)

        for i, j in flashing:
            # print(i, j)
            grid[(i, j)] = 0
        # print(grid.values(), steps)
        if len(flashing) == 100:
            return steps+1



if __name__ == "__main__":
    print("Part 1 Answer:")
    print(part1())
    print("Part 2 Answer:")
    print(part2())