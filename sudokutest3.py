
import sudoku
import unittest

class Test3Sudoku(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.puzzle = sudoku.parseSudokuFile('puzzle3.sudoku')

    def test_getPossibleValuesForZone(self):
        better = True
        while better:
            better = sudoku.runConstraints(self.__class__.puzzle)
        self.assertEqual(sudoku.getPossibleValuesForZone(self.__class__.puzzle,1,2),{1,2,3,4,5,6,7,9})

   
if __name__ == '__main__':
    unittest.main()