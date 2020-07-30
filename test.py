
import sudoku
import unittest

class TestSudoku(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.puzzle = sudoku.parseSudokuFile('puzzle1.sudoku')

    def test_parseSudokuChar_Dash(self):
        self.assertEqual(sudoku.parseSudokuChar('-'),[1,2,3,4,5,6,7,8,9])

    def test_parseSudokuChar_5(self):
        self.assertEqual(sudoku.parseSudokuChar('5'),[5])

    def test_parseValidSudokuLine(self):
        self.assertEqual(sudoku.parseSudokuLine("1,2,3,4,5,6,7,8,-"),[[1],[2],[3],[4],[5],[6],[7],[8],[1,2,3,4,5,6,7,8,9]])

    def test_getAllFinalValuesInRow(self):
        self.assertEqual(sudoku.getAllFinalValuesInRow(self.__class__.puzzle,2),[6,1,9,5])

    def test_getAllFinalValuesInCol(self):
        self.assertEqual(sudoku.getAllFinalValuesInCol(self.__class__.puzzle,5),[7,9,6,2,1,8])

    def test_loadWellFormattedFile(self):
        self.assertEqual(len(self.__class__.puzzle[1]),9)


if __name__ == '__main__':
    unittest.main()