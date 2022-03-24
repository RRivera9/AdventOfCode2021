with open("Day13Input") as f:
    puzzle = f.read().split("\n")

#This really should be a class. I'm doing way too much here.
def part1():
    dots = []
    folds = []
    grid = {}
    max_x, max_y = 0, 0
    dottotal = 0
    for i in puzzle:
        if i == "":
            pass
        elif i[0] == "f":
            fold, number = i.split("=")
            fold = fold[-1]
            folds.append((fold, int(number)))
        else:
            x, y = i.split(",")
            x, y = int(x), int(y)
            dots.append((int(x), int(y)))
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y
    for i in range(max_x+10):
        for j in range(max_y+10):
            grid[(i, j)] = "."
    for i in dots:
        grid[i[0], i[1]] = "#"

    def dotCount(oldgrid, maximum_x, maximum_y):
        dotcount = 0
        for i in range(maximum_x+1):
            for j in range(maximum_y+1):
                if oldgrid[(i, j)] == "#":
                    dotcount += 1
        return dotcount

    #Folds to the left, the coord is an X, but it shifts each X along a line
    def foldLeft(coordX, oldgrid, maximum_y):
        newgrid = {}
        for i in range(coordX+1):
            for j in range(maximum_y+1):
                if i == coordX:
                    newgrid[(i,j)] = "."
                elif oldgrid[(i,j)] == "#" or oldgrid[(-i+coordX*2, j)] == "#":
                    newgrid[(i,j)] = "#"
                else:
                    newgrid[(i,j)] = "."
        return newgrid

    def foldUp(coordX, oldgrid, maximum_x):
        newgrid = {}
        for i in range(maximum_x+1):
            for j in range(coordX):
                if j == coordX:
                    newgrid[(i, j)] = "."
                elif oldgrid[(i,j)] == "#" or oldgrid[(i, -i+2*coordX)] == "#":
                    newgrid[(i,j)] = "#"
                else:
                    newgrid[(i,j)] = "."
        return newgrid

    def printGrid(oldgrid, maximum_x, maximum_y):
        for j in range(maximum_y):
            line = ""
            for i in range(maximum_x):
                if oldgrid[(i, j)] == "#":
                    line += "#"
                else:
                    line += "."
            print(line)

    for fold in [folds[0]]:
        if fold[0] == "x":
            grid = foldLeft(fold[1], grid, max_y)
            max_x = fold[1]
        elif fold[1] == "y":
            grid = foldUp(fold[1], grid, max_x)
            max_y = fold[1]



    return dotCount(grid, max_x, max_y)



def part2():
    dots = []
    folds = []
    grid = {}
    max_x, max_y = 0, 0
    dottotal = 0
    for i in puzzle:
        if i == "":
            pass
        elif i[0] == "f":
            fold, number = i.split("=")
            fold = fold[-1]
            folds.append((fold, int(number)))
        else:
            x, y = i.split(",")
            x, y = int(x), int(y)
            dots.append((int(x), int(y)))
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y
    for i in range(max_x + 10):
        for j in range(max_y + 10):
            grid[(i, j)] = "."
    for i in dots:
        grid[i[0], i[1]] = "#"

    def dotCount(oldgrid, maximum_x, maximum_y):
        dotcount = 0
        for i in range(maximum_x + 1):
            for j in range(maximum_y + 1):
                if oldgrid[(i, j)] == "#":
                    dotcount += 1
        return dotcount

    # Folds to the left, the coord is an X, but it shifts each X along a line
    def foldLeft(coordX, oldgrid, maximum_y):
        newgrid = {}
        for i in range(coordX + 1):
            for j in range(maximum_y + 1):
                if i == coordX:
                    newgrid[(i, j)] = "."
                elif oldgrid[(i, j)] == "#" or oldgrid[(-i + coordX * 2, j)] == "#":
                    newgrid[(i, j)] = "#"
                else:
                    newgrid[(i, j)] = "."
        return newgrid

    def foldUp(coordX, oldgrid, maximum_x):
        newgrid = {}
        for i in range(maximum_x + 1):
            for j in range(coordX+1):
                if j == coordX:
                    newgrid[(i, j)] = "."
                elif oldgrid[(i, j)] == "#" or oldgrid[(i, -j + 2 * coordX)] == "#":
                    newgrid[(i, j)] = "#"
                else:
                    newgrid[(i, j)] = "."
        return newgrid

    def printGrid(oldgrid, maximum_x, maximum_y):
        for j in range(maximum_y):
            line = ""
            for i in range(maximum_x):
                if oldgrid[(i, j)] == "#":
                    line += "#"
                else:
                    line += "."
            print(line)


    for fold in folds:
        if fold[0] == "x":
            grid = foldLeft(fold[1], grid, max_y)
            max_x = fold[1]
        elif fold[0] == "y":
            print("ding")
            grid = foldUp(fold[1], grid, max_x)
            max_y = fold[1]

    return printGrid(grid, max_x, max_y)



if __name__ == "__main__":
    print("Part 1 Answer:")
    print(part1())
    print("Part 2 Answer:")
    print(part2())