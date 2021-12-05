with open("Day5Input") as f:
    puzzle = f.read().split("\n")

#PART 1
def part1():
    coords = []
    field = {}
    for i in range(1000):
        for j in range(1000):
            field[(i, j)] = 0
    for i in puzzle:
        temp = i.split(" -> ")
        temp1 = temp[0].split(",")
        temp2 = temp[1].split(",")
        temp1[0] = int(temp1[0])
        temp1[1] = int(temp1[1])
        temp2[0] = int(temp2[0])
        temp2[1] = int(temp2[1])
        coords.append((temp1, temp2))

    for i in coords:
        x1 = i[0][0]
        x2 = i[1][0]
        y1 = i[0][1]
        y2 = i[1][1]
        if x1 == x2:
            #could be equal
            if y1 > y2:
                for y_coord in range(y2,y1+1):
                    field[(x1, y_coord)] += 1
            if y2 > y1:
                for y_coord in range(y1,y2+1):
                    field[(x1, y_coord)] += 1
        if y1 == y2:
            if x1 > x2:
                for x_coord in range(x2,x1+1):
                    field[(x_coord, y1)] += 1
            if x2 > x1:
                for x_coord in range(x1,x2+1):
                    field[(x_coord, y1)] += 1

    count = 0
    for i in range(1000):
        for j in range(1000):
            if field[(i, j)] > 1:
                count += 1
    return count


#PART 2
def part2():
    coords = []
    field = {}
    for i in range(1000):
        for j in range(1000):
            field[(i, j)] = 0
    for i in puzzle:
        temp = i.split(" -> ")
        temp1 = temp[0].split(",")
        temp2 = temp[1].split(",")
        temp1[0] = int(temp1[0])
        temp1[1] = int(temp1[1])
        temp2[0] = int(temp2[0])
        temp2[1] = int(temp2[1])
        coords.append((temp1, temp2))

    for i in coords:
        x1 = i[0][0]
        x2 = i[1][0]
        y1 = i[0][1]
        y2 = i[1][1]
        if x1 == x2:
            # could be equal
            if y1 > y2:
                for y_coord in range(y2, y1 + 1):
                    field[(x1, y_coord)] += 1
            if y2 > y1:
                for y_coord in range(y1, y2 + 1):
                    field[(x1, y_coord)] += 1
        elif y1 == y2:
            if x1 > x2:
                for x_coord in range(x2, x1 + 1):
                    field[(x_coord, y1)] += 1
            if x2 > x1:
                for x_coord in range(x1, x2 + 1):
                    field[(x_coord, y1)] += 1

        #This is the only part that's different for part 2
        elif y2 > y1 and x2 > x1:
            for xy_coord in range(0, y2-y1+1):
                field[(x1+xy_coord, y1+xy_coord)] += 1
        elif y1 > y2 and x1 > x2:
            for xy_coord in range(0, y1-y2+1):
                field[(x1-xy_coord, y1-xy_coord)] += 1
        elif y1 > y2 and x2 > x1:
            for xy_coord in range(0, y1-y2+1):
                field[(x1+xy_coord, y1-xy_coord)] += 1
        elif y2 > y1 and x1 > x2:
            for xy_coord in range(0, y2-y1+1):
                field[(x1-xy_coord, y1+xy_coord)] += 1

    count = 0
    for i in range(1000):
        for j in range(1000):
            if field[(i, j)] > 1:
                count += 1
    return count


if __name__ == "__main__":
    print("Part 1 Answer:")
    print(part1())
    print("Part 2 Answer:")
    print(part2())

