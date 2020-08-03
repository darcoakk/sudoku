def printSudoku(puzzle):
    crow = 0
    for row in puzzle:
        if crow % 3 == 0:
            print("------------------------")
        printSudokuRow(row)
        crow += 1
    print("------------------------")
    

def printSudokuRow(row):
    ccol = 0
    for cell in row:
        if ccol % 3 == 0:
            print("|",end=" ")
        if len(cell) == 1:
            print(next(iter(cell)),end=" ")
        else:
            print(" ",end=" ")
        ccol += 1
    print("|")

def parseSudokuChar(c):
    if c == '-':
        return {1,2,3,4,5,6,7,8,9}
    else:
        return {int(c)}

def parseSudokuLine(l):
    numbers = l.strip('\n').split(",")
    return list(map(parseSudokuChar,numbers))

def parseSudokuFile(filepath):
    sudoku = []
    with open(filepath) as fp:
        line = fp.readline()
        while line:
            sudoku.append(parseSudokuLine(line))
            line = fp.readline()
    return sudoku

def getAllFinalValuesInRow(sudoku,r):
    finals = set()
    for cell in sudoku[r]:
        if len(cell) == 1:
            finals.update(cell)
    return finals
        
def getAllFinalValuesInCol(sudoku,c):
    finals = set()
    for row in sudoku:
        if len(row[c]) == 1:
            finals.update(row[c])
    return finals

def getSqIndex(i):
    return i // 3 * 3

def getAllFinalValuesInZone(sudoku,r,c):
    start_row = getSqIndex(r)
    start_col = getSqIndex(c)
    finals = set()
    for row in sudoku[start_row:start_row+3]:
        for cell in row[start_col:start_col+3]:
            if len(cell) == 1:
                finals.update(cell)
    return finals

def getPossibleValuesForZone(sudoku,r,c):
    start_row = getSqIndex(r)
    start_col = getSqIndex(c)
    finals = set()
    crow = start_row
    ccol = start_col
    for row in sudoku[start_row:start_row+3]:
        for cell in row[start_col:start_col+3]:
            if crow != r or ccol != c:
                finals.update(cell)
            ccol += 1
        crow += 1
    return finals

def getPossibleValuesForCell(sudoku,r,c):
    reduced = getAllFinalValuesInCol(sudoku,c).union(getAllFinalValuesInRow(sudoku,r)).union(getAllFinalValuesInZone(sudoku,r,c))
    return sudoku[r][c] - reduced

def solve(sudoku):
    better = True
    iteration = 0
    while better:
        rowIndex = 0
        iteration += 1
        print(iteration)
        better = False
        for row in sudoku:
            colIndex = 0
            for cell in row:
                if(len(cell) > 1):
                    initialSize = len(sudoku[rowIndex][colIndex])
                    sudoku[rowIndex][colIndex] = getPossibleValuesForCell(sudoku,rowIndex,colIndex)
                    newSize = len(sudoku[rowIndex][colIndex])
                    if newSize < initialSize:
                        better = True
                colIndex += 1
            rowIndex += 1
        printSudoku(sudoku)
        rowIndex = 0
        for row in sudoku:
            colIndex = 0
            for cell in row:
                if(len(cell) > 1):
                    initialSize = len(sudoku[rowIndex][colIndex])
                    p = sudoku[rowIndex][colIndex] - getPossibleValuesForZone(sudoku,rowIndex,colIndex)
                    if len(p) == 1:
                        sudoku[rowIndex][colIndex] = p
                        better = True
                colIndex += 1
            rowIndex += 1
        printSudoku(sudoku)

    print(sudoku)

    
puzzle = parseSudokuFile("puzzle2.sudoku")
solve(puzzle)
