with open("Day4Input") as f:
    puzzle = f.read().split("\n")

"""Check a bingoboard consisting of 0's for "haven't been hit yet" and 1's for hits to see if game has been won"""
def checkBoard(boardHit):
    for i in range(5):
        if boardHit[i] == [1, 1, 1, 1, 1]:
            return True, ("row", i)
    for i in range(5):
        boardColumn = True
        for j in range(5):
            if boardHit[j][i] == 0:
                boardColumn = False
        if boardColumn:
            return True, ("column", i)
    firstDiagonal = [boardHit[0][0], boardHit[1][1], boardHit[2][2], boardHit[3][3], boardHit[4][4]]
    secondDiagonal = [boardHit[0][4], boardHit[1][3], boardHit[2][2], boardHit[3][1], boardHit[4][0]]
    if firstDiagonal == [1, 1, 1, 1, 1]:
        return True, ("Diagonal", 1)
    if secondDiagonal == [1, 1, 1, 1, 1]:
        return True, ("Diagonal", 2)
    return False, ("None", False)


#PART 1
def part1():
    numbersToCall = list(map(int, puzzle[0].split(",")))
    bingoBoard = {}
    bingoBoardHits = {}

    #Converting puzzle into lists of ints for the board
    for i in range(int(len(puzzle[1::]) / 6)):
        bingoBoard[i] = puzzle[2 + i * 6:i * 6 + 7]
        for j in range(5):
            bingoBoard[i][j] = list(map(int, bingoBoard[i][j].split()))
        bingoBoardHits[i] = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

    #extremely slow
    winningBoardIndex = None
    gameWon = False
    while len(numbersToCall) > 0:
        calledNumber = numbersToCall.pop(0)
        for i in range(len(bingoBoard)):
            for j in range(5):
                #print(f' {bingoBoard[i][j] =}  {bingoBoardHits[i][j] =}  {calledNumber}')
                if (calledNumber in bingoBoard[i][j]):
                    index = bingoBoard[i][j].index(calledNumber)
                    bingoBoardHits[i][j][index] = 1
            if checkBoard(bingoBoardHits[i])[0] == True:
                winningBoardIndex = i
                gameWon = True
                break
        if gameWon:
            break
    remainingWinningNumbers = []
    for i in range(5):
        for j in range(5):
            if bingoBoardHits[winningBoardIndex][i][j] == 0:
                remainingWinningNumbers.append(bingoBoard[winningBoardIndex][i][j])

    return sum(remainingWinningNumbers) * calledNumber







#PART 2
def part2():
    numbersToCall = list(map(int, puzzle[0].split(",")))
    bingoBoard = {}
    bingoBoardHits = {}

    # Converting puzzle into lists of ints for the board
    for i in range(int(len(puzzle[1::]) / 6)):
        bingoBoard[i] = puzzle[2 + i * 6:i * 6 + 7]
        for j in range(5):
            bingoBoard[i][j] = list(map(int, bingoBoard[i][j].split()))
        bingoBoardHits[i] = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

    # extremely slow
    winningBoardIndex = None
    gameWon = False
    while len(numbersToCall) > 0:
        calledNumber = numbersToCall.pop(0)
        for i in range(len(bingoBoard)):
            if i in bingoBoardHits:
                for j in range(5):
                    # print(f' {bingoBoard[i][j] =}  {bingoBoardHits[i][j] =}  {calledNumber}')
                    if (calledNumber in bingoBoard[i][j]):
                        index = bingoBoard[i][j].index(calledNumber)
                        bingoBoardHits[i][j][index] = 1
                if checkBoard(bingoBoardHits[i])[0] == True:
                    if len(bingoBoardHits) == 1:
                        winningBoardIndex = i
                        gameWon = True
                        break
                    else:
                        del bingoBoardHits[i]
        if gameWon:
            break
    remainingWinningNumbers = []
    for i in range(5):
        for j in range(5):
            if bingoBoardHits[winningBoardIndex][i][j] == 0:
                remainingWinningNumbers.append(bingoBoard[winningBoardIndex][i][j])

    return sum(remainingWinningNumbers) * calledNumber

"""This should be cleaned up"""
def testCheckBoardNone():
    sampleBoardHit1 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    assert not checkBoard(sampleBoardHit1)[0]

def testCheckBoardRow():
    sampleBoardHit2 = [[1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    assert checkBoard(sampleBoardHit2)[0]

def testCheckBoardColumn():
    sampleBoardHit3 = [[1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]]
    assert checkBoard(sampleBoardHit3)[0]

def testCheckBoardDiagonal():
    sampleBoardHit4 = [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]
    assert checkBoard(sampleBoardHit4)[0]

if __name__ == "__main__":
    #testCheckBoardNone()
    #testCheckBoardRow()
    #testCheckBoardColumn()
    #testCheckBoardDiagonal()
    print("Part 1 Answer:")
    print(part1())
    print("Part 2 Answer:")
    print(part2())

