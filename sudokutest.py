
import sudoku
import unittest

class TestSudoku(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.puzzle = sudoku.parseSudokuFile('puzzle1.sudoku')

    def test_parseSudokuChar_Dash(self):
        self.assertEqual(sudoku.parseSudokuChar('-'),{1,2,3,4,5,6,7,8,9})

    def test_parseSudokuChar_5(self):
        self.assertEqual(sudoku.parseSudokuChar('5'),{5})

    def test_parseValidSudokuLine(self):
        self.assertEqual(sudoku.parseSudokuLine("1,2,3,4,5,6,7,8,-"),[{1},{2},{3},{4},{5},{6},{7},{8},{1,2,3,4,5,6,7,8,9}])

    def test_getAllFinalValuesInRow(self):
        self.assertEqual(sudoku.getAllFinalValuesInRow(self.__class__.puzzle,1),{6,1,9,5})

    def test_getAllFinalValuesInCol(self):
        self.assertEqual(sudoku.getAllFinalValuesInCol(self.__class__.puzzle,4),{7,9,6,2,1,8})
    
    def test_getAllFinalValuesInZone(self):
        self.assertEqual(sudoku.getAllFinalValuesInZone(self.__class__.puzzle,3,3),{6,8,3,2})
    
    def test_getAllFinalValuesInZone2(self):
         self.assertEqual(sudoku.getAllFinalValuesInZone(self.__class__.puzzle,6,8),{2,5,7,8,9})

    def test_getPossibleValuesForCell(self):
        self.assertEqual(sudoku.getPossibleValuesForCell(self.__class__.puzzle,6,8),{4})

    def test_loadWellFormattedFile(self):
        self.assertEqual(len(self.__class__.puzzle[1]),9)

    def test_solve(self):
        sudoku.solve(self.__class__.puzzle)

if __name__ == '__main__':
    unittest.main()