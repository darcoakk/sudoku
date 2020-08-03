
import sudoku
import unittest

class TestSudoku(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.puzzle = sudoku.parseSudokuFile('puzzle3.sudoku')

    def test_getPossibleValuesForZone(self):
        self.assertEqual(sudoku.getPossibleValuesForZone(self.__class__.puzzle,1,2),{1,2,3,4,5,6,7,9})

   
if __name__ == '__main__':
    unittest.main()