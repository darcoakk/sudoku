
def parseSudokuChar(c):
    if c == '-':
        return [1,2,3,4,5,6,7,8,9]
    else:
        return [int(c)]

def parseSudokuLine(l):
    numbers = l.strip('\n').split(",")
    return list(map(parseSudokuChar,numbers))

def parseSudokuFile(filepath):
    sudoku = []
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            sudoku.append(parseSudokuLine(line))
            line = fp.readline()
            cnt += 1
    return sudoku

def getAllFinalValuesInRow(sudoku,r):
    r = r-1
    finals = []
    for cells in sudoku[r]:
        if len(cells) == 1:
            finals.append(cells[0])
    return finals
        
def getAllFinalValuesInCol(sudoku,c):
    c = c-1
    finals = []
    for row in sudoku:
        if len(row[c]) == 1:
            finals.append(row[c][0])
    return finals
   


# dev solve(sudoku):
#     rowIndex = 0
#     for row in sudoku:
#         rowIndex += 1
#         colIndex = 0
#         for col in row:
#             colIndex +=   
#             if(len(cell) > 1):
