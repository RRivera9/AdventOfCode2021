from functools import cache

with open("Day12Input") as f:
    puzzle = f.read().split("\n")

graph = {}
for line in puzzle:
    node1, node2 = line.split("-")
    graph.setdefault(node1, [])
    graph[node1].append(node2)
    graph.setdefault(node2, [])
    graph[node2].append(node1)


#PART 1
def part1():
    count = 0
    finalPaths = []
    paths = [["start"]]

    while paths:
        currentPath = paths.pop()
        visited = set()
        visited.add("start")
        ###print(visited)
        ###print(f'currentpath is {currentPath}')
        ###print(visited)

        for i in currentPath[1:]:
            if i[0].islower():
                visited.add(i)

        for branches in graph[currentPath[-1]]:

            if branches not in visited:
                ###print(f'branches are {branches}, visited is {visited}')
                newpath = currentPath + [branches]
                ###print(f'newpath is {newpath}')
                if branches == "end":
                    finalPaths.append(newpath)
                else:
                    paths.append(newpath)
        ### print(f'paths are {paths}')
        count += 1
        if count % 1000000 == 0:
            print(count)
    return len(finalPaths)




#PART 2
def part2():
    finalPaths = []
    paths = [["start"]]

    while paths:
        currentPath = paths.pop()
        visited = set()
        visited.add("start")
        repeat = False
        ### print(visited)
        ### print(f'currentpath is {currentPath}')

        for i in currentPath:
            if i[0].islower() and i != "start":
                if i in visited:
                    repeat = True
                else:
                    visited.add(i)

        for branches in graph[currentPath[-1]]:
            if branches not in visited:
                newpath = currentPath + [branches]
                if branches == "end":
                    finalPaths.append(newpath)
                else:
                    paths.append(newpath)
            elif repeat is False and branches != "start":
                newpath = currentPath + [branches]
                if branches == "end":
                    finalPaths.append(newpath)
                else:
                    paths.append(newpath)

    print(f'paths are {finalPaths}')
    return len(finalPaths)

if __name__ == "__main__":
    print("Part 1 Answer:")
    print(part1())
    print("Part 2 Answer:")
    print(part2())